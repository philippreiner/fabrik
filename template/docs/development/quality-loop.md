# Development quality loop

This file owns commands, automated gates, and CI behavior. [AGENTS.md](../../AGENTS.md) owns handover requirements; the `review-change` skill owns code review judgment; the `qa` skill owns how a change looks and works for its user.

## Choose a command

| Command | Scope and effect |
| --- | --- |
| `[quality command]` | The whole gate: static checks, lint, typecheck, build, then all tests |
| `[e2e command] <spec>` | The changed journey's browser spec; the whole suite on request |

Run the gate once, in the foreground. It runs every step even after one fails and ends with one verdict line; after a fix, rerun only the failed steps.

## Gate owners

| Owner | Checks |
| --- | --- |
| Lint config with [anti-slop](https://github.com/dmmulroy/anti-slop) (`install-anti-slop` skill) | Type evidence, imports, cycles, and low-signal patterns |
| [Doc caps](../../scripts/quality/check-doc-caps.mjs) | Character caps for `AGENTS.md`, `DESIGN.md`, `PRODUCT.md`, `docs/architecture.md`, and own skills |
| [Comment density](../../scripts/quality/check-comment-density.mjs) | Comment ratio per changed file and long comment blocks |
| [Diff volume](../../scripts/quality/check-diff-volume.mjs) | Code and test lines changed since `origin/main` (report only) |
| `[architecture test]` | Package dependency direction |

The repository has no agent hooks: a hook runs on every matching tool call in every workspace, so guidance goes in `AGENTS.md`, a skill description, or the gate's output instead.

## Integration suites

[How database tests get their own database, and how race tests run competing writes on two connections.]

## E2E

[When browser specs run, and which journeys they own.]

## CI

[What runs on pull requests, what waits for the release, and which paths skip CI.]
