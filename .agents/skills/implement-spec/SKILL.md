---
name: implement-spec
description: "Implement an approved spec under plans/ through integration and verification."
---

# Implement Spec

Deliver the approved outcome end to end. The README owns intent, model, scenarios, and contracts. `AGENTS.md` owns delegation and testing; the agent files own model selection. Read existing step state and relevant handoffs so completed work stays completed.

## Execute

1. Establish the next open outcome. Read the defining code yourself and implement the critical model or shared seam before delegating dependent work. Follow the spec's contracts; adjust routine file placement and sequencing when the code supports a clearer shape.
2. Work directly or dispatch a bounded step using the worker brief in `AGENTS.md`. Include the spec and step paths, settled contracts, and new evidence. Continue useful independent work while the worker runs. Reuse an informed worker for adjacent work or corrections.
3. Read each handoff's diff and key files. Verify ownership, scope, contracts, and acceptance evidence. Correct the cause of an error before propagating the pattern to more consumers. If a fix fails twice, re-derive the diagnosis.
4. Keep lightweight progress in the spec. Write a `changes/<NN>-<summary>.md` handoff only when another executor needs durable context: outcome, changed paths, verification, deviations, and unresolved evidence. Do not repeat the README or create a diary for direct work.
5. Verify the integrated scenarios, update affected docs per the `documentation` skill and the worktree change record, run required checks, and perform one final `quality` review. Fix material findings and recheck affected behavior. Stop when the requested outcome and required evidence are complete; do not start another broad cleanup or review cycle.

Implement the final shape. Add no migrations, compatibility paths, or tests for intermediate states that never ship. Preserve accepted trade-offs. A newly discovered issue needs user input only if resolving it changes scope, product behavior beyond the request, or a safety boundary; continue independent work meanwhile.

If only the user can supply evidence, prepare the exact scenario and report what remains unverified. Honor a user-test gate already approved in the spec, but do not invent new gates or treat missing evidence as a pass.

The final response states the outcome, material deviations, verification and limitations, and branch diff volume. The lead owns completion; worker reports alone do not prove integration.
