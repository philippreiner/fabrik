---
name: documentation
description: "Write or update engineering docs, ADRs, and README sections about architecture, workflows, conventions, and gotchas. User-facing behavior belongs to document-product."
---

# Documentation

Write for the engineer or agent who needs to change this area safely. Preserve intent, ownership, lifecycle, and constraints that code cannot explain on its own.

Read the relevant implementation and existing docs first. Update the owning document before creating another. Flag drift; distinguish verified behavior from assumptions. Follow the destination the user named.

For a substantial domain document, start with purpose and an ownership map, then describe the model, lifecycle, and gotchas. For a small update, use the existing structure. Link definitions and contracts instead of repeating them. Include a diagram when it explains a relationship more clearly than prose.

Keep current-system docs independent of the latest diff. History belongs in the change record; durable architectural decisions follow the ADR criteria in `AGENTS.md`. A local choice that does not need an ADR can carry its reason next to the relevant explanation.

Use short, direct sentences and consistent repository terms. Lists suit steps and parallel facts; prose suits connected reasoning. Preserve useful technical detail and meaningful uncertainty. Omit symbol inventories, exhaustive enumerations, and signatures that a quick code read supplies.

Update only affected docs. Optimize for selective reading: split large manuals by task, keep glossary entries brief, and link to lifecycle detail in its owning doc. Do not create a new overview, data-model document, or glossary merely to satisfy a template. The worktree change record follows `docs/changelog/README.md`.
