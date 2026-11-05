# Working on Fabrik

Fabrik is a skill collection and a project template, not an application. `README.md` explains both.

- `skills/<bucket>/<name>/SKILL.md` installs through `npx skills add philippreiner/fabrik`. Buckets: `verify`, `think`, `improve`. A skill name is unique across buckets.
- `template/` is copied into a project root. Its `AGENTS.md`, docs, and agents carry `[placeholders]` for project facts; everything else stays project-neutral.
- Skills are written for the project they are installed into: paths such as `.agents/skills/review-change/...`, `docs/architecture.md`, and `PRODUCT.md` refer to that project.
- Follow `skills/improve/writing-for-agents` when editing a skill, an agent, or an `AGENTS.md`. Keep `template/.claude/agents/` and `template/.codex/agents/` aligned; model choices stay runtime-specific.
- Keep each `SKILL.md` under 12,000 characters. Before publishing, search for product names from the projects a change came from.
- Upstream skills (redline, agent-browser) install from their own repositories; do not vendor them here.
