---
name: codebase-audit
description: Audit the whole repository for architectural debt and needless complexity. Run from time to time with a large model. Returns one ranked list of simplifications.
disable-model-invocation: true
---

# Codebase Audit

Simplify the codebase. Ask: if we started over today with the same goal, what would we still keep? Think from first principles or similar solutions. Do not assume the current design is right. Complexity is fine where the problem is complex. Where the code is more complicated than the problem, cut there. Optimize the whole system, not one file or one test. Existing docs, decisions, and plans can be wrong; treat them as hints, not rules. Balance that we have foundations for future features but also bad past decision in the code. Explore broadly and use engineering judgment. 

Do not edit code; save the report only after user confirmation.

## Method

1. Map the subsystems: what each owns, its tables, states, entry points, and approximate lines of code.
2. Hunt for complexity by reading the key files yourself, with the lenses below. Decide first if a thing needs to exist, then if it can be simpler. When you find a bad pattern, check related or similar subsystems for it too.
3. Present a short overview of the map and candidate cuts, noting which areas you inspected deeply and which you only surveyed. Ground each cut in a concrete code example and a brief explanation of why the simpler shape works. Merge symptoms that share a root cause.
4. Discuss and refine with the user. Investigate further where it helps resolve a question or tradeoff.
5. Present the final ranked list in chat. Wait for the user to confirm it before writing a single report file under `docs/plans/`.

## Exploring

Use `explorer` agents for the map, at most three at once; for judging a large subsystem, brief `oracle` or a `codex` second opinion read-only. Preserve tokens and context. Workers do not spawn workers. They return observations, candidate cuts, and the code evidence behind their reasoning.

Treat worker conclusions as hypotheses. Read the decisive code yourself before including a finding. You own the reasoning and the final recommendations.

## Lenses

Use but do not limit yourself to these review dimensions:

- Implicit state machines: find all of them. Booleans, nullable timestamps, and status strings that together encode a lifecycle nobody declared; name the states and the illegal combinations the schema allows.
- Slop: implicit coupling, layer-first folders, duplication, representable illegal states, god files, shotgun surgery, layering violations, pass-through wrappers, errors and validation away from the boundary.

- Database: plain names, invariants in the database, each fact stored once, derived keys as generated columns, no invalid states the schema allows, no half-done migrations.
- Domain model: one name per concept, one concept per name, across code, schema, UI, and docs.
- Lifecycle: real states and transitions, boolean soup, impossible states, missing unhappy paths.
- Permissions: server-enforced, tenant isolation, no scattered guards.
- Consistency: same folder layout, file naming, and patterns for the same job. One way to fetch, mutate, check permissions, handle errors, build forms, and run workflows. Domain nouns for folders, no `utils`, `helpers`, `service`, `manager`.
- Wrappers: functions that only call another function, layers without meaning, adapters and factories with one implementation.
- Speculative code: options, flags, parameters, generics for a future that is not here. YAGNI. Prefer the one-liner.
- Over-defense: guards for states the model cannot produce, generic catches, errors turned into fake success, validation repeated at every layer.
- Coupling: how many files move for one ordinary change. Hubs imported everywhere.
- Readability: long names, comments that repeat the code, control flow that hides the simple case.
- Dead code: unreachable branches, unused exports, stale flags, obsolete compatibility paths.
- Test value: tests that restate the implementation, mock-only tests, call assertions that restate wiring, tests for removed behavior.
- Test gaps: missing permission failures, repeats, concurrency, partial failure at seams that carry real risk.
- Boring standard: custom code where the framework, a library, or the platform already does the job.
- Performance: sequential database steps and server calls per navigation, reloads after a write, third-party calls on the request path, cold-start weight, cache headers, slow queries, N+1. Measure the deployed site first ([verification](../review-change/references/verification.md)). Complexity added for speed without a measurement is a finding.

## Report

Start with the short subsystem overview. Rank findings by what disappears across the system: concepts, layers, branches, and lines of code. Name the potential regressions. Each item: location and brief evidence, the cut, what goes away (including estimated net lines of code where useful), what we lose, and what the change touches. Keep each short. Bugs found on the way go in a separate list in the same report, each scored by the `review-change` Report rule (often × bad). If the code is already good, say so. The audit can return nothing.
