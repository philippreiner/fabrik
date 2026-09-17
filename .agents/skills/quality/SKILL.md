---
name: quality
description: Review a named scope, or self-review behavior and contract changes before handover. Includes deep maintainability review.
---

# Quality

Use repository-root `QUALITY.md` for criteria and `AGENTS.md` for required checks. This skill owns the review process.

Prefer explicit contracts and fewer redundant concepts. Follow neighboring patterns and understand why a protection exists before proposing its removal.

## Route the task

- Explicit review: assess and report without editing unless fixes were requested.
- Handover: review behavior, contract, permission, persistence, or workflow changes once, at a depth proportional to risk. Mechanical, copy, and layout edits without those effects need only a focused check.
- Requested deep review: inspect the named scope for ownership or model changes that remove whole branches, states, wrappers, or coordination layers. Demonstrate the maintenance consequence; a passing checklist is not the ceiling.
- Whole-repository architectural audit: `/codebase-audit` is the separate user-invoked workflow.

Stay inside the requested scope. Stop when the review decision is supported.

## Establish the evidence

Establish the intended behavior, canonical owner, and neighboring case that must remain valid. Inspect relevant callers, invariants, permissions, contracts, and tests around the diff. For changed state transitions, check repeat, concurrency, and partial failure; local status alone may not prove released resources or available results.

Use incident reports as hypotheses. When proposing a review rule, check it against a known regression and a valid implementation it must allow. Extend an existing criterion where possible; keep the rule only if it distinguishes the two.

## Review

Apply relevant criteria, prioritizing user harm and system risk over maintainability. For bugs, verify the cause; name an introducing change only with evidence. For UI, inspect the composed page against `DESIGN.md`.

Report findings by materiality: location, demonstrated issue, impact, smallest correction, and blocker or advisory. Consolidate shared causes. A blocker needs material risk or substantial avoidable maintenance cost in scope. Separate facts from inference and optional coverage from required verification gaps. Omit cosmetic preference, tool-enforced noise, and unrelated redesign. A clean review or "not worth changing" is valid.

## Simplification

Simplification is a change in its own right, not a side effect. Look for it in every review: fewer concepts, states, screens, routes, words, lines, and tests, with the model still correct. Cut code and tests that no current behavior needs; a test that proves nothing a public seam cannot prove goes. Prefer conceptual simplification over code volume; apply the conceptual complexity criterion in `QUALITY.md`.

Rate every simplification, and every review of one, on this ladder and state the level:

- Level 0, internal: nothing user-visible, fewer code paths, routes, tests, or developer tooling. Free.
- Level 1, friction: same goal, same path; one click more or less, two screens become one, an extra error in an edge case, under 5% of the journey. Accept.
- Level 2, workaround: a partial feature goes and the goal is still reachable another way. Name the workaround. Accept when it buys simplification.
- Level 3, cut unused: a visible feature with no or minimal use today goes. Accept and record it, unless the feature is planned.
- Level 4, cut used or conceptual: a routinely used feature goes, or the conceptual model changes. User decides.

Unused is not unplanned. Before rating level 3, check `PRODUCT.md`, current plans, and what the user has said; a feature kept for a stated later step stays, and the review names it. Fundamental capabilities and data stay at every level below 4.

When a simplification merges or renames concepts, name the general concept, not today's only instance. One source today does not make "file import" the name for import.

## Fix the findings

For implementation requests, fix in-scope findings and recheck affected behavior under existing authorization. Preserve accepted trade-offs. Report results and material verification gaps; record the applicable E2E decision. Stop after the requested outcome and required evidence are complete rather than starting another broad review cycle.
