# Data and durable work

`docs/architecture.md` states the database, units of work, write rules, and
durable-work owner.

## Writes

- Put mutable preconditions in the write's `WHERE` clause or subquery and inspect `returning`. A read followed by a write is not atomic. Check last-owner protection, one-time acceptance, and never-reuse identifiers at this seam.
- Every guarded write reads its result (`returning` or the row count) and maps zero rows to a domain outcome. A command that ignores it reports false success.
- Writes that must commit together run in one short transaction. Never catch a failed statement inside it and continue. No external I/O inside; commit, then reconcile.
- Writes run concurrently. A precondition that reads other rows (`insert ... where not exists`, counting owners, one default) needs a unique constraint or a row lock taken first (`for update` on the parent), and a race test on two connections. Queue-like claims use `for update skip locked` in the statement that records the claim.
- Use stored fences where work runs outside a transaction (ownership versions, claim tokens, leases).
- Compensation calls the same writer as the forward path, never a copied implementation.

## Data Model

Start with entities, relationships, cardinality, and lifecycle. Prefer ordinary
tables, foreign keys, and constraints. Reuse an existing model when its identity,
ownership, and lifecycle fit; generalize only for current requirements.

- Every reference into a tenant table is a composite `(tenant_id, x_id)` foreign key, so the database refuses a cross-tenant link. Membership and capability predicates agree between detail reads, lists, and writes.
- Persist each domain fact once under a clear owner; derive display states and eligibility from those facts. A comparison key is a generated column, not a second write. Denormalization needs a measured read path and one synchronization owner.
- Reads that decide whether a unique slot is occupied must match the constraint's scope and predicate; the database still arbitrates concurrent writes.
- Use check constraints for closed durable states and shapes, and runtime validation for extensible registries.
- A child inherits ownership from one owning parent. A collection, view, or read projection that lists content is not its owner: it grants no access, and its deletion removes no content.
- Keep queryable identity, ownership, lifecycle, and relationships relational. Use JSON for provider envelopes, immutable snapshots, and variable configuration. Use `archivedAt` for reversible removal and `status` only for a real state machine.
- Verify deletion and replacement settle dependent rows and preserve independently owned data. An unstarted or failed process does not prove a container is empty.

## Migrations

- History on main is append-only; never squash or edit it there. Review the complete pending set as one deployment unit, including generated SQL and snapshots.
- Verify fresh installation and the upgrade path for existing data.
- Establish whether production has affected data before choosing compatibility, backfill, or rolling deployment. Persisted configuration changes need the same assessment, even without DDL. Replace unshipped contracts in place.
- Local checks do not authorize remote migration commands or prove a populated production migration is safe.

## Access Patterns

- Use the narrowest existing query or permission primitive for the target object. Do not fetch an inventory and filter it in the route.
- Bound growing reads and writes. Select only needed columns, keep bodies and JSON payloads out of lists, and use keyset cursors on a stable unique order instead of `OFFSET`.
- Index actual filters, joins, and ordering, including reverse foreign-key traversal. A sweep that reads open rows uses a partial index on the status it reads. Do not add an index covered by another index's leading columns.
- Prefer set-based queries and multi-row writes over awaited calls in loops.
- Use `exists` for existence and `count(*)` only when the number is required.
- Terminal writers must settle every field their read model filters on.

## Durable Work

The database owns product state; the workflow engine owns execution.

- Put external I/O in steps. Starts and steps may repeat: use stable operation identities and idempotent effects, and account for an effect succeeding before its checkpoint is persisted. Recheck mutable authorization at the effect that depends on it.
- A committed mutation followed by failed workflow creation needs recorded failure or retry intent where the product depends on completion.
- Pass identifiers, versions, and non-sensitive decisions into durable execution. Resolve current credentials in steps and keep secrets and raw customer payloads out of persisted step results and telemetry.
- Define terminal outcomes for denial, deletion, cancellation, exhausted retries, and missing targets. Fence claimed work with its generation wherever an old attempt could overwrite newer state. A runtime error must not leave product status indefinitely running.
- Keep retryable provider errors distinct from permanent rejection. Bound external calls with timeouts and use durable sleeps for waits.
- The database and object storage share no transaction. Order the writes so partial failure leaves an orphan object, not a row pointing at nothing, and name the cleanup that settles it.

Bounded execution: usage-billed infrastructure bills every wake, step, and request, often with no spending cap, so a loop runs until someone deploys a fix. Every path that triggers itself again needs a bound that survives eviction, redeploy, and a throwing handler.

- Alarms and timers re-arm only behind a stored attempt count or a terminal state, with backoff to a ceiling.
- A row a sweep re-dispatches carries an expiry, an attempt cap, or a budget in the database, and each tick has a `limit`. A row that fails forever reaches a terminal state.
- Every sweep query and per-request lookup has a matching index (`EXPLAIN` shows an index condition, not a sequential scan).
- Work started by inbound mail, webhooks, or provider notifications has a per-subject rate cap, so a remote system that answers us cannot keep it running.
- One trigger starts a bounded number of instances; user-sized collections are walked in capped steps.
- Client polling sends nothing from a hidden tab and stops on a terminal state.

When a bound is missing, name the trigger, the cadence, and the cost per day it allows.
