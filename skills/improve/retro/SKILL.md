---
name: retro
description: "Review recent sessions, or the ones the user names, and propose changes to the agent environment: checks, skills, agents, AGENTS.md, memory, docs."
disable-model-invocation: true
---

# Retro

## 1. Measure

Run `node .agents/skills/retro/scripts/sessions.mjs --since <date>`, with the
date of the last retro or the one the user names. It prints sessions, context
per main turn by day, sub-agent runs per role, Codex runs, skills loaded,
wakeups, and the memory index size, and writes `corrections.md` (each user
message under the agent reply before it) and `spawns.md` to `.context/retro/`.
In Conductor, model and effort per session live in
`~/Library/Application Support/com.conductor.app/conductor.db` (open it read-only).

Done when you have the numbers and both files.

## 2. Find the moments

Read every message in `corrections.md`. A moment is where the work went wrong
or slow: a repeated correction, a wrong turn, a skipped check, a rule read and
not applied, a fact that was hard to find, a status the user had to ask for, a
question a read or a run could have settled. The reply above a message usually
shows the cause; open the transcript only when it does not.

Weigh the roster in `spawns.md`: each role's jobs against its description,
misuse, and rarely used roles. A sub-agent earns its place with parallel work or
a fresh context; a role the main thread or another role covers is a removal.

Inputs the user brings, such as posts, articles, or another repository's retro,
are candidates: back each with a moment, or label it the user's idea.

Done when every correction belongs to a moment or is dismissed as a one-off.

## 3. Propose

For each moment, name the smallest change to the environment that would have
prevented it, in this order of preference:

1. A type or constraint that makes the state unrepresentable.
2. A deterministic check that fails the quality gate, or a permission rule.
3. A canonical helper, or a pointer in `AGENTS.md` Sources so the fact is found.
4. A line in a skill or agent definition, for a judgment call, with the failure as its example.
5. A line in `AGENTS.md`, for a judgment call every task meets. Last resort.

Then look for what to remove: a rule nobody needed, a line the agent obeys by
default, two lines that say one thing, a role nobody needs, a memory entry that
git or the repo already records. A removal counts as much as an addition.

Nudge with text: a line in `AGENTS.md` Done, a skill description, or
quality gate output. A hook runs on every matching call in every workspace;
propose one only for data safety, priced as runtime times calls per day times
parallel workspaces.

Check each change against current `main`, since a later session may have fixed
it. Follow `writing-for-agents` for wording and placement, and change
`.claude/agents/` and `.codex/agents/` together.

## 4. Report

Lead with the numbers in a few lines, against the last retro's when known.
Then one table, most costly moment first:

| # | Moment | Evidence (session · date) | Change | Tier |
| --- | --- | --- | --- | --- |

Close with what held and stays, and the inputs not adopted, one line each.
Wait for the user's pick before applying anything.
