---
name: break-ui
description: Break UI with worst-case data and fix what the task owns. Use once a new list, table, card, or detail surface that renders user or AI-generated data is built, or when asked.
---

# Break UI

Adapted from Emil Kowalski's [break-ui](https://github.com/emilkowalski/skills) (MIT).

Demo data is kind: names fit one line, counts need no separator, every optional field is set. Undo that one field at a time with the most demanding plausible customer account, then look at what breaks.

## Rules

- Plausible or schema-backed. Each value is something a real customer could produce, or the limit from the Zod schema, column, or API contract. No limit found is itself a finding: write "unbounded" and test long but believable.
- Change the data, not the component. Worst-case data enters at the boundary that already feeds the UI: the local seed, a test fixture, or props in a component test. Markup and CSS stay as shipped while you break them.
- One dataset, many failures. Spread breaks across the first rows as real data does: row 1 the long name, row 2 the long email, row 3 the missing avatar.

## 1. Map

List every value the surface renders with its source, type, limit, and whether it is optional. Include the values people forget: header counts, relative times, status text, data-driven button labels, tooltips, avatars, and the list length itself. Note where the form limit and the column limit disagree.

Done when every rendered value has a source and a limit or "unbounded".

## 2. Build the worst case

Pick values from [references/catalog.md](references/catalog.md). Shape the worst-case fixture exactly like the existing data, and cover the states one dataset cannot hold:

- Empty: zero items, no search results.
- One: a single item, every count at exactly 1.
- Many: the realistic upper bound, 1,000+ rows when the list is unpaginated.

## 3. Break it

Look once with `agent-browser` at the real container width and at 320px, in the longest supported language. Add the widest layout, 200% zoom, and the other theme only for a new page. Reason from the classes for the rest and mark those findings as inferred.

| What you see | Cause | Fix |
| --- | --- | --- |
| Avatar or icon squished into an oval | Flex child shrinking | `shrink-0` on every fixed-size box |
| Text overflows instead of wrapping or truncating | Flex or grid child keeps `min-width: auto` | `min-w-0` on the text column, `minmax(0,1fr)` in grid |
| Email or URL runs past the edge | No break opportunity in the string | `wrap-anywhere` on that element |
| Trailing menu or button pushed off or clipped | Middle content took the space | `min-w-0` on the middle, `shrink-0` on the action |
| Badge wraps onto two lines | Badge allowed to shrink | `whitespace-nowrap shrink-0`, and decide what yields instead |
| Avatar adrift beside a three-line name | `items-center` on rows of varying height | `items-start` once text can wrap |
| Heading breaks mid-word | `break-all` | `wrap-anywhere` |
| Umlaut dots on capitals clipped | Tight leading with `overflow-hidden` | Looser leading, or no clipping on text boxes |
| Wrong or missing initials | Local initials code | The shared avatar component, fixed there |
| Orphaned dash or empty line for a missing field | Placeholder rendered for an optional value | Omit the line, or reserve its height on purpose |
| "1 Items", "0 Item" | Hard-coded plural | ICU `plural` in the message catalog |
| `1284`, `NaN`, `undefined`, `1,284` in German | Raw number rendered | Locale number format; guard null |
| Numbers jitter on update, columns misalign | Proportional figures | `tabular-nums` |
| German label overflows its button or tab | Fixed width | Width from content with a `min-w-*` |
| Truncated text with no way to read it | `truncate` and nothing else | `title` or tooltip, and the full value in Detail |
| Raw `**text**`, `&amp;`, or a 40-line summary in a Row | Wrong rendering layer or no clamp | The Markdown renderer in Detail, plain clamped text in Rows |
| Scrolling 1,000 rows stutters | Every row rendered | Paging or virtualization; say which |
| Broken-image icon in an avatar | No error fallback | Fall back to initials; `object-cover` |

Truncate, wrap, or clamp per field:

- Wrap what identifies the object: names, and titles in Detail.
- Truncate at the end for secondary metadata whose start carries the meaning, with a way to read the full value.
- Truncate in the middle when items differ at the end: file names, emails sharing a long domain.
- Clamp (`line-clamp-2`) previews in cards and Rows so heights stay predictable.
- Show numbers, dates, and anything the user compares in full.

Done when every applicable catalog row is tried, every width and condition is checked, and every break has a cause and a fix.

## 4. Report, then fix

One row per break, worst first. Broken: content unreadable, action unreachable, or wrong data. Ugly: readable but visibly wrong. Fragile: fine now, one realistic step from breaking.

| # | Severity | Field | Worst-case value | What happens | Fix (`file:line`) |
| --- | --- | --- | --- | --- | --- |
| 1 | Broken | `email` | `hans-juergen.schulze-boeing@stadtwerke-…example` | Pushes the row menu off at 320px | `min-w-0` on text, `shrink-0` on menu |

Fix the breaks the current task owns with existing tokens and primitives, then re-check every state, the ordinary data too. List the rest, and each break with more than one right answer (wrap or truncate, paging or virtualization), as a decision with your recommendation. Name the worst cases that already held. Keep the fixture as the regression case for the next change to the surface.
