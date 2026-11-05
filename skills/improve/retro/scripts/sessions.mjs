#!/usr/bin/env node
// Measures agent sessions for a retro: Claude main threads and sub-agents,
// Codex runs, and the memory index, since a date. Writes each user message
// with the reply before it, and every spawn, for reading.
// Usage: node .agents/skills/retro/scripts/sessions.mjs [--since 2026-10-21] [--out .context/retro]

import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";
import { parseArgs } from "node:util";

const { values } = parseArgs({
  options: { since: { type: "string" }, out: { type: "string", default: ".context/retro" } },
});
const sinceText = values.since ?? new Date(Date.now() - 7 * 864e5).toISOString().slice(0, 10);
const since = Date.parse(sinceText);
const commonDir = execFileSync("git", ["rev-parse", "--git-common-dir"], { encoding: "utf8" }).trim();
const repo = path.dirname(path.resolve(commonDir));
const name = path.basename(repo);
const claudeProjects = path.join(homedir(), ".claude/projects");

const recent = (file) => statSync(file).mtimeMs >= since;
const at = (entry) => Date.parse(entry.timestamp ?? entry.payload?.timestamp ?? "");
const entries = (file) =>
  readFileSync(file, "utf8")
    .split("\n")
    .flatMap((line) => {
      try {
        return [JSON.parse(line)];
      } catch {
        return [];
      }
    });
const tally = (map, key, by = 1) => map.set(key, (map.get(key) ?? 0) + by);
const pct = (sorted, p) => sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * p))] ?? 0;
const k = (n) => `${Math.round(n / 1e3)}k`;
const oneLine = (text, max) => text.replace(/\s+/g, " ").trim().slice(0, max);

