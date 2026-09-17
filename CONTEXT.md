# [Project name] context

This is the short map of the domain, codebase, and terms agents need to work safely. Keep it factual and current. Put durable decisions in architecture docs or ADRs, not here.

## Read for the task

Start with the section relevant to the requested change:

- Product behavior and principles: `PRODUCT.md`
- UI rules and component boundaries: `DESIGN.md`
- Review criteria and required evidence: `QUALITY.md`
- Architecture and durable decisions: `docs/architecture.md` and `docs/adr/`

Example: “For an access change, read the glossary entry for Membership, the authorization owner, and the permission tests before editing a route.”

## Codebase map

| Area | Owns | Read first |
| --- | --- | --- |
| `[path or package]` | `[business or technical responsibility]` | `[entry point or module]` |
| `[path or package]` | `[business or technical responsibility]` | `[entry point or module]` |

Example:

| `src/billing` | invoices, charges, and settlement state | `src/billing/charge.ts` |

Describe ownership, not every file. Call out boundaries where callers must use a public contract rather than reaching into implementation details.

## Glossary

Use one name for each concept. Define what it is, who owns it, and what it is not when confusion is likely.

| Term | Meaning | Not |
| --- | --- | --- |
| `[Term]` | `[plain-language definition]` | `[nearest misleading concept]` |
| `[Term]` | `[plain-language definition]` | `[nearest misleading concept]` |

Example:

| Invoice | A durable request for payment with an owner, amount, and lifecycle. | A payment, which is the settled transfer of funds. |

## Lifecycle and invariants

Record facts that constrain behavior across modules:

- States: `[state] -> [state] -> [state]`
- Terminal states: `[states that cannot progress]`
- Repeat behavior: `[what happens when the same request arrives again]`
- Partial failure: `[what is durable, retryable, or visible after a failure]`
- Authorization: `[where identity, tenant, and permission are re-derived]`
- External effects: `[what is sent, when, and how it is reconciled]`

Example: “A submitted export can be retried by its owner. The request is durable before the job starts, and a failed job never appears as complete.”

## Persistence conventions

State what is stored once and what is derived:

- Source of truth: `[store or external owner]`
- Durable facts: `[facts that must be persisted]`
- Derived values: `[values calculated at read time or by a named process]`
- Relationship constraints: `[foreign keys, uniqueness, or other invariants]`
- Claim or lease rules: `[how concurrent work is coordinated]`

Example: “The database stores the approved amount once. Remaining balance is derived from settled payments; it is not a second editable field.”
