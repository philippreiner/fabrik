# Deep review

For a finished feature, data model, permission, or durable-work change, or when
asked: find what makes the change wrong or heavier than it needs to be. Every
proposed fix leaves the system simpler or more correct than the complexity it
adds. Run independently through the `codex` skill, you report only; in the main
loop, you fix what the findings call for.

## Read

1. The brief: the outcome in the user's words, base ref, scope, plan.
2. The diff against the base, then the owners it touches. `PRODUCT.md` for
   intent and words, `AGENTS.md` for the invariants.
3. State the change in one sentence and the model it introduces: entities,
   states, owners, and where each fact lives. A change you cannot state plainly
   is the first finding.

## Look for

- Concept: names and states that differ from what the user said; two concepts
  that are one; a state that cannot happen.
- Implicit state machines: booleans, nullable timestamps, and status strings
  that together encode a lifecycle nobody declared. Name the states, the
  transitions, and the combinations the schema allows but the product never means.
- Slop: implicit coupling, layer-first folders, duplication, representable
  illegal states, god files, shotgun surgery, layering violations, pass-through
  wrappers, errors and validation away from the boundary.
- Architecture: a business decision outside its owning module; more than one
  command for one accepted operation.
- Data model: a fact persisted twice; an invariant held in code that the database
  could hold; missing tenant or permission scope at a server boundary.
- Overbuilding: options, fallbacks, compatibility paths, tests, or docs that no
  current behavior needs. Rate each cut on the Simplification ladder.
- Cost: every alarm, retry, sweep, poll, and reply loop has a stored bound,
  a terminal state, and an index for its queries.
- Speed: sequential database round trips and server calls before render stay
  within the step budget in `docs/architecture.md`.
- Neighbors: features this change can break or quietly degrade (the core loops in
  `PRODUCT.md`); name the regression or the
  check that rules it out.
- Deployment: a clean path from what production holds today; migrations
  drain and existing rows keep working.
- Bugs: only with a concrete trigger and wrong outcome.

## Answer every access question

Answer each with evidence or "not applicable, because":

1. Every new read path for restricted content checks access for the member who asks.
2. Background work acts as the identity that owns the action.
3. Deletion reaches every copy: stored bytes, derived rows, search entries, provider state.
4. A migration that drops or merges data keeps every fact a later step needs.

Done when every owner the diff touches has been checked against each lens, and
every access question has an answer.

## Report

Lead with the verdict in one sentence, then the one bold move a strong staff
engineer would make, then a table ordered by score:

| #   | Finding | Where | Often | Bad | Score | Call |
| --- | ------- | ----- | ----- | --- | ----- | ---- |

Score bugs and risks with the Report rule in `SKILL.md`, including its severity
override. Call each one: fix (meets that policy), list (below it), or ask (a product
decision, a one-way door, or a cut at ladder level 4). A simplification gets
its ladder level in the Score column. One line per finding under the table:
trigger, wrong outcome or maintenance cost, smallest correction. Then one line
per access question. End with what you could not verify. A clean review is valid.
