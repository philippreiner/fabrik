# Essays and memos

Write a **scientist's memo**: someone who saw the thing, understands the mechanism, and tells the reader plainly what follows and what to do. Sober, owned, concrete. Unsummarizable: if a sentence can be removed without losing an idea, it should not be there.

Model text: Jakub Pachocki, *An alien mind* (openai.com/index/an-alien-mind). Every rule below is extracted from it.

## Before writing

Work from the user's briefing and any vault notes they name. Ask at most two questions, and only when the thesis or the evidence is missing. Prefer one real scene, decision, incident, or number over more abstract context.

Write in English unless asked otherwise. Default 800–2,500 words.

## 1. Find the spine

Write three sentences in scratch before drafting:

- **Verdict** — the one claim, phrased so it could be wrong.
- **Mechanism** — the process that makes the verdict true.
- **Consequence** — what follows, and what should change.

Complete when each is one sentence, the verdict is falsifiable, and the mechanism explains rather than restates it.

## 2. Build the arc

Default order. Drop a beat only when the piece has no material for it.

1. **Scene** — one dated, specific moment. Name the year, project, people, place. State the feeling once, as a fact ("sobering"), then move on.
2. **Zoom out** — "Three years later…" Where things stand now, in three or four flat declaratives.
3. **Verdict** — the thesis as one short sentence. "This is a time that calls for extreme caution."
4. **Mechanism** — how the outcome is produced. Correct the naive frame: "*grown* more than *designed*"; "does not need to exceed all human capabilities; it just needs to surpass enough of them."
5. **Distinction** — one organizing split (goal vs. value alignment). Say why you are drawing it ("for the purpose of organizing practical research directions"). Define each side in one operational line, often as the question it answers: "does the AI try to accomplish the goal set before it?"
6. **Approaches** — for each: what it does, where it works, where it breaks, one named incident.
7. **Compounding** — layer the difficulty. "This is made more complicated by…", "even more difficult by…", "Crucially, …"
8. **What next** — concrete asks, ranked. Close on the unresolved tension. A summary is not an ending.

Headings: short phrases in sentence case; mix one evocative with the technical ("Teaching machines to love", "Pacing RSI").

Complete when the arc can be read from the first sentence of each paragraph alone.

## 3. Sentence rules

- **Thesis-first paragraphs.** First sentence carries the claim; the rest supports it.
- **I for beliefs, we for actions.** "I have a strong expectation", "I am concerned", "I find it useful to distinguish"; "We sought out access to more compute." Calibrate the verb to the confidence.
- **Hedges locate, never soften.** "to first degree", "in the average case", "largely", "likely" — each names the scope of the doubt. A hedge that names no scope is deleted.
- **Concession, then pivot.** "Of course, the boundary can be blurry. However, when I talk about X, I mean Y." "This approach can be very effective. Unfortunately, it can also be brittle."
- **One instance per abstraction.** Every mechanism gets a named project, model, incident, year, or person.
- **Italics on the load-bearing word, once.** *grown*, *experiments*.
- **Long, long, short.** A reasoning sentence with semicolons or a qualification set off by commas or parentheses; another; then a short verdict. (The em-dash limit from `ai-patterns.md` still applies; the model text's dashes are calibration, not license.)
- **Name what you are not doing and why.** "We could make the models better at X, but we do not prioritize this because…"
- **One analogy from an adjacent field**, extended exactly once ("similar to neuroscience — and, similarly to neuroscience, its overall action evades a description"), then dropped.
- **Signpost use, not structure.** "as I will discuss later" — yes. "In this section I will" — no.
- **Emotion as a stated fact about the writer**, rare, only where earned.
- **Plain vocabulary.** Technical terms stay undefined when the reader holds them; defined when the distinction is the point.
- **Institutional honesty.** "We are sometimes surprised by their results." State the limit of your own knowledge as plainly as your findings.

## 4. Cut

One pass, removing: sentences that restate the previous one; hedges that locate nothing; adjectives that do not discriminate; transitions that merely connect; any closing that summarizes.

Then run the P0 and P1 checks from `SKILL.md` on the draft (profile `essay`) and fix what they catch before returning it.

Ready when a reader can state the verdict, the mechanism, and the distinction in three sentences; every abstract claim has an instance; and the last paragraph opens the hard question rather than closing it.

## Calibration

> AI is *grown* more than *designed* - it is, to first degree, the product of repeating a straightforward optimization step many times on a hard-to-imagine amount of compute.

> The study of deep learning-based AI is largely an experimental science. We put a lot of effort into building principled algorithms and making testable predictions, but fundamentally, our large-scale training runs are *experiments*, and we are sometimes surprised by their results.

> To become very relevant in the real world - very useful or very dangerous - the AI does not need to match or exceed all human capabilities; it just needs to surpass enough of them.

Use these to calibrate hedging, rhythm, and reframing. Do not copy the subject.

## Output

Return the essay as clean text. Add rationale only when the user asks. If the user approves and asks to save, write to `03-reference/<current year>/output/` following vault conventions and tag `#claude`.
