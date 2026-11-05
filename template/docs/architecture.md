# Architecture

[Product] is [shape: modular monolith, services, ...]. [Framework] is the shell, [domain module] owns product behavior, and [database] is product truth. This page holds the boundaries, invariants, and decisions that code does not explain. They are defaults with reasons: when a better design beats one, propose it and name what it replaces.

## Ownership

| Path | Responsibility |
| --- | --- |
| `[app]` | Routes, server functions, and UI composition |
| `[domain package]` | Product policy, commands, queries, and lifecycle transitions |
| `[database package]` | Schema, migrations, client and units of work, persisted types |
| `[workflow package]` | Durable coordination; steps perform external I/O |

## Dependency direction

- Apps depend on packages; packages never depend on apps.
- [Which package may import which, and the check that enforces it.]

## Request path

[The step budget per screen: how many sequential database steps a detail, list, and search read may take before render, and how to measure it.]

## Tenancy and authorization

[The access model: where identity, tenant, and capability come from, and where they are re-derived.]

## Database rules

[Units of work, write rules, constraints the database owns.]

## Durable work

[The engine, the step rules, and how every repeating path is bounded.]

## Decisions

Each line states a boundary, the reason that still holds, and what would reopen it. Git and pull requests hold the history.

- **[Decision].** Why: [reason that still holds]. Reopen: [the fact that would change it].
