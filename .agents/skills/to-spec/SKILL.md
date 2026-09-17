---
name: to-spec
description: "Write a clear implementation spec for substantial decided work: domain model, acceptance scenarios, contracts, and coarse steps. Small changes go directly to implementation."
---

# To Spec

Give the user and executor a clear picture of the intended system before implementation. Resolve the model here; keep execution mechanics in `implement-spec` and delegation policy in `AGENTS.md`.

Read the relevant code and sources before drafting. Use current ownership and repository terms. Research only what is needed to settle the proposed change; do not turn the spec into a research queue or a list of human tasks.

Make routine technical decisions and record material assumptions. Ask only when different answers would change the intended outcome, permission boundary, or data safety. Draft everything independent of that answer and give a recommendation with the consequence. Unknown production data matters when choosing compatibility or migration behavior, not when deciding whether the work is substantial.

## The spec

Write `plans/<topic>/README.md` with these parts, sized to the change:

1. **Intent and boundaries.** Requested outcome, non-goals, accepted trade-offs, and expected scope. Describe the final system; omit conversation history.
2. **Model and ownership.** Entities, relationships, identity, durable facts, invariants, states, and transitions. Name the owning modules and where truth lives. For changed transitions, explain repeat, concurrency, and partial failure. Show the proposed data shape when it settles ambiguity.
3. **Acceptance scenarios.** A few concrete user or caller actions and observable outcomes, including the important failure or permission case. Reuse existing tests where they prove these outcomes; follow `AGENTS.md` for new coverage. A scenario is not automatically a new test file.
4. **Contracts.** Changed interfaces, permissions, persistence, and external effects. Include migration requirements only where production data or live readers require them. For UI, name the existing page pattern and changed states. Link supporting docs rather than copying them.
5. **Coarse implementation steps.** Put the defining model or shared seam first, then dependent consumers and integration. Each step names its outcome, owner, and sufficient verification. Merge steps that share a model and acceptance evidence. Add separate step files only when they make execution easier to hand off.

Keep steps implementable. Resolve research during planning; record a remaining user-only decision or verification limitation explicitly rather than inventing staged approval gates. Do not add compatibility for intermediate states that will never ship. Distinguish assumptions from accepted decisions.

Before presenting, take one secondary review of the model and scenarios for unnecessary complexity, missing outcomes, and repeat or partial-failure errors; correct the spec once.

Deliver the written spec with a short summary of the key decisions and any open question. Approval authorizes `implement-spec` to execute it; writing the spec itself needs no separate approval. If the user already authorized execution after planning, continue under that authorization.
