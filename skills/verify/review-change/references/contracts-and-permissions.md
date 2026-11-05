# Contracts and permissions

## Types And Contracts

- Let the backend own product data contracts. Frontend code consumes those contracts and exposes violations instead of hiding them with fallbacks.
- Keep one source of truth for each shape and derive types from Zod when the schema exists.
- Prefer `satisfies` over `as` and keep top-level signatures explicit when control flow branches.
- Every producer must fill its type honestly. Split a narrower type when a producer cannot compute a field instead of padding with `0`, `null`, or `""`.
- Boundary validation should produce the type internal consumers need. Repeated casts, parsing, or null checks for facts already guaranteed within that trust boundary indicate a contract to repair; retain checks at new boundaries and for mutable state.
- Map stored rows to deliberate product types at the server boundary. Never return ORM row types from server functions or server routes.
- Define a persisted cross-package key, R2 path, or binding name once in a shared contract; mocks on both sides cannot catch drift.

## Product And Permission Checks

The database is the single source of permission facts
([docs/architecture.md](../../../../docs/architecture.md)), and platform
admin stays out of tenant authorization.

- Derive capabilities only from the access model in `docs/architecture.md`, for example an active account, an active membership with its role, and a role on an active team. Do not invent grants or restrictions from sender addresses, conversation participation, creator attribution, or workflow history. These facts change independently of authority; using them as permission makes access unpredictable and adds competing policies.
- Suspended membership authorizes nothing. Platform-admin status does not replace membership for tenant work.
- Keep place, permission, and consent separate. A verified channel identity sets a sender kind; it grants no access. Being a participant entitles an address to outbound replies, not to reading the inbox.
- A proposed new source of authority or exception needs a concrete user requirement, an explanation of why the existing role and assignment model cannot express it, and an explicit product decision recorded in `docs/architecture.md`. Implementation convenience is not a reason. Review both grants and denials against the same model at UI, server, and background boundaries.
- Gate views with the right capability and enforce writes on the server. Gate sensitive reads, edits, admin controls, and destructive actions separately. Hiding a control does not enforce permission.
- Enforce membership, account state, tenant scope, and object capability at every server function, server route, and background boundary; route guards are defense in depth.
- Prefer capabilities for enforcement; use raw roles only when role administration is the feature.
- Domain policy modules own object capability checks. Detail and list reads share authorization predicates and actor context; each surface may further restrict what belongs there.
- When ownership, assignment, or lifecycle changes, trace listings, detail links, background readers, and deletion checks. Each must use the current authority and distinguish active dependencies from historical links. Removing an assignment revokes access; it does not delete history.
- Show states with different consequences or remedies distinctly. A failed mutation must leave a visible error and recovery action; success feedback must follow the server result.
- Tie access grants to the intended identity and expose them only after the grant completes.
- Give each form label one labelable control and keep unrelated interactive elements outside labels.
- Make the next step clear after create, edit, archive, delete, retry, and handoff.
- State the consequence before an irreversible action. Do not make users assemble the workflow through settings and options.
