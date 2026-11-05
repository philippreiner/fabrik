---
name: write-human
description: Write, rewrite, edit or audit any text so it reads like a sharp human wrote it. Covers removing AI writing patterns (flag AI tells or rewrite), long-form essays, memos and position pieces in the scientist's-memo style, and user-facing copy such as landing pages, headlines, CTAs, emails, product descriptions, UI microcopy, documentation and PRDs. Use when asked to make writing less AI-like or more human, audit text for machine-generated patterns, write or expand an essay or memo, or write or improve any user-facing text, in English, German or other languages.
---

# Write human

Every piece of text that leaves this skill should be indistinguishable from the work of a sharp, opinionated human writer: warm, specific, direct, with as little prose and jargon as the job allows. The tone matches the user and the intent of the piece.

## Pick the job, then load its references

Read only the references the job needs. All paths are relative to this skill's folder.

| Job | Mode | Read |
|---|---|---|
| Flag AI tells without changing the text ("detect", "flag only", "audit only", "scan", "what AI patterns are in this") | `detect` | `references/ai-patterns.md`, `references/vocabulary.md` |
| Fix existing text (the default when text is pasted with no other instruction) | `rewrite` | `references/ai-patterns.md`, `references/vocabulary.md` |
| Write or expand an essay, memo, position paper or thinking note | `essay` | `references/essay.md` |
| Write or improve product copy: landing pages, headlines, CTAs, emails, product descriptions, docs | `copy` | `references/copy.md`, `references/copy-structures.md` |
| UI microcopy: labels, buttons, errors, empty states, tooltips | `copy` | `references/copy.md` (Microcopy section) |
| PRD, product spec, pushing back on a feature request | `copy` | `references/prd.md` |

Add these when they apply:

- Text not in English: `references/multilingual.md`.
- Strictness depends on the medium (LinkedIn post, investor email, README, Slack message, essay, UI): `references/context-profiles.md`.
- Paragraphs need connecting and you are reaching for a transition: `references/transitions.md`.

Whatever you write from scratch in `essay` or `copy` mode passes the P0 and P1 checks below before you return it. Load `ai-patterns.md` and `vocabulary.md` for that pass if the draft is longer than a few lines.

## Before you edit

- **Match the author's voice.** Read supplied samples first and copy their habits: sentence length, vocabulary, openings, punctuation. If they write short and say "stuff," don't hand back long sentences and "components."
- **Make the minimum effective edit.** Fix errors, repetition, inflation and passages that are hard to follow. Leave strong sentences alone. A rough draft with a real voice should still sound like the same person afterwards.
- **Never invent.** Don't add claims, numbers, sources, opinions or examples the author didn't supply. When a passage needs a fact you don't have, cut the claim or ask for the fact. Keep meaningful uncertainty and technical qualifications.
- **Don't over-flag.** A polished sentence, formal vocabulary or one "however" is not a tell on its own. Look for patterns across the piece.
- **Match format to structure.** Lists for parallel options or steps, prose for connected reasoning, tables only for comparing the same attributes.

## Principles

Kill these patterns:

1. Significance inflation. State facts and skip "pivotal moment" claims.
2. Vague attributions. Name the source or drop the claim.
3. -ing tails. "highlighting the importance of …" gets its own sentence or goes.
4. Copula avoidance. Use "is" and "has", not "serves as" or "boasts".
5. Sycophancy. Skip "Great question!" and answer.
6. Chatbot artifacts. No "I hope this helps" or "Let me know if …".
7. Generic conclusions. End on something specific, not "the future looks bright".

Write lists and bulk text for a skimming reader:

- Lead each item with the word that sets it apart from its siblings; readers often see only the first two words.
- Keep items in subject-verb-object order; when every item shares the subject, drop it and lead with the verb.
- Give parallel items one structure and one term per concept.
- Vary length, structure, or wording only where the difference means something; readers read every variation as a signal.
- Match the verb's tone to the item's point: plainly positive for what works, plainly negative for what fails.

Write with human texture:

- Vary sentence length: short, then long, then short.
- Have opinions and take stances where the piece calls for them.
- Use concrete specifics: numbers, names, dates. Take them from the source or the user; never make them up.
- Allow imperfection: contractions, fragments, sentences starting with "And" or "But".
- Use simple verbs. "Is", "has" and "does" are fine.
- Read it aloud. If you wouldn't say it, don't write it.

## Severity tiers

Use P0 and P1 for quick passes and for checking your own drafts. A full audit covers all three.

**P0, credibility killers (fix immediately):** cutoff disclaimers ("As of my last update"), chatbot artifacts and sycophancy, vague attributions ("Experts believe"), significance inflation on routine events.

**P1, obvious AI smell (fix before publishing):** Tier 1 and Tier 2 vocabulary (delve, leverage, harness, robust …), template phrases, "Let's" transition openers, synonym cycling, formulaic openings ("In the rapidly evolving world of …"), bold overuse, more than one em dash per 1,000 words.

**P2, stylistic polish (fix when time allows):** generic conclusions, compulsive rule of three, uniform paragraph length, copula avoidance, transition boilerplate (Moreover, Furthermore, Additionally).

If a text trips 5+ vocabulary flags across several categories, 3+ pattern categories and has uniform sentence and paragraph length, patching won't fix it. Recommend a full rewrite: state the core point in one sentence and rebuild from there.

## Self-reference escape hatch

When the text is *about* AI writing patterns (blog posts, tutorials, skill files like this one), quoted examples are exempt. Text in quotation marks, code blocks, or marked as illustrative ("for example, AI might write …") is not flagged. Only the author's own prose is.

## Output

**`rewrite`** returns four sections:

1. **Issues found.** Every AI-ism, with the offending text quoted.
2. **Rewritten version.** The full text. Keep the original structure, intent and every specific technical detail. Change only what the rules require.
3. **What changed.** The meaningful edits, not every word.
4. **Second-pass audit.** Re-read the rewrite and catch what survived the first pass (recycled transitions, lingering inflation, copula avoidance, filler). Fix it inline and say what changed. If it's clean, say so.

**`detect`** returns two sections:

1. **Issues found.** Every AI-ism, quoted, grouped by P0, P1 and P2.
2. **Assessment.** For each flag, say whether it's a clear problem or a judgment call. Some AI-associated patterns work in context: uniform paragraph length is a problem, a well-placed "however" isn't. If the text is clean, say so.

**`essay`** returns the essay as clean text, as `references/essay.md` describes. Rationale only when asked.

**`copy`** returns the text organized by where it lives, with annotations and alternatives, as `references/copy.md` describes.

## Tone calibration

The writing should demonstrate confidence, not assert it.

1. Vary sentence length. Fragments are fine.
2. Be concrete. Replace vague claims with numbers, names, dates or examples you actually have.
3. Have a voice. Where it fits, use first person, state preferences, show reactions.
4. Cut the neutrality. If the piece is meant to take a position, take it.
5. Earn your emphasis. Don't tell the reader something is interesting; make it interesting.

Don't over-edit. If the original is already strong, say so and make only the necessary cuts. Applying every rule at maximum strictness creates the very uniformity this skill exists to remove. The word tables are defaults, not mandates: if a flagged word is clearly right in context, keep it.
