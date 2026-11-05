---
name: review-change
description: Review a code change on request, or your own behavior or contract change before handover; read it before running the quality gate, which proves none of these rubrics. Owns the rubrics for code shape, data, permissions, performance, tests, and simplification. How a change looks and works for its user is the qa skill.
---

# Review change

This skill owns the review process and the review criteria. `AGENTS.md` owns required checks; `docs/development/quality-loop.md` owns commands and automated gates.

Tie findings to user impact or maintenance cost. Preserve behavior unless the request changes it. The checklist is the baseline, not the ceiling: when code smells wrong, name the conditions that made it so, even when no rule covers them.

## Route the task

- Explicit review: assess and report without editing unless fixes were requested.
- Handover: read behavior, contract, permission, persistence, or workflow changes once against the Checklist, the Concept rubrics, and the Seam rubrics, at a depth proportional to risk. Done when each has been read against the diff; the handover names only the ones that fired. Mechanical, copy, style, and layout edits without those effects need only lint and typecheck of the touched files. A review already done for this diff, by you, the user, another agent, or `/code-review`, counts; after fixes, recheck only the findings.
- Deep review: [deep-review.md](references/deep-review.md), when asked or for a new feature, data model, permission, or durable work. For an independent read, run it through the `codex` skill.
- Whole-repository architectural audit: `/codebase-audit` is the separate user-invoked workflow.

Stay inside the requested scope. Cover every seam the change touches before concluding.

## Establish the evidence

- State the requested outcome and, for bugs, the demonstrated cause. Name an introducing change only with evidence; do not block a proven fix on finding a commit.
- Establish the canonical owner and the neighboring case that must remain valid. Trace added state, types, helpers, policies, and side effects to the outcome, including callers outside the diff.
- For changed state transitions, check repeat, concurrency, and partial failure; local status alone may not prove released resources or available results.
- Ask when a finding needs a scope, permission, contract, or product decision beyond existing authorization.
- Use incident reports as hypotheses. A proposed review rule must reject a known regression and allow a valid implementation; extend an existing criterion where possible.

## Checklist

Walk the priority order, then read only the references for the seams the change touches.

