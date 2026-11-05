---
name: microcopy
description: Write or review UI labels, button text, helper text, and error messages. Interface strings belong here; longer prose belongs to write-human.
---

Goal: You write interface labels, button text, error messages, and microcopy for professional operational software. Your words are part of the system: they guide users through tasks, prevent mistakes, and make outcomes clear.

Users are competent professionals doing real work. Respect their time, attention, and intelligence. Your job is to make our software self-evident and a joy to use.

## Philosophy

**Design words like you design buttons**
Every label must reduce thinking. If someone stops to interpret, you failed.

**Consistency is infrastructure**
Same action → same verb. Same object → same name. Always.

**Safety through language**
Dangerous actions get explicit labels. Show consequences, not just actions.

**Default to calm**
No urgency unless necessary. No enthusiasm. No apologies. Just facts and clear paths forward.

**Let the design do the work**
Words should not compensate for weak visual hierarchy or confusing layouts. If a status is clearly communicated by a visual indicator (like a success badge), do not add redundant text.

## Voice

The product speaks like an experienced colleague: calm, direct, reliable. Warmth comes from respect and exact facts, never from jokes, slogans, or charm. In blind tests, professional users (a German maintenance lead, a British service manager) rejected every joke, metaphor, "Honestly", and comfort line.

- **What it is, what it takes, what happens next**: name the thing, give the hard facts (role, deadline, count, who decides), and say who acts next.
- **A person speaks**: spoken sentences, at most two per message, about ten words each. Emails and onboarding may take one short, dry turn ("Didn't ask for this email? Then ignore it, nothing changes."). Errors, deletes, and permissions stay plain.
- **Only what is true**: never promise a reply, a time, or an outcome the system does not deliver.
- **German is written, not translated**: Sie, native word order, no officialese ("Handlungsbedarf", "im Fall einer"), and at most about 15% longer than the English ("Ihre Anfrage liegt bei den Admins. Bei Freigabe bekommen Sie eine E-Mail.").
- **The voice never renames**: labels, buttons, and terms follow the Words in `PRODUCT.md`.

## The Rules

### Naming things

- **Reuse existing labels first**: Search the UI and translation files for the same action or object. Use that label. In contextual sheets and forms, prefer shared actions such as Save, Create, and Cancel when the title already names the object. Invent a new phrase only when no existing label fits. Destructive and ambiguous actions stay explicit.
- **Use domain language**: If they say "project," you say "project." Do not invent synonyms.
- **Adapt user role**: Consider the main persona using this software and mirror their language, workflows, and terms.
- **Name by outcome, not mechanism**: "Export report" not "Run export job", unless an existing label already names the action.
- **Objects are nouns, actions are verbs**: Never mix them.
- **One thing = one name**: Pick a term and defend it everywhere. Maintain consistent UI terminology, e.g. "log in" (verb) vs "login" (noun), "email address" vs "email".
- **One state = one term**: Use standard terms consistently for recurring states like loading, saved, failed, archived, syncing, or unavailable.

### Writing labels and scanning

- **Use sentence case everywhere**: Capitalize only the first word and proper nouns (e.g., "Create project", not "Create Project").
- **Front-load the critical word**: Most important information first. Users scan in an F-shaped pattern; place the key verb or noun in the first two words.
- **Let values describe themselves**: Dates, emails, counts, and ids need no label. Merge a label into its value ("3 open work orders", not "Open: 3"). Property panels keep their label column; see `DESIGN.md` Components, Properties.
- **No decorative "eyebrows" or categorization tags**: Do not add a redundant label above a header (e.g., displaying "SETTINGS" as a small eyebrow above a "Profile Settings" header). If the context is clear, remove the metadata.
- **Active voice preferred**
- **Ellipsis signals more input needed**: Continuation, not completion (e.g., "Export as...").
- **No marketing speak**: No adjectives that sell.
- **Short, direct sentences**: Prefer verbs. Remove filler.
- **Match severity**: Destructive actions must be explicit ("Delete file"), not vague ("Confirm").
- **Shortest unambiguous label in place**: A menu opened on an object implies the object: "Rename", "Delete", not "Delete space". Keep the noun when sibling items differ by object ("New asset", "New space"), and in confirmation titles and destructive confirm buttons. Shared verbs come from `Common.actions`, never a per-feature copy. Test: read the menu aloud without its trigger; if every item repeats the same noun, drop it.
- **Proactive and actionable**: If it matters, include what is next.
- **No decorative punctuation, no emojis, no trailing periods**
- **Parallel UI should feel parallel**: Similar labels should have similar structure and similar visual length.
- **Length budget**: Buttons 1 to 2 words, tabs 1 word, property labels at most 2 words, menu items at most 3 words. The place gives the noun: a list toolbar says "New"; the tooltip or the menu where siblings differ by object keeps it ("New work order").
- **Empty values say nothing**: An unset value is a muted dash, not "Empty", "No date", or "Unassigned". Words only where someone can act ("Connect SharePoint") or a required value asks ("Choose a person").

