# Fabrik

Skills, agents, and project rules for building software with Claude Code and Codex. One command installs the skills into any project, and a template sets up the rest.

## Install

Run from your project root (Node.js 22.20 or later):

```bash
npx skills add philippreiner/fabrik -a claude-code -a codex
npx skills add philippreiner/redline -a claude-code -a codex
npx skills add vercel-labs/agent-browser --skill agent-browser -a claude-code -a codex
```

The first line installs every Fabrik skill. Pick one with `--skill <name>`. The other two install the companions that `qa`, `break-ui`, and the `tester` agent call on. Update later with `npx skills update`.

## Skills

| Skill | Use it to | Starts |
| --- | --- | --- |
| **redline** | Design, review, and polish UI; measures the real screen with browser scripts. [Separate repo](https://github.com/philippreiner/redline) | On its own |
| **review-change** | Review a code change against rubrics for shape, data, permissions, performance, and tests | On its own |
| **qa** | Check a change the way its user meets it, screenshot beside baseline | On its own |
| **vernunft** | Test a design against what users expect and how established systems solve it | On its own |
| `codex` | Get a review or second opinion from the other vendor's model | On its own |
| `break-ui` | Fill a list or card with worst-case data and fix what breaks | On its own |
| `grilling` | Have the agent interview you until a plan has no silent assumptions | On its own |
| `shared-understanding` | Get an idea explained in the format you can hold: options, before/after, analogy | On its own |
| `clarity` | Write decks, memos, and exec updates for busy readers | On its own |
| `write-human` | Write prose without AI tells | On its own |
| `microcopy` | Write labels, buttons, and error messages | On its own |
| `writing-for-agents` | Write skills, agent definitions, and `AGENTS.md` | On its own |
| `github` | Commit, open pull requests with Learnings, handle review and CI | On its own |
| `retro` | Find where recent sessions went wrong and fix the setup | `/retro` |
| `codebase-audit` | Rank simplifications across the whole repository | `/codebase-audit` |
| `test-audit` | Prune tests that restate the implementation | `/test-audit` |

"On its own" means the agent picks the skill when the task matches; you can also type its name.

## Project template

`template/` holds the files a new project needs around the skills:

- `AGENTS.md` (linked as `CLAUDE.md`): rules for every task, with placeholders for your stack and checks
- `PRODUCT.md`, `DESIGN.md`, `docs/architecture.md`, `docs/plans/`, `docs/development/`
- Four agents for Claude Code and Codex: `explorer`, `oracle`, `tester`, `worker`
- `scripts/quality/`: eight anti-slop Oxlint rules and a size cap for the shared docs

Copy it without overwriting existing files, then fill in every `[placeholder]`:

```bash
gh repo clone philippreiner/fabrik /tmp/fabrik
cp -Rn /tmp/fabrik/template/. .
```

## FAQ

**Which agents does it support?** Claude Code and Codex. The skills CLI also installs into Cursor, Gemini CLI, and others with `-a <agent>`.

**Where do the skills end up?** In `.agents/skills/`, linked into `.claude/skills/`, with sources recorded in `skills-lock.json`. Commit all three.

**How do I turn on the lint rules?** Install `@oxlint/plugins` and add the plugin to `.oxlintrc.json`:

```json
{
  "jsPlugins": [{ "name": "anti-slop", "specifier": "./scripts/quality/anti-slop/index.ts" }],
  "rules": {
    "anti-slop/no-chained-type-assertions": "error",
    "anti-slop/no-widen-then-assert": "error",
    "anti-slop/no-module-mocking": "warn"
  }
}
```

The other rules are in `scripts/quality/anti-slop/index.ts`.

**What does the doc cap do?** `node scripts/quality/check-doc-caps.mjs` fails when `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, `docs/architecture.md`, or one of your own skills grows past its character limit. Add it to your quality gate so a change removes text before it adds text.

**Why only four agents?** Each does work the main thread should hand off:

- `explorer` looks things up in parallel.
- `oracle` gives an opinion without seeing your proposed answer.
- `tester` uses the running app as a persona.
- `worker` builds an independent slice of a change.

Code review runs in the main thread with `review-change`, and the `codex` skill gets a second review from another vendor's model.

**Why no hooks?** A hook runs on every matching tool call in every workspace and slows each edit. Put guidance in `AGENTS.md`, a skill description, or your quality gate's output.

**What does the template expect from my codebase?** Agents copy what they read, so the code has to be the documentation:

- Code shows behavior. Docs hold only intent, words, and decisions, so nothing describes behavior that has since changed.
- Comments state the reason a line exists or the invariant it keeps, in one or two lines.
- Each concept has one name across code, copy, and docs, listed in the Words of `PRODUCT.md`.
- When the agent copies a bad pattern, remove the pattern, or add a lint rule or a type. A warning paragraph does not stop it.
- Each test fails for a plausible broken implementation and survives a refactor that keeps behavior.

**How are the skills organized?** `skills/verify/` checks the agent's work, `skills/think/` helps you decide and write with it, and `skills/improve/` turns mistakes into better rules. The folders do not change how you install.

**Credits?** `break-ui` is adapted from Emil Kowalski's [break-ui](https://github.com/emilkowalski/skills) (MIT). `writing-for-agents` and the shared-vocabulary practice follow Matt Pocock. `agent-browser` is by [Vercel Labs](https://github.com/vercel-labs/agent-browser).
