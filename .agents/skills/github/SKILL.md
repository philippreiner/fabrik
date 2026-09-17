---
name: github
description: "Turn local changes into merge-ready history: commits, branches, pushes, pull requests, review and CI feedback, and the change record. Reading status or a diff needs no skill."
---

# Git and GitHub workflow

Turn a local diff into reviewable history: learn what the branch actually changed, record it once in the change record, and derive commit and pull request copy from that record so the three never drift.

## Learn the state

- Diff against the default branch (`git diff origin/main...`), then read status, staged changes, and branch commits.
- Separate the requested change from pre-existing or unrelated work. Never stage, rewrite, or discard the unrelated part.
- Push, open a pull request, comment, merge, or rewrite shared history only when the user asked for that state change.

## Record what we did

`docs/changelog/README.md` owns the change-record shape and naming. In this skill's flow:

Create or update the record when implementing or preparing a commit or PR, not for a read-only status or review request.

- One entry per pull request. Find the worktree's existing entry before creating one; update it as review changes the result.
- Write for a reader who did not follow the work: what changed for the user, what was removed, and a learning only when it prevents a repeat. Learnings name what the user corrected and what changed because of it.
- Do not invent impact, decisions, or learnings to fill sections. Omit an empty section.

## Commits

- One coherent review unit per commit. Stage explicit paths and check the staged diff before committing.
- Imperative, sentence-case subject naming the outcome: `Fix bulk upload processing stalls`. No trailing period, no `update`/`WIP`/file lists, no Conventional Commits in this history.
- Add a body only for motivation or constraints the diff cannot show.
- Run validation required by `AGENTS.md`; reuse passing evidence for unchanged code. Do not bypass hooks unless the user accepts the consequence.

## Pull request

- Name the concrete outcome in the title. Lead the description with the problem and resulting behavior; add a trigger and before/after example when it makes the change clearer. Write for a reviewer who has not seen the conversation.
- Scale the description to the diff. A small PR needs one or two sentences and relevant validation. For larger work, explain the key ownership or model decision, material trade-offs, and risks. Include checks actually run and any verification limits; link evidence when useful.
- Rewrite the title and description when scope changes so they describe the final implementation. Omit session history, abandoned approaches, file inventories, and claims the diff or checks do not support. Follow an existing PR template when present.
- Generate from the verified branch diff and change record, not conversation memory.
- Mark open work and merge blockers explicitly. Prefer a draft when known blockers remain.
- Before creating or updating, check the base, included commits, CI state, and whether a pull request already exists.

## Review and CI feedback

- Judge each finding first: valid, already resolved, out of scope, or false premise. Fix accepted ones at the root, then run focused validation.
- Record material outcomes in the change record; keep comment-by-comment history out of it.
- Reply to or resolve external review threads only when asked.
- After the last push, recheck merge readiness: required checks, unresolved threads, conflicts.

For merge conflicts, inspect both branches' intent and follow `AGENTS.md`. Stage only resolved paths, then complete the authorized merge or rebase. Surface incompatible intent rather than inventing behavior.
