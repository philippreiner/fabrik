---
name: github
description: "Turn local changes into merge-ready history: commits, branches, pushes, merges and conflicts, pull requests with their learnings, review and CI feedback, and releases to production. Create, read, and label GitHub issues. Reading status or a diff needs no skill."
---

# Git and GitHub workflow

Turn a local diff into reviewable history: learn what the branch actually changed and describe it once in the pull request. The pull request body is the record; there are no separate change records. GitHub issues are intake and tracking; plans stay in `docs/plans/`.

## Learn the state

- Diff against the default branch (`git diff origin/main...`), then read status, staged changes, and branch commits.
- Separate the requested change from pre-existing or unrelated work. Never stage, rewrite, or discard the unrelated part.
- Push, open or update a pull request, comment, merge, or rewrite shared history only when the user asks for that state change in the current message; an earlier approval does not carry over.

## Issues

Issues are intake, not specs. Clear lists, no mini-prose.

- **Read:** `gh issue list` and `gh issue view <n>`. If the user names issues or a batch of work, look them up first.
- **Write:** `gh issue create` or `gh issue edit`, when the user asks. Title names the outcome.
  - Goal / Intention / Problem: what should become true, or what is broken
  - Consider / Context / Steps: known constraints and context
  - Complete when: Gherkin (`Given` / `When` / `Then`), observable
  - Notes / Links: plan path, related issues
- **Labels:** `gh label list`, then apply existing ones. Do not create labels.
- **Reuse:** search open issues before creating. One issue per tracked piece of work, not per PR. Small related bugs can share a collection issue.
- **PRs:** the implementing PR links and closes the issue (`Fixes #<n>`).

## Commits

- "Commit" or "commit and push" covers every change in the worktree, including changes from agents working in parallel. Group them into coherent commits; do not leave another agent's changes unstaged.
- One coherent review unit per commit. Stage explicit paths and check the staged diff before committing.
- Imperative, sentence-case subject naming the outcome: `Fix bulk upload processing stalls`. No trailing period, no `update`/`WIP`/file lists, no Conventional Commits in this history.
- Add a body only for motivation or constraints the diff cannot show.
- Run validation required by `AGENTS.md`; reuse passing evidence for unchanged code.

## Pull request

Write for a busy human reviewer who has not seen the conversation. Help them
understand why the change matters, what it does, and where to focus their judgment.
Use `write-human` for the copy; derive facts from the verified branch diff, not
from the session.

- **History:** a squash merge keeps the PR title (or a lone commit's subject) and the commit messages; the PR body stays on GitHub. Anything a later `git log` reader needs goes into a commit body.
- **Title:** name the concrete outcome in imperative sentence case. It becomes the squash commit subject, so it must stand alone: `Keep inbox runs going when email delivery fails`, not `Fix inbox bug`.

Every body has the same shape, in this order. Omit a section that would be empty, except Verification.

1. **Opening** (no heading): the problem and the resulting behavior in plain language, including removed or changed behavior. A concrete trigger and before/after example often does this best. For guidance or internal work, name whose work improves and how.
2. **Review focus**: only the model or ownership decisions, trade-offs, and risks that help assess the diff, with the decisive file or symbol. Routine details stay in the diff.
3. **Verification**: the checks actually run and what they establish, then what was not verified. Separate automated tests, manual checks, and expectations. Link screenshots when they help judge the result.
4. **Learnings**: one bullet per lesson that should prevent a repeat: a user correction, review feedback that found a real defect, guidance or a tool that misled an agent, or a bug that needs a rule. Each bullet states what went wrong, the rule, and where it now lives (lint rule, test, type, skill or doc line). Encode the rule in this PR when it is cheap; otherwise write `not encoded`. Never invent a learning to fill the section.

A tiny PR is one sentence plus Verification. Use bullets inside a section when they make it easier to scan. Avoid file inventories, session history, agent handoffs, ceremonial checklists, and unsupported claims such as “robust” or “fully tested”.

Before creating or updating:

- Check the base, included commits, CI state, and whether a PR already exists.
- Link the tracking issue with `Fixes #<n>` when one exists.
- Ensure each new table, binding, event, trigger, capability, flag, or option has a shipped caller; one without a caller is a merge blocker. Include that evidence in the description only when it helps review.
- Rewrite the title and body around the final scope, removing stale claims and abandoned approaches. Add Learnings from review rounds as they land.
- Mark open work and merge blockers explicitly; prefer a draft when known blockers remain.
- Read it cold: can a colleague understand the change and its verification without the chat?

Find past learnings with `gh pr list --state merged --search "Learnings in:body" --limit 50`.

## Review and CI feedback

- Judge each finding first: valid, already resolved, out of scope, unproven, or false premise. A finding without a concrete trigger and wrong outcome is unproven; reject it in one line. Fix accepted ones at the root, then run focused validation.
- Add a Learning for each accepted finding that a rule could have prevented; keep comment-by-comment history out of the body.
- Reply to or resolve external review threads only when asked.
- After the last push, recheck merge readiness: required checks, unresolved threads, conflicts.

For merge conflicts, keep both branches' intent. Stage only resolved paths, then complete the authorized merge or rebase. Surface incompatible intent rather than inventing behavior.

## Release

For a repository that releases through a pull request from `main` into `release`, whose merge deploys to production. Open, merge, or deploy only when the user asks in the current message. `docs/development/deployment.md` owns the rules.

1. `gh pr create --base release --head main`. Title: `Release <yyyy-mm-dd>`. Body: one bullet per included pull request (`git log --first-parent --format='%s' origin/release..origin/main`), then Verification.
2. When the release contains a large feature, run the full E2E suite locally and report the result in Verification.
3. Watch the **Release** checks. Fix a failure on a branch from `main` with its own pull request; the release pull request picks up the merge.
4. Merge with a merge commit: `gh pr merge <n> --merge`. A squash makes `release` drift from `main`.
5. Watch the deploy job of the push run on `release`. After it succeeds, check the production behavior the release changed.
