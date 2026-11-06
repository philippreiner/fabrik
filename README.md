# Fabrik

Skills, agents, and project rules for building software with Claude Code and Codex.

An agent says "done" in the same tone whether the work is done or not. So every change gets verified: a code review against rubrics, QA on the real screen, a second opinion from another vendor's model. Every mistake becomes a rule, a check, or a skill line. The codebase stays small and clean, because agents copy what they read.

Fabrik builds on Matt Pocock's [skills](https://github.com/mattpocock/skills) and Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack).

## Install

Run from your project root (Node.js 22.20 or later).

All Fabrik skills, for Claude Code and Codex:

```bash
npx skills add philippreiner/fabrik -a claude-code -a codex
```

One skill, for example `vernunft`:

```bash
npx skills add philippreiner/fabrik --skill vernunft -a claude-code -a codex
```

The companions that `qa`, `break-ui`, and the `tester` agent call on, and the anti-slop lint rules:

```bash
npx skills add philippreiner/redline -a claude-code -a codex
npx skills add vercel-labs/agent-browser --skill agent-browser -a claude-code -a codex
npx skills add dmmulroy/anti-slop --skill install-anti-slop -a claude-code -a codex
```

Then ask your agent to install anti-slop. Update everything with `npx skills update`.

## Skills

