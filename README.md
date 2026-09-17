# Fabrik

Portable agent instructions, skills, review roles, and project-document templates.

The folder is intentionally project-neutral. Replace bracketed placeholders in
`AGENTS.md`, `CONTEXT.md`, `PRODUCT.md`, `DESIGN.md`, and `QUALITY.md` when
installing it in a project. The skill files are the reusable starting point;
keep project-specific rules in the target project's instruction files.

## Included

```text
.
├── .agents/skills/       reusable agent skills
├── .agents.md            alias to AGENTS.md for tools that expect it
├── .claude/agents/       Claude agent role definitions
├── .codex/agents/        Codex agent role definitions
├── AGENTS.md             shared project instructions and placeholders
├── CLAUDE.md             symlink to AGENTS.md
├── CONTEXT.md            domain and codebase map template
├── DESIGN.md             UI and interaction rules template
├── PRODUCT.md            product context template
└── QUALITY.md            review checklist template
```

## Symlinks

The setup has one shared source of truth for instructions and one shared skill
directory:

```text
CLAUDE.md          -> AGENTS.md
.agents.md         -> AGENTS.md
.claude/skills     -> ../.agents/skills
```

If a project also needs the shorthand filename `.agents.md`, create it as an
alias to the canonical file rather than maintaining a second instruction set:

```bash
ln -s AGENTS.md .agents.md
```

Verify the links after copying:

```bash
test "$(readlink CLAUDE.md)" = "AGENTS.md"
test "$(readlink .agents.md)" = "AGENTS.md"
test "$(readlink .claude/skills)" = "../.agents/skills"
```

## Install into a project

Copy the folders and templates into the project root, preserving the links:

```bash
cp -a .agents .claude .codex .agents.md AGENTS.md CLAUDE.md CONTEXT.md DESIGN.md PRODUCT.md QUALITY.md /path/to/project/
```

Inspect existing files before copying. Merge project-specific instructions
instead of overwriting them, and do not copy credentials, local environment
files, generated artifacts, or unrelated product documentation.

Then replace the bracketed placeholders and add only the architecture and
workflow references that the target project actually has. Keep `AGENTS.md` as
the canonical instruction file. Commit the symlinks as symlinks so Claude and
Codex read the same skill and instruction content in every checkout.

## Updating the setup

When a shared rule changes, update the canonical file or skill once and check
both `.claude/agents/` and `.codex/agents/` for corresponding role changes.
Keep tool-specific model settings in their native directories. Run a repository
search for old product names and paths before publishing a new version.