1. Correctness, security, permission, data-loss, or unbounded-cost failure. Usage-billed infrastructure often has no spending cap: every path that runs again without a person (alarm, retry, sweep, poll, reply) needs a stored bound and a terminal state, and every query on such a path needs an index ([durable work](references/data-and-durable-work.md#durable-work))
2. Broken product flow, misleading state, or blocked recovery
3. Hidden contract, lifecycle, or state-model failure
4. Wrong ownership or layer
5. Unnecessary concepts, branches, indirection, or volume, including doc text the diff added without a changed rule
6. Weak type boundaries or true duplication
7. Cosmetic cleanup, skipped while structural issues remain

Concept rubrics, read against every new name, state, control, and table. Lint measures code complexity; conceptual complexity is measured by explaining the change cold, to someone outside the team, in three sentences: the problem, what the user sees, the words it needs. Then:

- A why with two subjects is two changes: split and say so.
- Two concepts that are one, or one name for two: one screen says archive, another says deactivate for the same transition.
- A state the user never named, or one that cannot happen.
- A control whose label promises less or more than its effect: share is not move.
- A fact a person would look for on this object that lives on another.
- A new word missing from the Words in `PRODUCT.md`, or a term that differs from the interface copy or the user's words. Name the general case, not today's only instance.
- A sentence that needs implementation detail to be true, a fact persisted twice, or a business decision outside its owning module.

Seam rubrics, read against every diff that touches the seam. The reference holds the rest.

- Writes: the mutable precondition sits in the write's `WHERE` and the command maps zero `returning` rows to a domain outcome. A precondition that reads other rows has a unique constraint or a row lock and a race test on two connections. No external I/O inside a transaction.
- Data model: every tenant-scoped reference is a composite `(tenant_id, x_id)` foreign key. No caller, no merge: a new table, column, flag, or option has a caller that reaches a user in the same change; a test or seed is not a caller.
- Reads: admit once, then the screen's reads in parallel within the step budget; options load when their control opens. Growing reads are bounded with keyset cursors and select only needed columns. Set-based queries, never awaited calls in loops.
- Server boundary: every server function and route handler validates input and enforces session, tenant, and capability itself; loaders and GET handlers mutate nothing; posted ids are untrusted selectors.
- React: no derived or mirrored state; `useEffect` only to sync with an external system; one discriminated state instead of mode booleans.
- Durable work: external I/O in steps with stable operation ids; every re-arming alarm, sweep, or retry has a stored bound and a terminal state, and its queries have an index.
- Permissions: capabilities come only from account, membership role, and team role; hiding a control is not enforcement; detail and list reads share one predicate.
- Contracts: map rows to product types at the server boundary; one source per shape; a producer fills its type honestly instead of padding.
- Failure: missing, empty, denied, and failed stay distinct; a catch that returns `[]`, `null`, or success erases them. Unexpected errors reach error telemetry.
- Tests: each added test fails for a plausible broken implementation and passes a behavior-preserving refactor; database rules are proved in an integration suite, providers faked at their boundary.

| Seam | Reference |
| --- | --- |
| Failure repair, ownership, volume, conceptual complexity, naming | [code-shape.md](references/code-shape.md) |
| Server boundaries, UI state, fetching, mutations, errors, provider calls | [ui-and-server.md](references/ui-and-server.md) |
| Database writes, data model, migrations, access patterns, durable work | [data-and-durable-work.md](references/data-and-durable-work.md) |
| Types, contracts, product and permission checks | [contracts-and-permissions.md](references/contracts-and-permissions.md) |
| Type design, unions, casts, and narrowing | [typescript.md](references/typescript.md) |
| Latency, round trips, provider calls, batching, caching | [performance.md](references/performance.md) |
| Tests, lint warnings, test seams | [verification.md](references/verification.md) |

## Report

Find issues before scoring them. Rate how often each would happen and how bad it would be, each 1–10; fix at a product of 15 or more, and list the rest with both scores. Credible security, tenant-isolation, data-loss, unbounded-cost, or blocked-recovery defects require resolution regardless of frequency. For review-only requests, report without editing. Report findings by severity, then score: location, demonstrated issue, impact, smallest correction. Every finding names the trigger and wrong outcome, or maintenance cost; an unproven claim is not a finding. Do not add guards against states the types, constraints, or callers exclude. Prefer corrections whose complexity fits the risk. Consolidate shared causes. Missing tests alone are advisory unless a required gate fails or material risk remains unproven. Separate facts from inference. Omit cosmetic preference, tool-enforced noise, and unrelated redesign. A clean review is valid.

## Simplification

Look for simplification in every review: fewer concepts, states, screens, routes, words, lines, and tests, with the model still correct. Cut code and tests that no current behavior needs. Prefer conceptual simplification over code volume.

Rate every simplification, and every review of one, on this ladder:

- Level 0, internal: nothing user-visible, fewer code paths, routes, tests, or developer tooling. Free.
- Level 1, friction: same goal, same path; one click more or less, two screens become one, an extra error in an edge case, under 5% of the journey. Accept.
- Level 2, workaround: a partial feature goes and the goal is still reachable another way. Name the workaround. Accept when it buys simplification.
- Level 3, cut unused: a visible feature with no or minimal use today goes. Accept and record it, unless the feature is planned.
- Level 4, cut used or conceptual: a routinely used feature goes, or the conceptual model changes. User decides.

Before rating level 3, check `PRODUCT.md`, `docs/plans/`, and the current request for a concrete use. Preserve capabilities needed by that work and name the dependency. Fundamental capabilities and data stay at every level below 4.

When a simplification merges or renames concepts, name the general concept, not today's only instance. One channel today does not make "web message" the name for a message.

## Fix the findings

For implementation requests, fix in-scope findings and recheck affected behavior under existing authorization. Treat each finding as a claim: accept it when its trigger and outcome hold in the code, and reject it in one line when they do not. Never add defensive code only to settle a finding. Preserve accepted trade-offs. Report results and material verification gaps. Stop after the requested outcome and required evidence are complete rather than starting another broad review cycle.

A good fix makes the model easier to understand without losing necessary distinctions. It may need more states or lines to make contracts and boundaries explicit.

Review in the main loop with this skill; an independent read runs through the `codex` skill. A follow-up the user specified after a review does not reopen independent review unless it changes permissions, migrations, or durable work.
