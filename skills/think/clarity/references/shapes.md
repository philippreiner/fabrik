# Shapes

Options, never requirements. Pick a shape after the point and the outline exist, and only if the content wants it. A shape that fights the content costs more clarity than it adds.

## Answer first

BLUF, Minto's pyramid: the answer, then the reasons, then the evidence. The default for memos, exec messages and decision slides.

Reason audit (Minto). The reasons under one answer:

- are the same kind (all causes, all steps, or all criteria),
- do not overlap,
- cover the question together,
- have an order: deductive (premise, premise, conclusion), chronological, structural (parts of a whole), or by rank.

The logic sets the count. Two reasons that cover the question beat three where one is padding.

## Narrative shapes

| Shape | Order | Use when |
|---|---|---|
| SCQA (Minto) | situation, complication, question, answer | The reader shares the situation but not the complication |
| And-But-Therefore (Olson) | and, and, but, therefore | Anything that should read as a story; at least one "but" before the "therefore" |
| Start with Why (Sinek) | why, how, what | Pitches and mission pages; the reader must buy the reason before the product |
| Decision memo | situation, options including doing nothing, recommendation, the one reason | A decision is pending and the reader owns it |
| Before / after | the old world, the new world, what changed | A change the reader will feel directly |
| What is / what could be (Duarte) | alternate today and the possible future, end in the new world | Talks and keynotes that need to move people |
| Strategic narrative (Raskin) | change in the world, winners and losers, promised land, gifts, evidence | Sales decks and company pitches; the product never appears before the change is named |

## Pitch or company one-pager

The reader's problem in their terms, what you offer, how it works in one or two sentences, proof (customers, results, numbers you have), who is behind it and why they are credible, the ask. Credibility comes from people and results. The product's development history rarely earns its space. When you sell a service around someone else's product, say what the reader buys from you: deliverables, days, and the effort on their side.

For a skeptical reader, show how it works and where it fails before any adoption or market numbers. Statistics about others persuade only after the reader understands the thing.

## Decision made or still open (Tsar)

Made: the recommendation, the one number that justifies it, the risks, then stop. Open: the options, the criteria that decide, your lean and why. Mixing the two reads as either steamrolling or indecision.

## Slide craft

From analyst and consulting practice:

- Titles are full-sentence claims of at most two lines. "Churn doubled after the price change", not "Churn analysis".
- Draft the deck as titles only before adding data. If the titles do not argue, data will not save them.
- Executive summary as dot-dash: one line per section claim, its supporting points indented beneath.
- Horizontal logic: the titles alone, read in order, tell the argument. Vertical logic: everything on a slide supports its title; anything else moves or goes.
- One chart, one message; a source under every number.
- Assertion-evidence (Alley): the title asserts, the body is visual evidence (a chart, a diagram, a quote, a table). Bullets that restate the title are not evidence.
- Glance test (Duarte): the point lands in about three seconds. If the eye has nowhere to land, remove until it does.
- Calibration: Jobs used about ten words across seven slides for a product reveal.
- The first slide orients before it asks: one line on the situation the reader recognises, then the recommendation and the ask. Decision-first does not mean context-free.
- Each risk control or caveat sits on the slide where the risk arises. A recap slide that repeats them is padding.
- Size a timeline from its slowest approval (legal, works council, procurement), not from the work you control.

## Bento grids

For an overview the reader scans rather than reads. One fact per tile; tile size shows importance; a big number plus a short label; one hero tile; and a title that makes the point of the whole grid. Without that title it is a fact dump.

## Email and message

Point and ask in the first two sentences. About 150 words, unless a decision, owner, date or caveat would be lost. Below that: context, options, what you ruled out. The subject line is the point.

Status update: Progress / Plans / Problems, one to three sentences each. Problems name the ask.

## Form

- Parallel items have similar length and grammar.
- Fit length to the medium: a slide under about 40 words, an email about 150, a one-pager one page. When the piece runs long, cut in this order: mechanism, secondary features, history, then context. The point, the ask, credibility, and the cost and data lines stay.
- One focal point per slide or section; few type sizes.
- No eyebrows, kickers, taglines or helper text. The claim carries itself.
- One moment of delight per piece: one image, one line, one surprise.
- It works without the presenter.

## Where detail goes

The page carries what the decision needs. Mechanism, method, full data and caveats that do not change the decision go to an appendix, a backup slide or a linked document, and the main text says where. Speaker notes hold what the presenter says aloud, never the writer's to-dos. A number the argument depends on goes on the slide with its source; the notes may carry its caveat.

## Explaining a choice or a structure

When the reader must decide or align, pick the shape the idea needs and name it in one line:

- A trade-off: options against the two or three criteria that decide, never a feature list.
- Words are the blocker: a table of term, meaning, and what it is not.
- A process change: a reader's-eye walkthrough of what they see, do, and get next.
- A new domain: an analogy to a system the reader knows, and the point where it breaks.
- A build-up: one layer per step, each step complete on its own.
- A disagreement about viewpoint: the same topic as two or three roles see it.
- Structure or flow, smallest visual first: pseudocode for logic, a shallow call tree for runtime flow, a component tree for UI, a file tree for ownership, Mermaid for interaction or data flow, a focused diff for a change to an existing shape. Use real names from the code; label proposals as proposals.
- Too dense for chat: one self-contained HTML file in the project's `.context/show-me-<topic>.html` (or where the user names), in the product's visual language, with a clickable path. A click dummy for a flow still being shaped lives in `.context/mockups/<topic>/`: rough, clickable between states, a thinking aid and never the spec.
- Hard to follow: revise with the Hamburg comprehensibility lenses (simple words, visible order, brevity, one apt example). Procedures: one instruction per sentence, condition before action, the same term every time (STE-100 style).