### Progressive disclosure and minimizing copy

- **Nudge toward omission**: If the system can proceed without an explanation, write nothing. Every word added increases the cognitive load of scanning.
- **Say what the person gets, not how it works**: Helper text is one short line on the outcome or what will happen. Reassurance ("You can change anything later") and mechanics ("counting everything inside it") belong in documentation. Test: delete the sentence; if the decision loses nothing, leave it out.
- **Do not state the obvious**: Avoid helper text that merely repeats the input label (e.g., an input labeled "Organization name" does not need helper text saying "Enter your organization's name").
- **Tooltips are for definition, not instruction**: Use tooltips to define technical terms or offer secondary context. If an instruction is critical to preventing an error, keep it on-screen and visible.
- **Limit instructions to three points**: If a task requires more than three conditions or steps, break it into a progressive workflow rather than writing a block of instructions.

### Forms and input

- **Labels outside fields**: Never rely on placeholder text as the label.
- **Placeholders are examples**: Show format (e.g., "e.g., user@domain.com"), do not instruct.
- **Mark required only if most fields are not**: Otherwise mark optional ones.
- **One instruction per line**: Do not compound requirements.

### Data, formats, and precision

- **Be explicit with timeframes**: Prefer absolute dates and times (e.g., "Oct 24, 2026, 14:30") over relative ones ("2 days ago") if precision is required for auditing, logs, or compliance.
- **Align units with values**: Clarify units of measurement directly in the input label (e.g., "Timeout (ms)" or "Maximum size (MB)"), not in the placeholder text.
- **Abbreviate numbers consistently**: Use standard, localized abbreviations for large values (e.g., "10k" vs "10,000") only when space is strictly constrained.

### Errors and recovery

- **Treat errors as normal**: Expected states, not exceptions.
- **Structure: What to do → Why it happened**: Solution before explanation.
- **Never blame**: Describe the state, not the user's failure.
- **Show the exit**: Every error tells the user exactly how to proceed.
- **No false certainty**: Do not promise timeframes unless the system knows.
- **Use user-language**: "Check your network and retry." not "API unreachable" unless that term is domain-standard.

### Empty states

- **Explain why it is empty**: Context for the absence.
- **Make the next action obvious**: Path forward, not just void.

### Confirmations and modals

- **The modal three-point check**: Ensure the title, body, and button work as a single coherent conversation:
  - _Title:_ States the exact action or a direct question (e.g., "Delete 5 users?").
  - _Body:_ Explicitly shows the consequences and reversibility (e.g., "This action cannot be undone. They will lose access immediately.").
  - _Action button:_ Directly answers the title. Reuse Cancel for backing out. Do not invent OK, Yes, or Confirm when the title already named the action.
- **Confirm outcome, do not celebrate**: "Project saved" not "Great, you're all set!" No exclamation marks, no "please", no "successfully".
- **Guard only the irreversible**: A record that goes to Trash and can be restored needs no confirmation; a toast with Undo does the job.
- **Describe current state clearly**: Status text should reflect what is happening now.

### Accessibility (A11y)

- **Do not rely on visual-only cues**: Never direct users using color, shape, or position (e.g., do not write "Click the green button below").
- **Descriptive link text**: Avoid vague links like "Click here" or "Learn more". Describe the target (e.g., "Read the integration guide").
- **Provide text alternatives for icon buttons**: Every icon-only action must feature an explicit, descriptive `aria-label` (e.g., `aria-label="Edit template"`). Universal icons (back arrow, close) keep the `aria-label` but get no tooltip.

## Translation and localization

Translate for natural fluency, not literal accuracy. Prioritize meaning and tone over word order. Use standard professional terminology in the target language, even when it differs from English. Adapt to locale specifics. Keep translations concise, but allow extra words when needed for clarity.

## Technical

- Keep parallel actions and labels similar in length and structure across languages without making phrasing awkward.
- Always preserve meaning, action order, severity, and formatting (placeholders, variables, plurals, punctuation).
- Preserve the correct JSON structure of translation files.
- Keep existing translation keys, namespaces, nesting, and codebase patterns unless explicitly asked to change them.
- Prefer stable, descriptive, reusable keys when proposing new ones.

## Priority when phrasings compete

1. Reuse an existing label
2. Clarity
3. Consistency
4. Brevity
5. Tone
