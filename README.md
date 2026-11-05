# Fabrik

My software factory: the skills, agents, and project rules I use to build software with coding agents. *Fabrik* is German for factory. Here the workers are agents.

It runs in Claude Code and Codex, and it comes from two production codebases where it was cut down until only what earned its place stayed.

## Install

Skills install with the [skills CLI](https://github.com/vercel-labs/skills). Run it from your project root:

```bash
# Every Fabrik skill, for Claude Code and Codex
npx skills add philippreiner/fabrik -a claude-code -a codex

# One skill
npx skills add philippreiner/fabrik --skill vernunft -a claude-code -a codex

# The companions the skills call on
npx skills add philippreiner/redline -a claude-code -a codex
npx skills add vercel-labs/agent-browser --skill agent-browser -a claude-code -a codex
```

The CLI keeps one copy in `.agents/skills/`, links it for Claude Code, and records the source in `skills-lock.json`. `npx skills update` pulls new versions.

The project template (agents, `AGENTS.md`, docs, checks) is plain files. Copy it without overwriting what you have, then fill in the `[placeholders]`:

```bash
gh repo clone philippreiner/fabrik /tmp/fabrik
cp -Rn /tmp/fabrik/template/. .
```

## Highlights

- **[redline](https://github.com/philippreiner/redline)**: design for agents. Lenses, numbers, and browser scripts that measure the UI an agent built instead of trusting its description of it. Alignment, hierarchy, spacing, words, and slop, checked on the real screen.
- **The review loop**: `review-change` reads every change against rubrics for code shape, data, permissions, and performance, and rates every cut on a Simplification ladder. `qa` looks at the change the way its user meets it, screenshot beside baseline. `codex` hands a deep review to the other vendor's model, which has other blind spots. The `tester` agent uses the product as a persona and reports what breaks.
- **vernunft**: German for reason, good sense. A least-astonishment check that holds a design against what its user expects and how established systems solve it. The second opinion when something feels off, or when you challenge the agent.

## Three buckets

Fabrik does three things. Each bucket is a folder under `skills/`.

### Verify: make the agent's work checkable

An agent says "done" in the same tone whether it is or not. These skills turn claims into evidence.

| Skill | Job |
| --- | --- |
| `review-change` | Code review rubrics, deep review, and the Simplification ladder |
| `qa` | Check screens, flows, and strings as the user meets them |
| `break-ui` | Feed a surface worst-case data until it breaks, then fix it |
| `codex` | Run a review or second opinion on the other vendor's model |
| `test-audit` | Prune tests that restate the implementation (invoked by hand) |
| `codebase-audit` | Rank whole-repository simplifications (invoked by hand) |

The template adds deterministic checks: an Oxlint plugin with eight anti-slop type rules and a character cap on the shared docs.

### Think: work and decide with the agent

A human reader has limited attention. These skills spend it on the decision, not on the agent's process.

| Skill | Job |
| --- | --- |
| `vernunft` | Test a design against expectations and established solutions |
| `grilling` | Interview you, in rounds, until the plan has no silent assumptions |
| `shared-understanding` | Pick the format that lets you hold an idea: options, before/after, analogy |
| `clarity` | Clear writing for smart, busy readers: decks, memos, exec updates |
| `write-human` | Prose without AI tells, for anything published, sent, or committed |
| `microcopy` | Labels, buttons, and errors |

`template/AGENTS.md` sets the same rules for every reply: the first sentence says what happened, facts apart from inference, at most three questions, each with an example and a recommendation.

### Improve: let the setup learn

| Skill | Job |
| --- | --- |
| `retro` | Measure recent sessions, find where work went wrong, propose the smallest fix to the environment (invoked by hand) |
| `writing-for-agents` | How to write skills, agents, and `AGENTS.md` so the agent takes the same path every run |
| `github` | Commits and pull requests, each with a Learnings section that names the rule a mistake should become |

A lesson moves up the cheapest rung that holds it: a type, then a check, then a pointer, then a skill line, and an `AGENTS.md` line last.

## The codebase is the documentation

Agents read the code more than the docs, and they copy what they find. A long comment, a stale pattern, or a second word for the same thing gets repeated in every change that touches it. So the codebase itself has to be the teaching material:

- **Code shows behavior; docs hold intent.** `PRODUCT.md` says why and in which words, `docs/architecture.md` holds boundaries and decisions with the fact that would reopen each. Feature docs, ADRs, and change logs go stale and anchor agents to old shapes, so there are none.
- **Comments stay short.** A comment states the reason a line exists or the invariant it keeps. Restatement and history come out.
- **One vocabulary.** Every concept has one name across code, copy, docs, and agent replies, recorded in the Words of `PRODUCT.md`, after Matt Pocock's practice of a shared domain glossary.
- **Bad patterns get removed, not documented.** When the agent copies something wrong, the fix is the code, a lint rule, or a type, not a warning paragraph.
- **Docs have caps.** `check-doc-caps.mjs` counts characters in `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, `docs/architecture.md`, and your own skills. A change retires text before it adds text.
- **Tests prove behavior.** Each test fails for a plausible broken implementation and survives a behavior-preserving refactor. Database rules are proven against a real database.

## What the template holds

```text
template/
├── AGENTS.md                 rules for every task; CLAUDE.md links here
├── PRODUCT.md                who it serves, principles, Words
├── DESIGN.md                 your design decisions; the craft lives in redline
├── docs/
│   ├── architecture.md       ownership, boundaries, decisions with reasons
│   ├── plans/README.md       where the product goes next
│   └── development/          quality loop and setup
├── .claude/agents/           explorer, oracle, tester, worker
├── .codex/agents/            the same four for Codex
└── scripts/quality/          anti-slop Oxlint plugin, doc caps
```

Four agents, each for work the main thread should not do itself: `explorer` looks things up in parallel, `oracle` gives an unanchored recommendation or goal review, `tester` uses the product as a persona, `worker` builds an independent slice. Everything else stays in the main thread, where you can steer it.

To use the lint plugin, add it to `.oxlintrc.json` and install `@oxlint/plugins`:

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

## What was cut, and why

The setup used to be larger. Session retros showed what helped:

- **Four agents, not nine.** Reviewer, writer, researcher, and ideas agents were removed. Review runs in the main thread with `review-change`, and an independent read goes to the other vendor's model.
- **No hooks.** A hook runs on every matching tool call in every workspace, and a per-edit lint hook slowed every edit. Nudges go in `AGENTS.md`, skill descriptions, or the quality gate's output.
- **Review split from QA.** Most corrections were about visible results the agent had not looked at, not code bugs. So `qa` became its own step.
- **No specs, ADRs, or context files.** Plans live in `docs/plans/` until they ship. Decisions are one line each in `docs/architecture.md`.

## Credits

`break-ui` is adapted from Emil Kowalski's [break-ui](https://github.com/emilkowalski/skills) (MIT). `writing-for-agents` and the shared-vocabulary practice follow Matt Pocock. `agent-browser` is by [Vercel Labs](https://github.com/vercel-labs/agent-browser).