// A user message the person typed, without wrappers the harness adds.
const HARNESS = /^(This session is being continued|\[Request interrupted|Base directory for this skill|Caveat:|# AGENTS\.md)/;
function typed(content) {
  const parts = typeof content === "string" ? [content] : (content ?? []).map((part) => part.text ?? "");
  const text = parts
    .join("\n")
    .replace(/<(system_instruction|system-reminder|environment_context)>[\s\S]*?<\/\1>/g, "")
    .trim();
  return text && !text.startsWith("<") && !HARNESS.test(text) ? text : "";
}

const usage = (u = {}) => ({
  context: (u.input_tokens ?? 0) + (u.cache_read_input_tokens ?? 0) + (u.cache_creation_input_tokens ?? 0),
  output: u.output_tokens ?? 0,
});

const contextByDay = new Map();
const skills = new Map();
const spawns = [];
const messages = [];
const roles = new Map();
let mainSessions = 0;
let mainContext = 0;
let wakeups = 0;
let waitMs = 0;

const projectDirs = readdirSync(claudeProjects)
  .filter((dir) => dir.includes(name))
  .map((dir) => path.join(claudeProjects, dir));

for (const dir of projectDirs) {
  const worktree = path.basename(dir).split(`${name}-`).pop();
  for (const file of readdirSync(dir).filter((f) => f.endsWith(".jsonl"))) {
    const full = path.join(dir, file);
    if (!recent(full)) continue;
    const session = `${worktree} ${file.slice(0, 8)}`;
    const seen = new Set();
    const pending = new Map();
    let reply = "";
    let counted = false;
    for (const entry of entries(full)) {
      if (entry.isSidechain || !(at(entry) >= since)) continue;
      if (!counted) (counted = true), mainSessions++;
      const content = entry.message?.content;
      if (entry.type === "assistant") {
        if (!seen.has(entry.message.id)) {
          seen.add(entry.message.id);
          const { context } = usage(entry.message.usage);
          mainContext += context;
          if (context) contextByDay.set(entry.timestamp.slice(0, 10), [...(contextByDay.get(entry.timestamp.slice(0, 10)) ?? []), context]);
        }
        for (const part of content ?? []) {
          if (part.type === "text") reply = part.text;
          if (part.type !== "tool_use") continue;
          if (part.name === "Skill") tally(skills, part.input.skill);
          if (part.name === "ScheduleWakeup") wakeups++;
          if (part.name === "Agent" || part.name === "Task") {
            spawns.push(`- ${entry.timestamp.slice(5, 16)} ${session} · ${part.input.subagent_type ?? "general-purpose"}: ${part.input.description}`);
            pending.set(part.id, at(entry));
          }
        }
      } else if (entry.type === "user" && !entry.isMeta) {
        for (const part of Array.isArray(content) ? content : []) {
          if (part.type !== "tool_result" || !pending.has(part.tool_use_id)) continue;
          if (!JSON.stringify(part.content).includes("Async agent launched")) waitMs += at(entry) - pending.get(part.tool_use_id);
          pending.delete(part.tool_use_id);
        }
        const text = typed(content);
        if (text) messages.push({ when: entry.timestamp, session, reply, text });
      }
    }

    const subagents = path.join(dir, file.replace(".jsonl", ""), "subagents");
    if (!existsSync(subagents)) continue;
    for (const metaFile of readdirSync(subagents).filter((f) => f.endsWith(".meta.json"))) {
      const log = path.join(subagents, metaFile.replace(".meta.json", ".jsonl"));
      if (!existsSync(log) || !recent(log)) continue;
      const meta = JSON.parse(readFileSync(path.join(subagents, metaFile), "utf8"));
      const run = { minutes: 0, turns: 0, context: 0, output: 0, model: "" };
      const ids = new Set();
      let first;
      let last;
      for (const entry of entries(log)) {
        if (at(entry)) (first ??= at(entry)), (last = at(entry));
        if (entry.type !== "assistant" || ids.has(entry.message.id)) continue;
        ids.add(entry.message.id);
        const { context, output } = usage(entry.message.usage);
        run.turns++, (run.context += context), (run.output += output), (run.model = entry.message.model ?? run.model);
      }
      run.minutes = first ? (last - first) / 6e4 : 0;
      const role = meta.agentType ?? "unknown";
      roles.set(role, [...(roles.get(role) ?? []), run]);
    }
  }
}

const codex = new Map();
const codexRoot = path.join(homedir(), ".codex/sessions");
const codexFiles = existsSync(codexRoot)
  ? readdirSync(codexRoot, { recursive: true }).filter((f) => f.endsWith(".jsonl")).map((f) => path.join(codexRoot, f))
  : [];
for (const file of codexFiles.filter(recent)) {
  const log = entries(file);
  const meta = log.find((entry) => entry.type === "session_meta")?.payload;
  if (!meta?.cwd?.includes(name)) continue;
  const kind = typeof meta.source === "string" ? meta.source : "subagent";
  tally(codex, kind);
  if (kind === "exec" || kind === "subagent") continue;
  let reply = "";
  for (const { type, payload, timestamp } of log) {
    if (type !== "response_item" || payload?.type !== "message" || !(Date.parse(timestamp) >= since)) continue;
    const text = (payload.content ?? []).map((part) => part.text ?? "").join("\n");
    if (payload.role === "assistant") reply = text;
    if (payload.role === "user" && typed(text)) messages.push({ when: timestamp, session: `codex ${path.basename(meta.cwd)}`, reply, text: typed(text) });
  }
}

const memory = path.join(claudeProjects, repo.replaceAll("/", "-"), "memory");
const memoryIndex = path.join(memory, "MEMORY.md");

const subagentContext = [...roles.values()].flat().reduce((sum, run) => sum + run.context, 0);
console.log(`Since ${sinceText} for ${name}`);
console.log(`Main sessions ${mainSessions}, context ${(mainContext / 1e9).toFixed(1)}B; sub-agent runs ${[...roles.values()].flat().length}, context ${(subagentContext / 1e9).toFixed(1)}B`);
console.log(`Main thread waiting on foreground agents ${(waitMs / 36e5).toFixed(1)} h; wakeups ${wakeups}`);
console.log(`Codex sessions ${[...codex].map(([kind, n]) => `${kind} ${n}`).join(", ") || "none"}`);
if (existsSync(memoryIndex)) {
  const types = new Map();
  for (const file of readdirSync(memory).filter((f) => f.endsWith(".md") && f !== "MEMORY.md")) {
    tally(types, readFileSync(path.join(memory, file), "utf8").match(/^\s*type:\s*(\w+)/m)?.[1] ?? "none");
  }
  console.log(`Memory index ${readFileSync(memoryIndex, "utf8").length} chars; entries ${[...types].map(([type, n]) => `${type} ${n}`).join(", ")}`);
}
console.log(`Skills loaded ${[...skills].sort((a, b) => b[1] - a[1]).map(([skill, n]) => `${skill} ${n}`).join(", ")}`);

console.log("\nContext per main turn: day, turns, median, p90, max");
for (const [day, turns] of [...contextByDay].sort()) {
  const sorted = turns.sort((a, b) => a - b);
  console.log(`${day}  ${String(sorted.length).padStart(5)}  ${k(pct(sorted, 0.5)).padStart(5)}  ${k(pct(sorted, 0.9)).padStart(5)}  ${k(sorted.at(-1)).padStart(5)}`);
}

console.log("\nSub-agents: role, runs, median min, total min, median turns, output, context, model");
for (const [role, runs] of [...roles].sort((a, b) => b[1].length - a[1].length)) {
  const minutes = runs.map((run) => run.minutes).sort((a, b) => a - b);
  const turns = runs.map((run) => run.turns).sort((a, b) => a - b);
  const sum = (key) => runs.reduce((total, run) => total + run[key], 0);
  const models = new Map();
  for (const run of runs) tally(models, run.model.replace(/^claude-/, ""));
  console.log(
    `${role.padEnd(18)}${String(runs.length).padStart(4)}${pct(minutes, 0.5).toFixed(1).padStart(7)}${Math.round(sum("minutes")).toString().padStart(7)}${String(pct(turns, 0.5)).padStart(6)}${k(sum("output")).padStart(8)}${`${(sum("context") / 1e6).toFixed(0)}M`.padStart(8)}  ${[...models.keys()].join(", ")}`,
  );
}

mkdirSync(values.out, { recursive: true });
messages.sort((a, b) => (a.when ?? "").localeCompare(b.when ?? ""));
writeFileSync(
  path.join(values.out, "corrections.md"),
  messages.map(({ when, session, reply, text }) => `## ${(when ?? "").slice(5, 16)} ${session}\n> ${oneLine(reply, 600)}\n\n${oneLine(text, 1500)}\n`).join("\n"),
);
writeFileSync(path.join(values.out, "spawns.md"), `${spawns.sort().join("\n")}\n`);
console.log(`\n${messages.length} user messages in ${values.out}/corrections.md, ${spawns.length} spawns in ${values.out}/spawns.md`);
