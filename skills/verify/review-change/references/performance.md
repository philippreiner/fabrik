# Performance

Read the hot path before you measure, then measure before you fix. Count each item on the path the user waits for; a finding names the count and what it costs in latency or load. `docs/architecture.md` owns the step budget per screen.

- Sequential: awaits, queries, or provider calls that do not depend on each other run in parallel. A loader or server function waits for nothing it does not render.
- Concurrency: a fan-out has a bound, and the bound names its trade-off: the connection pool, a provider rate limit, durable step count, memory.
- I/O calls: one query per row, one provider call per item, or a second read of what the request already holds become one batched call. Count round trips per request, per durable step, and per model call.
- Passes: data walked twice to filter, map, and count is walked once; the database filters, sorts, and aggregates before rows reach TypeScript.
- Batches: a batch has a size bound and a reason for it. A batch that holds the user's first result back streams instead, or pages.
- Waiting: work that does not depend on a slow await starts before it, not after.
- Early exit: a loop, query, or model call stops once the answer is known: `LIMIT`, `EXISTS`, a found item, a decided gate.
- Data shape: a lookup inside a loop uses a `Map` or `Set` built once; a large result is not copied into intermediate arrays or objects it never needs.
- Freshness: a cache or stale window names the read it saves and how late a teammate's change may show.
