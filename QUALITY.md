# Quality review guidelines

Use this checklist for code and contract review. Start with correctness, security, product behavior, ownership, and maintainability. Review behavior and module shape, not only diff hunks.

Replace bracketed examples with project-specific owners and commands. This is a baseline, not a ceiling.

## Scope and evidence

- State the requested outcome and, for bugs, the demonstrated cause.
- Trace added state, types, helpers, policies, and side effects to that outcome.
- Name the canonical owner for each decision and boundary.
- Distinguish verified behavior, inference, and unresolved evidence.

Example: “The route now derives the account from the session; it no longer trusts an account ID from form input.”

## Review priority

1. Correctness, security, permission, or data-loss failure
2. Broken product flow, misleading state, or blocked recovery
3. Hidden contract, lifecycle, or state-model failure
4. Wrong ownership or layer
5. Unnecessary concepts, branches, indirection, or volume
6. Weak type boundaries or true duplication
7. Cosmetic cleanup

## Failure and change

- Trace the conditions that produce the demonstrated failure and correct the broken invariant.
- Size a change by the failure paths it opens, including rarer paths with higher impact.
- Repair the contract, not the last link. Catch-alls and post-hoc retries around a wrong model add coupling and hide failures.
- Define success, failure, and unknown at the boundary in types, tests, and docs.

## Code shape and ownership

- Prefer the smallest sufficient diff, the nearest established pattern, and standard platform facilities.
- Keep business policy in its owning module. Routes, views, and handlers consume decisions rather than reconstructing them from raw fields.
- Validate untrusted input at boundaries and preserve explicit types inward.
- Enforce authorization at every server and background boundary.
- Store each independent fact once and derive the rest.
- Keep wrappers that own policy, translation, boundary protection, or lifecycle coordination. Remove wrappers that add no meaning.
- Keep the main flow top-down. Split files when mixed lifecycles or concerns make state implicit.
- Defaults and fallbacks must have a contract meaning. Preserve the distinction between missing, empty, denied, and failed.

Example: “A failed upload must remain failed or retryable; returning an empty list would erase the failure.”

## State, UI, and effects

- Keep server state, URL state, and local UI state separate.
- Do not store derived data in state or mirror props into state.
- Use effects only to synchronize with an external system.
- Replace booleans that describe one mode with a discriminated state.
- Route loading, empty, error, partial, and complete states through the owning surface.
- Keep labels, actions, and confirmation text consistent with the state transition.

## Data, mutations, and errors

- Validate on the server and revalidate intentionally after writes.
- Re-derive identity, account, tenant, and permission at the mutation boundary.
- Make durable work idempotent and define recovery after partial failure.
- Emit operational telemetry for asynchronous failures; do not hide them in generic logs.
- Keep pagination and polling order stable and unique.
- Preserve distinct failure causes instead of converting them all to success, empty, or retry.

## Complexity and volume

- Ask whether each new concept, branch, helper, configuration flag, fixture, and test is needed by current behavior.
- Prefer one owner and one vocabulary for shared semantics.
- Do not add generic registries, factories, providers, or compatibility paths without a demonstrated need.
- Remove obsolete code and tests within scope after checking what protection they provide.

## Types and contracts

- Encode exclusive choices in types.
- Keep public interfaces small and test through them.
- Do not widen types or use `any` to hide a broken contract.
- Keep validation and normalization at the boundary that owns them.
- Document only the invariants that code cannot make obvious.

## Product and permission checks

- Check the user's visible path, expected outcome, and recovery path.
- Preserve tenant or account isolation and least privilege.
- Separate place, permission, and consent; do not infer one from another.
- Make destructive actions explicit and proportional to irreversibility.

Example: “Displaying a record in a shared list does not grant access to its private attachment.”

## Verification

- Run relevant existing tests first.
- Add permanent coverage when current tests cannot prove changed behavior or an important failure path.
- Assert outcomes at public seams; use call assertions only for external-interaction contracts.
- Use browser or end-to-end checks when lower-level tests cannot prove the user journey.
- Report checks that could not run and why.

Suggested project commands:

```text
[install or setup command]
[focused test command]
[lint/typecheck command]
[full quality command]
```

## Done

- The requested outcome is implemented.
- Affected docs and change records are updated.
- The diff contains no unrelated cleanup.
- Verification evidence and limitations are recorded.
- A fresh reader can identify the owner, contract, and recovery behavior.
