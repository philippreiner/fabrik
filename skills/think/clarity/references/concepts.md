# Concept economy

Clarity has a currency: the reader's attention. Every unfamiliar term spends some of it.

## Concept tax and budget

Every unfamiliar term charges a concept tax: the reader stops, decodes, and only then returns to your point. Two unfamiliar terms within about ten seconds and a listener disengages (Tsar). In text that is about one unfamiliar term per 25 words: roughly one per sentence, at most two per slide or section.

- Budget before you draft. List the terms the reader does not know, keep the one or two that change the decision, translate or cut the rest.
- Never stack. Two cones in one sentence means the reader sees neither.
- Count what this reader does not know. `scripts/scan.py` counts against a frequency list, and your knowledge of the reader beats the list.

Unfamiliar is relative. "Churn" is free for a SaaS board and a cone for a hospital director. Pick the reader first, then budget in both directions:

- A term new to this reader is a cone: translate it or cut it.
- A term this reader uses every day is free, and it signals that you know their world. Use it plainly. Translating it talks down, and swapping it for a casual paraphrase makes the writer sound junior (`voice.md`).

## Translation formula

term → plain meaning → why it matters, as a decision or a risk

- "migrate off the legacy system" → "the old system is retiring" → "we need a scale decision by Q3" (Tsar)
- "latency" → "how long people wait after they click" → "every extra second loses carts at checkout"
- "technical debt" → "shortcuts we took that now slow every change" → "each feature costs about 30% more than last year"

Write all three parts the first time. After that the plain meaning carries on its own, and the term can ride along in parentheses for the experts in the room.

Translate, do not dilute. "Less technical" drops the mechanism and leaves the reader unable to judge. Bilingual keeps the mechanism and adds the meaning.

## Reader's units

Never leave a big number without perspective. "1,000 songs in your pocket", not "5 GB" (Apple). For executives: euros, hours, headcount, customers, probability.

The shape of a conversion (numbers illustrative; use real ones or none):

- 400 ms faster → about 2% more completed checkouts → about €600k a year
- 99.9% uptime → about nine hours down a year
- 3 FTE → €300k a year, the support budget of one region

State the conversion once, then use the reader's unit for the rest of the piece.

## Failure movie

Replace abstract risk words with a scene: "If this breaks, [who] sees [what], and it costs [what]."

- "less reliable" → "users stuck at checkout for twenty minutes on a Saturday evening; about €40k of orders"
- "compliance exposure" → "the auditor asks for the access log and we cannot produce it; certification slips a quarter"

A scene is harder to dismiss than an adjective and easier to size.

## Analogies

Take the analogy from the reader's domain and map the one property that matters. Follow with the precise claim. Say where the analogy breaks.

- Retrieval for a chatbot: "we cut all documents into a million post-its and pick the ten that best match the question." Precise claim: answers are only as good as the ten post-its picked. Breaks: an answer spread across fifty post-its gets lost when only ten are picked.
- A cache: "the notepad by the phone with the numbers you call most." Breaks: the notepad can be stale.

One analogy per concept. Two analogies for one concept means neither fits.

## One term per concept

Pick one word for each concept and keep it for the whole piece. Rotating synonyms (customers, users, accounts, clients) makes the reader wonder whether these are four groups. Keep a short term list while drafting; for a deck or a website, hand the list to everyone who writes.

## Proximity

- A definition sits next to its first use, in the same sentence or the next.
- Related concepts sit together. The reader should never hold a concept across three slides waiting for its partner.
- No term is used before it is introduced. Check the titles: a title can introduce a cone before the body defines it.
- Define before you compare. A comparison of two things the reader cannot picture is a comparison of nothing.

## Start from the reader's frame

Open inside what the reader already believes, then introduce your frame. Familiar before new: their problem before your architecture, their metric before yours, their words before your terms. When your frame contradicts theirs, name the contradiction, because the reader notices it anyway.

## Market words as anchors

Use the word buyers already use ("agent", "copilot", "platform"), then make it precise: "an agent, meaning software that takes the next step without being told, inside limits you set." The market word lets the reader place you in a category they already know. The precise clause says what you actually do.

## Curse of knowledge

Once you know something, you cannot imagine not knowing it (Pinker, Heath). Two symptoms with opposite fixes:

- You skip steps the reader needs: your terms, your abbreviations, your "obviously". Fix with the translation formula and the cold read.
- You explain what the reader already knows: revenue to a CFO, a sprint to an engineer, a tool every manager has used for years. Fix by trusting the reader as an expert in their field, and cut. Explain a term only when the reader's role implies they lack it.

The cold read (`cold-read.md`) is the only reliable detector, because the curse disables the writer's own judgment.
