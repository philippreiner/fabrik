# Cold read

Clarity is measured in the reader's head. The cold read puts a reader there who has not seen your intent: a fresh subagent that sees only the text. Run it for anything that ships, and twice when the audience is unknown.

## The loop

1. Predict 5 to 10 questions a real reader would ask after reading. Start from the fixed exec questions below and add questions specific to the piece. Write down the answers you intend.
2. Reader pass. Give a fresh subagent only the text and a persona. It answers your questions from the text alone, restates the point in one sentence, states the ask (who does what by when), and lists every word or sentence it stumbled over.
3. Critic pass. Give a second fresh subagent the text alone. It hunts for ambiguity (two possible readings), false assumptions about what the reader knows, contradictions between numbers, claims or titles, and the first question a skeptic would ask.
4. Compare in a table: question, intended answer, reader's answer, match (yes, partly, no). Fix the text where they differ, never the questions. Then give the fixed text to one more fresh reader, because fixes create new contradictions.

The subagents get the text only: no brief, no intent, no draft history. Any context you hand them is context the real reader will not have. Tell them whether speaker notes are part of what the audience sees.

## Fixed exec questions

- What is the ask?
- Who decides?
- By when?
- What does it cost: money, people, time, risk?
- Why now?

## Persona critics

Pick the personas closest to the real readers, one or two per pass.

| Persona | Hunts for |
|---|---|
| CFO | the number, the cost, the downside, what happens if we wait |
| Skeptical engineer | hand-waving, claims without mechanism, invented numbers |
| Buyer | what changes for them on Monday, switching cost, the risk of looking foolish |
| Outsider | every term they would have to look up, every assumption of shared context |

Style lenses, usable as critics ("read this as X would"):

- Apple circa 2010: one product truth in the reader's units, said once, big.
- Stripe: precise and calm; every claim concrete enough to check.
- Amazon: numbers instead of adjectives; the memo answers the question before the meeting.
- McKinsey: the titles argue; reasons are MECE; a so-what on every page.
- Paul Graham: talk-test words; a point the writer could lose an argument over.
- Basecamp: read in the worst light; plain, short, no sell.

## Be unreasonable

For anything that ships, write variations before converging: ten headlines, three structures, three openings. Shortlist three, score them in a small table against five or six of the picked checks, keep the winner, and stop after one round. Look at how others solved the same thing (a competitor's page, a known memo, a keynote) before settling.

## Subagent prompts

Reader:

```
You are [persona]. Read the text below once, as a busy reader would. Then answer:
1. In one sentence: what is the point?
2. What is being asked of you? Who decides, by when?
3. Answer these questions from the text alone; say "not in the text" when it is not: [questions]
4. List every word or sentence you stumbled over or had to reread.

Text:
[text]
```

Critic:

```
Read the text below as a skeptical [persona]. Quote each finding:
- sentences with two possible readings
- things the text assumes the reader already knows
- contradictions between numbers, claims or titles
- the first question you would ask the author
Rank the findings by damage to the reader and give the top 5 first.

Text:
[text]
```

## Without a subagent tool

Do the cold read as a separate pass yourself: finish the draft, write the predicted questions, then reread the text top to bottom as the persona, answering only from what is on the page. Say in your output that the cold read was a self-pass, so the author knows it carries less weight.
