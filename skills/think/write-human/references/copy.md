# Product copy and microcopy

Every word is a design decision. A button label shapes behavior. A headline sets expectations. An error message builds or breaks trust.

Readers are competent professionals. They are busy, skeptical, and judge in seconds. Respect that.

## Before writing

Build context yourself. Don't interview, investigate. When working in the vault:

- `03-reference/Glossary.md` holds the canonical terms. Use them exactly and never invent synonyms.
- Product and feature notes under `03-reference/` (and `04-output/` for research drafts) say what exists, what it's called, and how it's described.
- Real user language lives in `02-notes/<year>/`, `03-reference/meetings/`, `03-reference/sources/` and transcripts.

Understand what the user is trying to achieve. If there is no input to work from, stop and ask one short question.

## Philosophy

**Language is the product.** How you name things shapes how people think about them. A rename changes behavior. A vague label creates support tickets. Terminology is architecture.

**Clarity is respect.** If the reader has to guess, you failed. Vagueness is not sophistication.

**Restraint is the craft.** The best writing is shaped by what gets cut. If a sentence works without an adjective, remove the adjective.

**Consistency compounds.** One label is a pattern. A tone choice in one error message sets expectations for every error message. Think in systems, not instances.

**Honesty over persuasion.** European readers smell hype instantly. Understatement earns trust. Let the product speak.

**Convention over invention.** Borrow from what billions of people already know before teaching something new. If Excel, iOS or Google solved the interaction, study how they write about it.

## Process

1. **Understand the situation before touching words.** Who reads this, where are they, what just happened, what should happen next?
2. **Use the reader's language.** Not your internal model or your excitement about the feature. Start with the glossary and real user phrasing.
3. **Write for the worst moment first.** The empty state, the error, the confusion. A technician in a loud factory on a phone. If it works there, it works everywhere.
4. **One idea per unit.** One headline, one idea. One section, one argument. One error message, one problem plus one action.
5. **Know what you're trading.** Shorter loses nuance. Friendlier loses authority. Specific loses breadth. Make the trade-off on purpose.
6. **Rewrite until it feels inevitable.** First drafts capture intent. Rewrites create clarity.

## Rules

- Simple over complex. "Use", not "utilize". "Help", not "facilitate".
- Specific over vague. No "streamline", "optimize", "innovative", "seamless" (see `vocabulary.md`).
- Active over passive. "We generate reports", not "Reports are generated".
- Confident over qualified. Cut "almost", "very", "really", "just".
- Show over tell. Describe the outcome, not the adjective.
- Honest over sensational. Never fabricate numbers, customers or quotes.
- Transitions must advance the argument. If removing one doesn't break the flow, it wasn't needed. Alternatives are in `transitions.md`.
- Consistent over creative. Same concept, same word, everywhere.

## Microcopy

Small text at decision points: labels, tooltips, empty states, confirmations, errors, placeholders. Often more important than headlines because it appears when people need guidance most.

- Say what happened, then what to do. Not "Error" but "Couldn't save. Check your connection and try again."
- Use the user's verb. If they clicked "Delete", confirm with "Delete", not "Remove" or "Confirm action".
- Front-load the useful word. "3 assets selected", not "You have selected 3 assets".
- Buttons name their action. "Save changes", not "Submit". "Add technician", not "OK".
- Placeholders show a format or example. "e.g. Pump-A-3201", not "Search...".
- Tooltips are one sentence. If one needs more, the UI needs a redesign.
- Empty states say what belongs here and offer one action to start.
- Success confirms briefly, then gets out of the way. "Asset created."
- Sentence case for buttons and labels.

## Tone

Calm, not excited. No exclamation points. No manufactured urgency.
Direct, not blunt. Precision without coldness.
Confident, not arrogant. Say it plainly and back it up.
Human, not cute. Personality yes; cleverness at the expense of clarity, never.

Adjust intensity by context (headlines bolder, body copy clearer, microcopy quieter) but keep the same personality. For German audiences see `multilingual.md`.

## European context

- No manufactured urgency or artificial scarcity. It reads as manipulation.
- Privacy language is a trust signal, not only a legal requirement.
- Directness is valued, precision is expected, fluff is punished.
- Metric units, European date formats and local conventions by default.

## Quality check

- [ ] Terms match `03-reference/Glossary.md` exactly
- [ ] Makes sense to someone who has never seen this product
- [ ] Works at the worst moment: error, empty, confused, mobile
- [ ] Every word earns its place
- [ ] No buzzwords without substance
- [ ] No passive voice hiding who does what
- [ ] No exclamation points
- [ ] P0 and P1 checks from `SKILL.md` pass (profile `product-copy` or `ui-copy`)

## Output

- Give the text organized by where it lives (screen, section, component).
- Annotate key choices: why this word, why this structure.
- Offer 2–3 alternatives for headlines and CTAs, each with a one-line rationale.
- Flag any glossary conflicts in existing copy.

Headline formulas, CTA patterns and page structures are in `copy-structures.md`.
