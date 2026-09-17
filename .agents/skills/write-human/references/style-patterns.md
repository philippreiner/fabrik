# Style patterns

Consult the relevant sections for long-form or non-English editing. These are examples and clues, not quotas or evidence of machine authorship. The main skill owns scope and delivery.

## Words and phrases to replace

Words are organized into three tiers based on how reliably they signal AI-generated text. This tiered approach, adapted from [brandonwise/humanizer](https://github.com/brandonwise/humanizer)'s vocabulary research, reduces false positives on words that are fine in isolation but suspicious in clusters.

- **Tier 1, always flag.** Use these as editing prompts, not evidence of authorship. Preserve precise technical and domain terms.
- **Tier 2, flag in clusters.** Individually fine, but two or more in the same paragraph is a strong AI signal. Flag when they appear together.
- **Tier 3, flag by density.** Common words that AI simply overuses. Only flag when they make up a noticeable fraction of the text (roughly 3%+ of total words).
### Tier 1: strong candidates for replacement

| Replace | With |
|---|---|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| tapestry | (describe the actual complexity) |
| realm | area, field, domain |
| paradigm | model, approach, framework |
| embark | start, begin |
| beacon | (rewrite entirely) |
| testament to | shows, proves, demonstrates |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| cutting-edge | latest, newest, advanced |
| leverage (verb) | use |
| pivotal | important, key, critical |
| underscores | highlights, shows |
| meticulous / meticulously | careful, detailed, precise |
| seamless / seamlessly | smooth, easy, without friction |
| game-changer / game-changing | describe what specifically changed and why it matters |
| utilize | use |
| nestled | is located, sits, is in |
| vibrant | (describe what makes it active, or cut) |
| thriving | growing, active (or cite a number) |
| showcasing | showing, demonstrating (or cut the clause) |
| deep dive / dive into | look at, examine, explore |
| unpack / unpacking | explain, break down, walk through |
| bustling | busy, active (or cite what makes it busy) |
| intricate / intricacies | complex, detailed (or name the specific complexity) |
| complexities | (name the actual complexities, or use "problems" / "details") |
| ever-evolving | changing, growing (or describe how) |
| enduring | lasting, long-running (or cite how long) |
| daunting | hard, difficult, challenging |
| holistic / holistically | complete, full, whole (or describe what's included) |
| actionable | practical, useful, concrete |
| impactful | effective, significant (or describe the impact) |
| learnings | lessons, findings, takeaways |
| thought leader / thought leadership | expert, authority (or describe their actual contribution) |
| best practices | what works, proven methods, standard approach |
| synergy / synergies | (describe the actual combined effect) |
| interplay | relationship, connection, interaction |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| features (verb) | has, includes |
| boasts | has |
| presents (inflated) | is, shows, gives |
| commence | start, begin |
| ascertain | find out, determine, learn |
| endeavor | effort, attempt, try |
| keen (as intensifier) | interested, eager, enthusiastic (or cut, and just state the interest) |
| symphony (metaphor) | (describe the actual coordination or combination) |
| embrace (metaphor) | adopt, accept, use, switch to |

### Tier 2: flag in clusters

These words are legitimate on their own. When two or more show up together, the paragraph likely needs a rewrite.

| Replace | With |
|---|---|
| harness | use, take advantage of |
| navigate / navigating | work through, handle, deal with |
| foster | encourage, support, build |
| elevate | improve, raise, strengthen |
| unleash | release, enable, unlock |
| streamline | simplify, speed up |
| empower | enable, let, allow |
| bolster | support, strengthen, back up |
| spearhead | lead, drive, run |
| resonate / resonates with | connect with, appeal to, matter to |
| revolutionize | change, transform, reshape (or describe what changed) |
| facilitate / facilitates | enable, help, allow, run |
| underpin | support, form the basis of |
| nuanced | specific, subtle, detailed (or name the actual nuance) |
| crucial | important, key, necessary |
| multifaceted | (describe the actual facets, or cut) |
| ecosystem (metaphor) | system, community, network, market |
| myriad | many, numerous (or give a number) |
| plethora | many, a lot of (or give a number) |
| encompass | include, cover, span |
| catalyze | start, trigger, accelerate |
| reimagine | rethink, redesign, rebuild |
| galvanize | motivate, rally, push |
| augment | add to, expand, supplement |
| cultivate | build, develop, grow |
| illuminate | clarify, explain, show |
| elucidate | explain, clarify, spell out |
| juxtapose | compare, contrast, set side by side |
| paradigm-shifting | (describe what actually shifted) |
| transformative / transformation | (describe what changed and how) |
| cornerstone | foundation, basis, key part |
| paramount | most important, top priority |
| poised (to) | ready, set, about to |
| burgeoning | growing, emerging (or cite a number) |
| nascent | new, early-stage, emerging |
| quintessential | typical, classic, defining |
| overarching | main, central, broad |
| underpinning / underpinnings | basis, foundation, what supports |

### Tier 3: flag only at high density

These are normal words. Only flag them when the text is saturated with them, a sign that AI filled space with vague praise instead of specifics.

| Word | What to do |
|---|---|
| significant / significantly | Replace some with specifics: numbers, comparisons, examples |
| innovative / innovation | Describe what's actually new |
| effective / effectively | Say how or cite a metric |
| dynamic / dynamics | Name the actual forces or changes |
| scalable / scalability | Describe what scales and to what |
| compelling | Say why it compels |
| unprecedented | Name the precedent it breaks (or cut) |
| exceptional / exceptionally | Cite what makes it an exception |
| remarkable / remarkably | Say what's worth remarking on |
| sophisticated | Describe the sophistication |
| instrumental | Say what role it played |
| world-class / state-of-the-art / best-in-class | Cite a benchmark or comparison |

## Non-English text

This skill applies to any language, not just English. The structural tells of AI (uniformity, false ranges, conversational padding, emotional flatlining) cross language boundaries. Ensure all other languages are also clean.

When rewriting non-English text, apply the core rules through these language-agnostic checks:

#### Translated AI-isms
LLMs heavily rely on their English training data and often directly translate English AI-isms into the target language. When working in another language, look for the exact literal translations of the Tier 1 and Tier 2 English words.
- **Example (German):** The English AI tell "delve" becomes "eintauchen". "Seamless" becomes "nahtlos". "Unleash" becomes "entfesseln".
- **Example (Spanish):** "In today's fast-paced world" becomes "En el mundo acelerado de hoy". "Delve" becomes "adentrarse".
- **Action:** Treat literal translations of the English stop-words as Tier 1 offenses in the target language. Replace them with natural, culturally appropriate phrasing.
#### Register and Pronoun Dissonance
Many languages use different pronouns and verb conjugations for formal vs. informal addressing (e.g., *Sie* vs. *du* in German, *vous* vs. *tu* in French, *usted* vs. *tú* in Spanish).
- AI text frequently slips between the two, or it pairs a highly rigid, formal register with inappropriate, overly enthusiastic adjectives (e.g., using stiff bureaucratic grammar to describe a "magical, game-changing journey").
- **Action:** Enforce strict consistency. Pick one register (formal or informal) based on the context profile, stick to it, and ensure the emotional tone matches the chosen level of formality.
#### Transition Boilerplate
AI generates identical transition scaffolding across all languages.
- **Action:** Strip the literal equivalents of "In conclusion..." (e.g., *En conclusión, Zusammenfassend lässt sich sagen, En résumé*), "Let's explore..." (e.g., *Vamos a explorar, Lassen Sie uns untersuchen, Découvrons*), and "It is important to note" from the text.
#### German Specifics
When editing German text, keep the core rules but watch for typical AI patterns: literal translations from English, overly formal tone, and mixed registers. Consider here:
1. Avoid bold + colon patterns (“**Die Lösung:**”). Use normal sentences.
2. Keep register consistent (Sie vs. Du). Avoid mixing formal tone with hype.
3. Avoid empty balance phrases (“Einerseits... andererseits...”); be specific.
4. Avoid overly formal buzzwords, boilerplate, and bureaucratic transitions.

### Template phrases (avoid)

These slot-fill constructions signal that a sentence was generated, not written. If a phrase has a blank where a noun or adjective could go and still sound the same, it's too generic.

- "a [adjective] step towards [adjective] AI infrastructure" → describe the specific capability, benchmark, or outcome
- "a [adjective] step forward for [noun]" → same rule: say what actually changed
- "Whether you're [X] or [Y]" → false-breadth construction. Pick the audience you're actually addressing, or cut. "Whether you're a startup founder or an enterprise architect" means nothing. It is just "everyone."
- "I recently had the pleasure of [verb]-ing" → review/social AI pattern. Just say what happened: "I talked to," "I read," "I attended."
- **Aphorism formulas**: "X is the Y of Z", "the currency of trust", "the architecture of", "X becomes a trap", "X is not a tool but a mirror". These dress an ordinary claim as profundity. Replace with the concrete claim it gestures at.
- **Persuasive authority tropes**: "The real question is", "at its core", "in reality", "what really matters", "fundamentally", "the deeper issue", "the heart of the matter". They pretend to cut to a deeper truth before restating an ordinary point. Drop the framing and state the point.
### Transition phrases to remove or rewrite
- "Moreover" / "Furthermore" / "Additionally" → restructure so the connection is obvious, or use "and," "also," "on top of that"
- "In today's [X]" / "In an era where" → cut or state specific context
- "In conclusion" / "In summary" / "To summarize" → your conclusion should be obvious
- "When it comes to" → just talk about the thing directly
- "At the end of the day" → cut
- "That said" / "That being said" → cut or use "but," "yet," or "however." Don't overuse any one of them.
## Structural issues
- **Uniform paragraph length**: Vary deliberately. Include some 1-2 sentence paragraphs and some longer ones. If every paragraph is roughly the same size, fix it.
- **Formulaic openings**: If the piece opens with broad context before getting to the point ("In the rapidly evolving world of..."), rewrite to lead with the news or the insight. Context can come second.
- **LinkedIn revelation cadence**: "I used to think X. I was wrong. It's actually Y. Here are N lessons." This structure can work when it carries a specific lived reversal. Without that, it reads like engagement bait. Rewrite as a direct argument or a concrete story.
- **Suspiciously clean grammar**: Don't sand away all personality. Deliberate fragments, sentences starting with "And" or "But," comma splices for effect: if the natural voice uses them, keep them.
### Significance inflation
- Phrases like "marking a pivotal moment in the evolution of..." or "a watershed moment for the industry" inflate routine events into history-making ones. State what happened and let the reader judge significance.
- If the sentence still works after you delete the inflation clause, delete it.
### Copula avoidance
- AI text avoids "is" and "has" by substituting fancier verbs: "serves as," "features," "boasts," "presents," "represents." These sound like a press release.
- Default to "is" or "has" unless a more specific verb genuinely adds meaning.
- The mirror image is the buried verb. "Made a decision" is "decided". "Has the ability to" is "can". "Performed an analysis of" is "analysed". Put the action in the verb, not in a noun with a helper attached.
### Synonym cycling
- AI rotates synonyms to avoid repeating a word: "developers… engineers… practitioners… builders" in the same paragraph. Human writers repeat the clearest word.
- If the same noun or verb appears three times in a paragraph and that's the right word, keep all three. Forced variation reads as thesaurus abuse.
### Vague attributions
- "Experts believe," "Studies show," "Research suggests," "Industry leaders agree," "many creators are realizing," "businesses across industries are discovering" all name nobody. Either cite a specific source or drop the attribution and state the claim directly. Same for attributive passives: "has been described as," "is regarded as," "is considered."
### Filler phrases
- Strip mechanical padding that adds no meaning: "In terms of", "The reality is that", "With regard to", "When it comes to the question of". Just state the claim.
### Generic conclusions
- "The future looks bright," "Only time will tell," "One thing is certain," "As we move forward" are filler disguised as conclusions. Cut them. If the piece needs a closing thought, make it specific to the argument.
- **Fake-profound kickers**: the final line that turns the point into a metaphor, an aphorism, or a mic drop ("The tool was never the bottleneck."). Delete it. Do not rewrite it into a better metaphor and do not preserve its rhythm. End on the clearest concrete sentence already in the draft. If the ending needs more closure, add a plain takeaway or the next action.
### Chatbot artifacts
- "I hope this helps!", "Certainly!", "Absolutely!", "Feel free to reach out," "Let me know if you need anything else" are conversational tics from chat interfaces, not writing. Remove entirely.
- Also watch for meta-narration about the piece itself: "In this article, we will explore…", "This post covers…", "This piece aims to…". Cut it or rewrite as a direct opening.
- Canned procedural preambles belong here too, including in commit messages and pull requests: "This preserves all information while improving tone."
### "Let's" constructions
- "Let's explore," "Let's take a look," "Let's break this down," "Let's examine". AI uses "let's" as a false-collaborative opener to ease into a topic. It's filler that delays the actual point. Just start with the point. Flag any "let's + verb" that works as a transition rather than a real invitation to act, including "Let's dive in."
### Notability name-dropping
- AI text piles on prestigious citations to manufacture credibility: "cited in The New York Times, BBC, Financial Times, and The Hindu." If a source matters, use it with context: "In a 2024 NYT interview, she argued..." One specific reference beats four name-drops.
### Superficial -ing analyses
- Strings of present participles used as pseudo-analysis: "symbolizing the region's commitment to progress, reflecting decades of investment, and showcasing a new era of collaboration." These say nothing. Replace with specific facts or cut entirely.
### Promotional language
- AI defaults to tourism-brochure prose: "nestled within the breathtaking foothills," "a vibrant hub of innovation," "a thriving ecosystem." Replace with plain description: "is a town in the Gonder region," "has 12 startups." If you wouldn't say it in conversation, cut it.
### Formulaic challenges
- "Despite challenges, [subject] continues to thrive" or "While facing headwinds, the organization remains resilient." This is a non-statement. Name the actual challenge and the actual response, or cut the sentence.
### False ranges
- AI creates false breadth by pairing unrelated extremes: "from the Big Bang to dark matter," "from ancient civilizations to modern startups." These sound sweeping but say nothing. List the actual topics or pick the one that matters.
### Inline-header lists
- Bullet lists where each item starts with a bold header that repeats itself: "**Performance:** Performance improved by..." Strip the bold header and write the point directly. If the list items need headers, they should probably be paragraphs.
### Title case headings
- AI over-capitalizes headings: "Strategic Negotiations And Key Partnerships" instead of "Strategic negotiations and key partnerships." Use sentence case for subheadings. Title case only for the piece's main title, if at all.
### Cutoff disclaimers and speculative gap-filling
- "While specific details are limited based on available information," "As of my last update," "I don't have access to real-time data." These are model limitations leaking into prose. Either find the information or remove the hedge. Never publish a sentence that admits the writer didn't look something up.
- The flip side: when a model can't find a source it invents plausible filler: "maintains a low profile," "keeps personal details private," "likely grew up in," "it is believed that." Say what isn't known or cut the sentence; don't dress a guess as fact.
### Diff-anchored writing
- Docs or comments that narrate a change instead of describing the thing as it is: "This was added to replace the previous approach," "We refactored this to avoid the old O(n²) loop." Unless the document is version-scoped (changelog, migration guide, ADR), it should read coherently without knowing the last commit. State what the code does and why, not what it used to do. Especially relevant for our `docs/` and code comments.
### Novelty inflation
- AI text treats established concepts as if the speaker invented or discovered them: "He introduced a term," "She coined the phrase," "a concept nobody's naming," "a failure mode nobody talks about." In reality, most ideas in a conversation are applications of existing concepts, not inventions.
- Two problems. First, it's factually risky: if the concept already has a Wikipedia page or conference talks from last year, claiming novelty makes the writer look uninformed. Second, it flatters the subject in a way that reads as promotional rather than analytical.
- The fix: describe what the person *did with* the concept, not that they discovered it. "Michel walked through how context poisoning works in practice" instead of "Michel introduced a term I hadn't heard before: context poisoning." If you're unsure whether something is novel, assume it isn't and frame accordingly.
- Related patterns to flag: "the failure mode nobody's naming," "a problem nobody talks about," "the insight everyone's missing," "what nobody tells you about." These are engagement-bait framings that claim scarcity of knowledge where none exists.
### Emotional flatline
- AI claims emotions as a structural crutch without conveying them through the writing: "What surprised me most," "I was fascinated to discover," "What struck me was," "I was excited to learn," "The most interesting part."
- Two problems. First, it's tell-don't-show: if the thing is genuinely surprising, the reader should feel that from the content, not from the writer announcing it. Second, these phrases are massively overused as list introductions and transitions. They're filler wearing an emotion costume.
- This pattern isn't always AI. It's also a sign of lazy human writing on autopilot. Flag it either way.
- The fix isn't "never say surprised." It's: if you claim an emotion, the writing around it should earn it. Otherwise cut the claim and present the thing directly.
### False concession structure
- "While X is impressive, Y remains a challenge" or "Although X has made strides, Y is still an open question." AI uses this to sound balanced without actually weighing anything. Both halves are vague. Either make the concession specific (name what's impressive, name the actual challenge) or pick a side and argue it.
### Rhetorical question openers
- "But what does this mean for developers?" / "So why should you care?" / "What's next?" AI uses rhetorical questions to stall before the actual point. If you know the answer, just say it. Rhetorical questions are earned by strong setup, not dropped as section transitions.
### Parenthetical hedging
- "(and, increasingly, Z)" / "(or, more precisely, Y)" / "(and perhaps more importantly, W)" AI inserts parenthetical asides to sound nuanced without committing. If the aside matters, give it its own sentence. If it doesn't, cut it.
### Padded lists
- The count is the symptom; padding is the fault. "Five things to know" with two real items and three restatements needs the three cut, not the list. Keep the list when every item is a distinct, parallel point, and drop the number from the heading if it is doing the promising.
### Reasoning chain artifacts
- "Let me think step by step," "Breaking this down," "To approach this systematically," "Step 1:," "Here's my thought process," "First, let's consider," "Working through this logically" are artifacts of chain-of-thought reasoning leaking into published prose. The reader doesn't need to see the scaffolding. State the conclusion, then the evidence.
- Also watch for numbered reasoning steps that read like an internal monologue rather than an argument meant for an audience.
### Sycophantic tone
- "Great question!", "Excellent point!", "You're absolutely right!", "That's a really insightful observation" are conversational rewards from chat interfaces, not writing. Remove entirely.
- Distinct from chatbot artifacts: sycophancy specifically validates the reader/questioner rather than just performing helpfulness.
### Acknowledgment loops
- "You're asking about," "The question of whether," "To answer your question," "That's a great question. The..." all restate the prompt before answering. In writing, this is pure filler. The reader knows what they asked. Just answer.
- Related pattern: opening a section by summarizing what the previous section said. If the structure is clear, the reader doesn't need a recap.
### Confidence calibration phrases
- "It's worth noting that," "Interestingly," "Surprisingly," "Importantly," "Significantly," "Notably," "Certainly," "Undoubtedly," "Without a doubt" signal how the reader should feel about a fact instead of letting the fact speak for itself.
- "Here's what's interesting," "Here's the interesting part," "Here's what caught my eye," "Here's what stood out" are reader-steering cues that pre-interpret importance. Works when followed by genuinely surprising data; fails when it introduces a restatement of something obvious (which is the AI default).
- **Interpretive metadiscourse**: lines that step outside the subject to tell the reader what to notice or how much weight to give it. "That last part matters more than it sounds," "The key point is," "This distinction matters," "As you can see," and redundant "In other words." If the point is already clear, delete the aside. If it is not, replace the aside with the fact or support that makes it clear.
- One "notably" in a 2,000-word piece is fine. Three in 500 words is emphasis stacking. Flag by density.
### Excessive structure
- Too many headers in short text: more than 3 headings in under 300 words is almost always AI trying to look organized. Merge sections or use prose transitions instead.
- Bullets that are not parallel: if the items argue with each other, build on each other, or vary wildly in length, they are a paragraph wearing a list costume. The reverse also counts: a dense paragraph holding six parallel options should be a list.
- Formulaic section headers: "Overview," "Key Points," "Summary," "Conclusion," "Introduction," and the "X and Y" pairs ("Legacy and impact," "Challenges and future outlook") are default AI scaffolding. Use headers that tell the reader something specific about what follows.
### Quick tells
- **Vague connection expressions**: "associated with leadership," "has been linked to," "worked alongside." Name the relation: "was CEO of"
- **Heading hygiene**: skipped levels, headings holding only subheadings, an H1 inside the body, a rule between every section
- **Tool artifacts**: `[oaicite]`, `contentReference`, `turn0search0`, `[cite: 1]`, stray lenticular brackets, `utm_source=` on pasted links. Nothing human produces these
- **Style shift**: one paragraph that turns suddenly fluent, balanced, and evenly paced. Match it to the surrounding voice, not the reverse
- **Assistant register**: hedged, agreeable, unwilling to lose anyone. If nobody could disagree with a sentence, it says nothing
- **Fake-empathy openers**: "Imagine you're a founder with three weeks of runway." Use a real example or none
## Rhythm and uniformity

These aren't individual word or phrase problems. They're patterns in how the text flows as a whole. AI text is metronomic; human text has varied rhythm.

**Rhythm outranks vocabulary.** Uniform sentence construction, even pacing, and symmetrical phrasing are what make text feel machine-made, and they survive any amount of word swapping. If you fix every word on the Tier 1 list and leave the rhythm alone, the piece still reads as generated.

- **Sentence length uniformity**: If most sentences are 15–25 words, the text sounds robotic. Mix short punchy sentences (3–8 words) with longer flowing ones (20+). Fragments work. Questions break the monotony.
- **Manufactured punchlines / staccato drama**: AI makes every sentence land like a quotable closer, then stacks short fragments to fake intensity ("No symmetry. No prior. No nostalgia. The old rules were gone."). One short sentence for emphasis is fine; a run of them is engineered. Collapse the run into a real clause.
- **Paragraph length uniformity**: If every paragraph is 3–5 sentences and roughly the same size, vary deliberately. Some paragraphs should be one sentence. Some should be longer.
- **Vocabulary repetition vs. synonym cycling**: AI either repeats the same word mechanically or cycles through synonyms conspicuously. Human writers repeat when the word is right and vary when it's natural. There's no formula.
- **Read-aloud test**: If the text sounds like it could be read by a text-to-speech engine without sounding weird, it's probably too uniform. Human writing has rhythm that resists robotic delivery.
- **Missing first-person perspective**: Where appropriate, the writer should have opinions, preferences, and reactions. AI is relentlessly neutral. If the piece is supposed to have a voice, the absence of "I think," "in my experience," or a stated preference is itself an AI tell.
- **Over-polishing**: Editing out every irregularity produces the flat uniformity this whole skill exists to remove. Natural disfluency, odd word choices, and uneven pacing are what make prose sound like a person. Don't sand away personality in pursuit of clean copy. Applying every rule at maximum strictness makes the writing less human, not more.

## Adjust for the format

Read the piece first and match the strictness to what it is. For long-form prose, inspect structure and rhythm as well as vocabulary. Short social posts and internal notes keep fragments, lists, and one or two emoji, and only the worst offenders are worth an edit. Investor, customer, and board writing gets the strictest pass on promotional language and significance inflation, where one "thriving ecosystem" undermines the whole message. Documentation trades voice for clarity, so hedging that is technically accurate stays, and steps belong in a list.

Technical writing keeps the terms that carry real meaning in context: `robust`, `comprehensive`, `seamless`, `ecosystem`, `leverage` (actual platform leverage or APIs), `facilitate`, `underpin`, `streamline`. Still cut `delve`, `tapestry`, `beacon`, `embark`, `testament to`, `game-changer`, `harness`.
