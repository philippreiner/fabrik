---
name: microcopy
description: Write or review UI labels, button text, helper text, and error messages. Interface strings belong here; longer prose belongs to write-human.
---

Write calm, concrete interface text for the product's users. Make actions and
consequences clear. Flag confusing layout rather than compensating with more copy;
omit text that repeats a visible label or status.

## The Rules

### Naming things

- **Reuse existing labels first** — Search the UI and translation files for the same action or object. Use that label. In contextual sheets and forms, prefer shared actions such as Save, Create, and Cancel when the title already names the object. Invent a new phrase only when no existing label fits. Destructive and ambiguous actions stay explicit.
- **Use domain language** — If they say "project," you say "project." Do not invent synonyms.
- **Name by outcome, not mechanism** — "Export report" not "Run export job", unless an existing label already names the action.
- **Objects are nouns, actions are verbs** — Never mix them.
- **One state = one term** — Use standard terms consistently for recurring states like loading, saved, failed, archived, syncing, or unavailable.

### Writing labels and scanning

- **Use sentence case everywhere** — Capitalize only the first word and proper nouns (e.g., "Create project", not "Create Project").
- **Front-load the action or object** — Make labels easy to scan.
- **No decorative "eyebrows" or categorization tags** — Do not add a redundant label above a header (e.g., displaying "SETTINGS" as a small eyebrow above a "Profile Settings" header). If the context is clear, remove the metadata.
- **Ellipsis signals more input needed** — Continuation, not completion (e.g., "Export as...").
- **Match severity** — Destructive actions must be explicit ("Delete file"), not vague ("Confirm").
- **No decorative punctuation, no emojis, no trailing periods**
- **Parallel UI should feel parallel** — Similar labels should have similar structure and similar visual length.

### Progressive disclosure and minimizing copy

- **Nudge toward omission** — If the system can proceed without an explanation, write nothing. Every word added increases the cognitive load of scanning.
- **Do not state the obvious** — Avoid helper text that merely repeats the input label (e.g., an input labeled "Organization name" does not need helper text saying "Enter your organization's name").
- **Tooltips are for definition, not instruction** — Use tooltips to define technical terms or offer secondary context. If an instruction is critical to preventing an error, keep it on-screen and visible.
- **Keep instructions manageable** — When conditions are hard to follow, simplify or split the workflow rather than adding a block of helper text.

### Forms and input

- **Labels outside fields** — Never rely on placeholder text as the label.
- **Placeholders are examples** — Show format (e.g., "e.g., user@domain.com"), do not instruct.
- **Mark required only if most fields are not** — Otherwise mark optional ones.
- **One instruction per line** — Do not compound requirements.

### Data, formats, and precision

- **Be explicit with timeframes** — Prefer absolute dates and times (e.g., "Oct 24, 2026, 14:30") over relative ones ("2 days ago") if precision is required for auditing, logs, or compliance.
- **Align units with values** — Clarify units of measurement directly in the input label (e.g., "Timeout (ms)" or "Maximum size (MB)"), not in the placeholder text.
- **Abbreviate numbers consistently** — Use standard, localized abbreviations for large values (e.g., "10k" vs "10,000") only when space is strictly constrained.

### Errors and recovery

- **Treat errors as normal** — Expected states, not exceptions.
- **Structure: What to do → Why it happened** — Solution before explanation.
- **Never blame** — Describe the state, not the user's failure.
- **Show the exit** — Every error tells the user exactly how to proceed.
- **No false certainty** — Do not promise timeframes unless the system knows.
- **Use user-language** — "Check your network and retry." not "API unreachable" unless that term is domain-standard.

### Empty states

- **Explain why it is empty** — Context for the absence.
- **Make the next action obvious** — Path forward, not just void.

### Confirmations and modals

- **The modal three-point check** — Ensure the title, body, and button work as a single coherent conversation:
  - *Title:* States the exact action or a direct question (e.g., "Delete 5 users?").
  - *Body:* Explicitly shows the consequences and reversibility (e.g., "This action cannot be undone. They will lose access immediately.").
  - *Action button:* Directly answers the title. Reuse Cancel for backing out. Do not invent OK, Yes, or Confirm when the title already named the action.
- **Confirm outcome, do not celebrate** — "Project saved" not "Great, you're all set!"
- **Describe current state clearly** — Status text should reflect what is happening now.

### Accessibility (A11y)

- **Do not rely on visual-only cues** — Never direct users using color, shape, or position (e.g., do not write "Click the green button below").
- **Descriptive link text** — Avoid vague links like "Click here" or "Learn more". Describe the target (e.g., "Read the integration guide").
- **Provide text alternatives for icon buttons** — Every icon-only action must feature an explicit, descriptive `aria-label` (e.g., `aria-label="Edit template"`).

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