| Skill | Why it is in |
| --- | --- |
| [**redline**](https://github.com/philippreiner/redline/blob/main/skills/redline/SKILL.md) | Agents describe UI they never looked at. redline measures the real screen (alignment, spacing, hierarchy, words) and fixes what is off. |
| [**review-change**](https://github.com/philippreiner/fabrik/blob/main/skills/verify/review-change/SKILL.md) | Green tests do not prove a change is right. Reviews code against rubrics for shape, data, permissions, and performance, and rates every cut on a Simplification ladder. |
| [**qa**](https://github.com/philippreiner/fabrik/blob/main/skills/verify/qa/SKILL.md) | Most corrections are about results the agent never looked at. Screenshots each changed screen beside its baseline before handover. |
| [**vernunft**](https://github.com/philippreiner/fabrik/blob/main/skills/think/vernunft/SKILL.md) | Agents defend surprising designs. Tests a design against what users expect and how established systems solve it. |
| [`codex`](https://github.com/philippreiner/fabrik/blob/main/skills/verify/codex/SKILL.md) | One model misses what another catches. Runs a review or second opinion on the other vendor's model. |
| [`break-ui`](https://github.com/philippreiner/fabrik/blob/main/skills/verify/break-ui/SKILL.md) | Demo data hides layout bugs. Fills a list or card with worst-case data and fixes what breaks. |
| [`grilling`](https://github.com/philippreiner/fabrik/blob/main/skills/think/grilling/SKILL.md) | A plan with silent assumptions fails late. The agent interviews you, in rounds, until none are left. |
| [`shared-understanding`](https://github.com/philippreiner/fabrik/blob/main/skills/think/shared-understanding/SKILL.md) | Long explanations cost your attention. Picks the format you can hold: options, before/after, an analogy. |
| [`clarity`](https://github.com/philippreiner/fabrik/blob/main/skills/think/clarity/SKILL.md) | Busy readers need the point first. Writes and reviews decks, memos, and exec updates. |
| [`write-human`](https://github.com/philippreiner/fabrik/blob/main/skills/think/write-human/SKILL.md) | Readers stop trusting text that sounds generated. Removes AI tells from anything published or sent. |
| [`microcopy`](https://github.com/philippreiner/fabrik/blob/main/skills/think/microcopy/SKILL.md) | One concept, one name, on every screen. Writes labels, buttons, and error messages. |
| [`writing-for-agents`](https://github.com/philippreiner/fabrik/blob/main/skills/improve/writing-for-agents/SKILL.md) | A vague instruction makes the agent take a different path each run. Writes skills, agent definitions, and `AGENTS.md`. |
| [`github`](https://github.com/philippreiner/fabrik/blob/main/skills/improve/github/SKILL.md) | A mistake should happen once. Writes pull requests whose Learnings name the rule each mistake becomes. |
| [`retro`](https://github.com/philippreiner/fabrik/blob/main/skills/improve/retro/SKILL.md) | The setup should learn from its sessions. Run `/retro` to find where work went wrong and get the smallest fix. |
| [`codebase-audit`](https://github.com/philippreiner/fabrik/blob/main/skills/verify/codebase-audit/SKILL.md) | Complexity grows one reasonable change at a time. Run `/codebase-audit` for a ranked list of cuts. |
| [`test-audit`](https://github.com/philippreiner/fabrik/blob/main/skills/verify/test-audit/SKILL.md) | Tests that restate the code break on every refactor. Run `/test-audit` to prune them. |
| [`agent-browser`](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md) | QA needs a browser the agent can drive. By Vercel Labs. |
| [`install-anti-slop`](https://github.com/dmmulroy/anti-slop/blob/main/skills/install-anti-slop/SKILL.md) | Lint catches slop before review does. Copies Dillon Mulroy's Oxlint rules into your repo and keeps them updated. |

## Project template

`template/` holds the files a new project needs around the skills:

- `AGENTS.md` (linked as `CLAUDE.md`): rules for every task, with placeholders for your stack and checks
- `PRODUCT.md`, `DESIGN.md`, `docs/architecture.md`, `docs/plans/`, `docs/development/`
- Four agents for Claude Code and Codex: `explorer`, `oracle`, `tester`, `worker`
- `scripts/quality/`: checks that work in any git repository (see the FAQ)
- `scripts/ab`: drives agent-browser, waits for the network after each action, and saves screenshots to `.context/shots/`

Copy it without overwriting existing files, then fill in every `[placeholder]`:

```bash
gh repo clone philippreiner/fabrik /tmp/fabrik
cp -Rn /tmp/fabrik/template/. .
```

## FAQ

**Which agents does it support?**

Claude Code and Codex. The skills CLI also installs into Cursor, Gemini CLI, and others with `-a <agent>`.

**Where do the skills end up?**

In `.agents/skills/`, linked into `.claude/skills/`, with sources recorded in `skills-lock.json`. Commit all three.

**How do I add the lint rules?**

Install `install-anti-slop` and ask your agent to install anti-slop. It copies the rules into your repo, matches your Oxlint version, and enables them. The copy is yours to change; asking the agent to update anti-slop later merges upstream fixes and keeps your changes.

**Which quality checks come with the template?**

Three Node scripts that work in any git repository:

| Script | Checks |
| --- | --- |
| `check-comment-density.mjs` | Files where more than 12% of lines are comments, and single comments of 12+ lines or 70+ words. Scans files changed since `origin/main`; `--all` scans the repo, `--strict` fails on findings. Needs `typescript` 5.x. |
| `check-doc-caps.mjs` | `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, `docs/architecture.md`, and your own skills stay under a character cap, so a change removes text before it adds text. |
| `check-diff-volume.mjs` | Lines added and removed since `origin/main`, code apart from tests, with a note when test lines outgrow code lines. |

Run them from your quality gate, for example `node scripts/quality/check-comment-density.mjs --strict`.

**Why only four agents?**

Each does work the main thread should hand off:

- `explorer` looks things up in parallel.
- `oracle` gives an opinion without seeing your proposed answer.
- `tester` uses the running app as a persona.
- `worker` builds an independent slice of a change.

Code review runs in the main thread with `review-change`, and the `codex` skill gets a second review from another vendor's model.

**Why no hooks?**

A hook runs on every matching tool call in every workspace and slows each edit. Put guidance in `AGENTS.md`, a skill description, or your quality gate's output.

**What does the template expect from my codebase?**

Agents copy what they read, so the code has to be the documentation, an idea from pstack:

- Code shows behavior. Docs hold only intent, words, and decisions, so nothing describes behavior that has since changed.
- Comments state the reason a line exists or the invariant it keeps, in one or two lines.
- Each concept has one name across code, copy, and docs, listed in the Words of `PRODUCT.md`.
- When the agent copies a bad pattern, remove the pattern, or add a lint rule or a type. A warning paragraph does not stop it.
- Each test fails for a plausible broken implementation and survives a refactor that keeps behavior.

**How are the skills organized?**

`skills/verify/` checks the agent's work, `skills/think/` helps you decide and write with it, and `skills/improve/` turns mistakes into better rules. The folders do not change how you install.

**Who made what?**

`break-ui` is adapted from Emil Kowalski's [break-ui](https://github.com/emilkowalski/skills) (MIT). `writing-for-agents` and the shared-vocabulary practice follow Matt Pocock. `agent-browser` is by [Vercel Labs](https://github.com/vercel-labs/agent-browser), and [anti-slop](https://github.com/dmmulroy/anti-slop) by Dillon Mulroy (MIT).
