---
name: clarity
description: Clear writing and review for smart, busy readers. Use when writing, structuring or reviewing high-level content (a slide, a deck, an exec message or update, sales and pitch material, website copy, a one-pager, a memo), when explaining a decision, change, or structure the user must decide or align on, or when asked to make something clearer, simpler, less technical, or "for execs". English and German.
---

# Clarity

Clarity means the reader gets the point and the next step at the lowest cognitive cost, with no dumbing down. It happens in the reader's head. A short, correct, well-formatted page can still leave the reader without a decision.

Every reader asks three questions (Tsar): what changed, why it matters, what do you need from me. Answer them early, in that order. In a deck, the first slide carries the point and the ask, and the three answers may take the first two or three slides.

This skill covers high-level content: slides and decks, exec messages and updates, sales and pitch material, website copy, one-pagers, memos. For long-form essays and personal voice, use the write-human skill.

## Thinking model

- **Bilingual.** Speak the expert's language and the reader's at once. Translation keeps the information that making a text "less technical" would drop. Give the term, its plain meaning, and why it matters as a decision or risk: "latency" becomes "how long people wait after they click; every extra second loses carts at checkout."
- **Concept tax.** Every term new to the reader costs attention. Unfamiliar terms are verbal orange cones. One is fine. A street full of them and the reader watches the cones instead of the road. Budget about one new term per sentence and two per slide or section. Terms the reader uses every day are free.
- **Decision-first.** Mechanism-first (how it works, then what it means) suits building and fails in briefings. Open with what the reader should decide or do. Add mechanism only where it changes the decision.

## Principles, ranked

1. Point first, with orientation. The first sentence or title states what the reader should think, decide or do, in words a reader arriving cold can place: what this is about comes before what to do about it. The ask names who decides what, by when.
2. Spend the concept budget on purpose. Count the cones, translate each at first use, cut the rest.
3. One term per concept, defined next to its first use. Related ideas sit together, and nothing is used before it is introduced.
4. Write from the reader's side, to the reader as "you": their units (money, time, people, risk) and what they keep, do and get. "1,000 songs in your pocket" instead of "5 GB"; "your teams keep their tools" instead of "replaces none of them"; "you decide" instead of "the CEO decides" on a page the CEO reads.
5. Titles tell the story alone. Each title is a claim that its body proves.
6. Parallel things look parallel. Use lists and tables for items of the same kind, with similar length and grammar, and prose for reasoning.
7. Sound like a senior practitioner briefing a peer: the reader's professional vocabulary, precise nouns, varied sentence length, and every paragraph ending on a fact. No aphorisms, quip closers or mirrored contrasts (`references/voice.md`).
8. Never invent a fact. Name each gap with who can fill it, and bound what you can: a ceiling, a range, the date the real number arrives. Where the reader must set something (a threshold, a plan, a scope), propose a default, mark it as your proposal and name who confirms it; a bare "Open:" is homework for the reader. A fact found only in an unverified or AI-written draft counts as missing. Inside the piece a gap reads as a sentence ("Fee: in our written offer"), never as a bracket. When the piece cannot work without the fact, ask the author.

## Moves

Scale the effort with the stakes. A chat reply gets moves 1, 2 and 6. A board deck or a website gets all of them, plus a cold read.

1. **Name the reader.** One line: who reads this, what they already know, which words they use daily, what they decide. The cone count depends on it.
2. **Find the point.** One sentence: what the reader should think, decide or do afterwards. Until it exists, the piece is not ready to write.
3. **Outline and order** before choosing a format. List the claims, check they answer the three questions, and put the decision first. Pick a shape from `references/shapes.md` when the content fits one.
4. **Write variations**: three openings, ten titles or two structures; for a deck, vary the whole title storyline. Shortlist three, score them against a few picked checks, keep the winner, and stop after one round.
5. **Draft** in the reader's words. Introduce each new concept where it is first needed, next to its translation.
6. **Check.** Take the default set for the format from `references/checks.md`, add what fits, and review against at least 20 checks.
7. **Cut**, then **format**. Formatting comes last so it serves the argument.

Translating between languages: carry the concept and recount the cones, because a familiar term in one language is often a cone in the other. Write German the way a German consultant writes it: standard business terms, natural word order, no colloquial phrasing and no English sentence rhythm. Choose Sie or du once and hold it, and split compound nouns over about 20 letters.

## Output

When writing: the piece. Below it, one line with the point and ask you aimed for, one line per trade-off (a cone kept on purpose, a caveat that cost words), and one line per missing fact.

When reviewing: the point and the ask as you read them, the cones with a translation or a cut for each, the failed checks ranked by damage to the reader, and a rewrite of the three worst places. Strong passages stay as they are.

## Before it ships

For anything you send, present or publish (paths are relative to this skill's folder):

- Run `python3 scripts/scan.py FILE` (or pipe text in; `--lang en|de`, `--json`, `--known "Term A,Term B"` for product names and the reader's jargon). It prints the titles as a storyline, a chart of unfamiliar terms, the worst sentences, AI filler, generated-sounding shapes and patterns, and a load number (new terms per 100 words) for comparing drafts. The word list does not know your reader, so you decide which flagged terms are cones. Treat a single flag as a hint and a cluster as a problem.
- Run the cold read in `references/cold-read.md`: a fresh reader restates the point and the ask from the text alone.

## References

- A term, number or analogy needs translating, or the reader drowns in jargon: `references/concepts.md`.
- Choosing a structure, slide titles, a pitch, a bento grid, an email or a status update: `references/shapes.md`.
- Reviewing a draft or picking the checks: `references/checks.md`.
- The draft sounds generated, casual or junior: `references/voice.md`.
- The piece ships, or the audience is unknown: `references/cold-read.md`.

## Done when

- A cold reader restates the point and the ask as intended.
- The titles alone tell the story.
- Every unfamiliar term was counted and is either translated at first use or cut.
- The scan shows no AI shape in a title, no CUT filler, and no AI pattern line (uniform sentence length, repeated openers, one title shape).
- Every picked check passes, or its trade-off is named in one line.
