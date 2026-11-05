# Voice

How the piece sounds. The target is a senior practitioner briefing a peer: precise, calm, in the reader's professional language. Clear does not mean casual, and plain words do not mean a plain register.

## Register

- Use the vocabulary the reader works with every day. For a board that is business case, run-rate, steering committee, transformation, recovery; for a CFO, cash flow, payback, working capital; for an engineering lead, incident, on-call, release. These words cost this reader nothing and show that you know their world. Translating them talks down.
- Replace casual phrasing with the professional term the reader would use. "Get the project back on track" becomes "project recovery"; "trouble" becomes "risk" or "issue"; "hit other projects" becomes "downstream dependencies"; "a lot of" becomes the number; "stuff" becomes the noun.
- Before finishing, list five to eight terms a senior practitioner in the reader's field would use about this topic, and check that the piece uses the ones that fit, once each, without explaining them.
- Aim one notch more formal than a chat message and one notch less formal than a contract. A senior consultant's memo, minus the jargon nobody in the room uses.
- State facts at their real size. No hype adjectives, no sales superlatives, no manufactured urgency.
- German: Sie unless the relationship clearly says du. Professional without being bureaucratic: verbs instead of Nominalstil, no "im Rahmen von", no "es ist darauf hinzuweisen". Write it as German, not as translated English: German business terms where they are standard (Freigabe, Verantwortliche, Budget), sentence order a German reader expects, no colloquial shortcuts ("das klappt" → "das funktioniert", "kriegen" → "erhalten").

## Sentence shapes that read as generated

These shapes make a text sound machine-written even when every word is fine. Readers notice them before any single word. Write the plain statement instead: subject, verb, the fact.

| Shape | Example | Plain version |
|---|---|---|
| Mirrored contrast | "Speed is a strategy, not a metric." / "Wir verkaufen keine Software, sondern Sicherheit." | State the claim and its evidence. Address the other view only if the reader holds it, in its own sentence. |
| Antithesis pair | "Others report problems; we prevent them." | Say what you do: "The system flags a supplier delay on the day it is announced." |
| Aphorism opener or closer | "Every delay is a decision someone did not make." | "Three of the five delays came from open decisions." |
| Colon reveal | "The result: fewer outages." / "Das Ergebnis:" | "Outages fell from six to two a quarter." |
| Staged setup | "Here's the thing:", "The catch?" | Start with the thing. |
| Fragment drumbeat | "Fast. Simple. Secure." | One sentence with the evidence for the one quality that matters. |
| Habitual triplet | three adjectives, three parallel clauses | Use the number of items the content has. |
| Rhetorical question as transition | "So what does this mean for you?" | Say what it means. |
| Title formula or slogan | "Why X matters", "From X to Y", "…before your competitor does" | A claim title: subject, verb, the finding. |
| One title shape for every slide | "X, because Y" on three slides | Give titles different jobs: a recommendation, a fact, a risk, a number, a decision. |
| Quip closer | "…, and that makes all the difference." / "That only a pilot can show." | End the paragraph, note or slide on the fact the reader needs next. |
| Tacked-on reveal | "…monitored the migration, the work we now automate." | Give the link its own plain sentence: "We automate that monitoring." |
| Comma tail | "You hear about it at the board meeting, or later." / "…and replaces none of them." | Say the fact once and stop at the full stop. |
| Anaphora | "It flags… It flags… It drafts…", the product name opening every other sentence | Merge into one sentence with a list, or vary the subject. |
| Orphan fact | a one-line fact bolted onto the end of an unrelated paragraph | Move it where it belongs, or give it its own line with context. |

One deliberate contrast per piece is allowed when the reader holds the wrong belief and the contrast corrects it. Never in a title.

## Precision

- Name the thing. "The facts behind it", "the data", "this", "things" make the reader ask "which?". Write the noun: "last quarter's order intake by region".
- Long sentences carry reasoning (because, so, unless, which means). They never stack attributes or trailing qualifiers: "The platform consolidates supplier data across all plants and flags late deliveries against contract terms, with a confidence score for every alert" becomes two sentences, one per claim.
- Describe the effect from the reader's side of the table: what they keep, do, get or avoid. "Your teams keep their current tools" instead of "replaces none of them".
- Address the reader as "you". Naming their role ("the CTO sets the threshold") on a page they read sounds like a report about them.

## Words

Run `scripts/scan.py`: it lists AI filler words (CUT always, HIGHLIGHT in clusters), hedges and padding in English and German. Typical offenders: delve, leverage, robust, seamless, cutting-edge, pivotal, landscape, unlock, empower; nahtlos, ganzheitlich, zukunftsweisend, maßgeschneidert, "spielt eine entscheidende Rolle". Also cut chatbot artifacts ("I hope this helps"), sycophancy, vague attributions ("experts agree"), and generic conclusions ("the future looks bright"). For a full audit of a long text, use the write-human skill.

## Lists are fine

Bullets, numbered steps, tables and tickets are the right form for parallel items, and executives scan them faster than prose. Do not turn a list into paragraphs to look human. What reads as generated is uniformity: every bullet the same length and shape, a bold label on every line, every section with exactly three points. Use bold lead-ins only when the list is meant to be scanned by label.

## Rhythm

Uniform brevity reads as generated. A text where every sentence runs 8 to 14 words sounds machine-made even when each sentence is clean, so short-sentence rules apply to the average, never to every sentence. After two short sentences, write one with a subordinate clause that carries reasoning. Avoid runs of sentences with the same opening. The scan reports the spread of sentence length and repeated openers. Read the piece aloud once; where you would never say it that way to the reader's face, rewrite.
