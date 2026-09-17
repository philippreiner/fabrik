---
name: vernunft
description: Assess surprising or complex designs against user expectations and established solutions.
---

# Vernunft

For an assessment, report the smallest justified correction. Apply changes only when the user requested implementation. Stay inside the requested scope.

Apply the principle of least astonishment: behavior should match what its surface
suggests. Compare the design with established solutions and the affected person's
expectations. A deviation needs a concrete requirement or constraint.

## Method

1. **Name the person and expectation.** Use their role, permissions, and visible facts. For internal architecture, consider the downstream caller or maintainer. State what comparable systems would lead them to expect.
2. **Trace material surprises to their cause.** Check which requirement, observed behavior, permission need, or measured limit justifies the deviation. Speculation and effort already spent are not evidence.
3. **Recommend the smallest justified correction.** Reuse the nearest suitable pattern and fix the owning model. Before removing an oddity, investigate why it exists; missing documentation does not prove it is unnecessary. Preserve protections and make required differences understandable.

## The straight-face test

The principle of least astonishment, spoken out loud. Say the result to the person in one sentence: "You see X because Y." "We store this twice because Y."

If you cannot say it with a straight face, if it leans on hidden implementation details, or if it needs a long defense, go back. Short form: would this person be surprised by what is hidden, renamed, duplicated, or silently dropped?

For a substantial independent assessment, follow `AGENTS.md` delegation policy. Give the reviewer the artifact and decision context without prescribing the verdict.

## Patterns to catch

Common ways systems surprise people, named so you can spot and cite them.

- **Whole picture.** If the person would look for it on this object, it is here. A record shows the relevant people and state, not only the subset easiest for the implementation to load.
- **Plain names.** The known name for the known concept, in the words people say, with one vocabulary across the product. If one screen says "archive," no other screen says "deactivate" for the same transition.
- **One thing, one record.** Resolve identity before creating a record; say "unmatched" rather than invent a duplicate. The same action from two paths produces the same record.
- **Single source of truth.** Store each fact once. A copy, cache, or second system needs an operational job the source cannot do. Name the job or remove the copy.
- **The label contract.** A control does exactly what its label says: the full effect and nothing more. Share is not move. One control answers one question. After the action, the new state is immediately visible.
- **No action at a distance.** Acting on one thing never silently alters another. A side effect is visible immediately or declared as a deferred job.
- **Readable cold.** A first-time reader can tell what things are, what state they hold, and what a control will do. Defaults match what this role routinely chooses, and the system never asks for what it already knows.
- **One-way doors.** Friction scales with irreversibility. A reversible action needs zero confirmation. An irreversible action demands explicit friction and names exactly what will be destroyed. When two designs tie, pick the reversible one.
- **Fail loudly.** Show what broke, not the machinery. Distinct causes keep distinct names; failed is not skipped. A state that cannot progress must not claim it is working. Never guess past broken data; stop and name the broken constraint.
- **Three separate facts.** Place, permission, and consent. Where something appears, who may access it, and who agreed to that are three separate facts. A page does not grant access, a move does not revoke it, and found data is not consent.

## Guardrail

Vernunft rewards the expected solution, not naive simplicity:

- Separate facts stay separate, even when one page shows them together. An invitation, participation, and access to an artifact are three facts. Only an explicit product rule may merge facts; never infer the merge.
- Expected is not familiar (Hickey: simple is not easy). A familiar shortcut that entangles two concepts fails; an unfamiliar, untangled design can pass. Judge the tangle, not the habit.
- Do not explain away a surprise. A tooltip, warning, or longer README does not fix a confusing design. Redesign it.
- Boring is not flimsy. The expected solution still gets full engineering: correctness, integrity, completeness.
- Judge the whole, not the part. Ten reasonable local patches can sum to an unreasonable system. Fix where the invariant lives.
