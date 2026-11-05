# Worst-case catalog

Plausible values for a demanding customer account, grouped by what the surface renders. Use the rows that match your map and swap in the product's own objects. Emails and URLs use the reserved `.example` domain.

## People

| Value | Breaks |
| --- | --- |
| `Hans-Jürgen Schulze-Böing` | Hyphens and umlauts; wraps at the hyphen, initials logic |
| `Dr. Annegret Müller-Lüdenscheidt` | Title prefix; initials `DM`, sorting by last name |
| `Maximilian von Hohenzollern-Sigmaringen` | Lowercase particle and long compound; overflows one-line rows |
| `Jo` / `Ü` | Very short; empty name column, one-letter initials, tiny link target |
| `Özlem Çelik` | Leading accented capital; clipping under tight leading, sort order |
| _missing name_ | Only an email exists; the surface needs a fallback |
| _missing avatar_, avatar URL that 404s | Initials fallback and its size parity with real avatars |
| Suspended member, pending invitation, the current user | Status labels, "You", actions that should not apply |

## Emails and identifiers

| Value | Breaks |
| --- | --- |
| `hans-juergen.schulze-boeing@stadtwerke-rhein-ruhr-netzbetrieb.example` | No break opportunity; pushes siblings off the row |
| `einkauf.niederlassung-sindelfingen+rechnungen@maschinenbau-baden.example` | Plus-addressing; truncation hides the part that differs |
| `a@b.example` | Layout that assumed a long email looks empty |
| `PROJ-12847`, `SN-2026-00-4471-A/03` | Wide readable ids in fixed-width columns |
| `Rahmenvertrag_Wartung_Standort-Nord_Rev7_freigegeben.pdf` | File name; end truncation hides version and extension |
| A shared-drive URL with a 120-character path | Overflow, and end truncation hides the meaningful tail |

## Titles and generated text

| Value | Breaks |
| --- | --- |
| A four-level path `Firma › Standort Nord › Abteilung Instandhaltung › Linie 2` | Wraps in trees, crumb trails, and pickers |
| `Qualitätssicherungsverantwortlicher` | Single long compound; no space to break at |
| `Settings` in en, `Einstellungen` in de | The same label 30 to 40 percent longer in German |
| A 280-character comment with an attachment | Row height, clamp, the feed |
| A 2,000-word AI summary with headings, lists, and `**bold**` | Clamp in Rows, Markdown rendering in Detail, "show more" |
| An AI answer citing a source with a 60-character folder name | Citation layout, label truncation |
| Empty or whitespace-only title | Collapsed heading, zero-height row |
| `<script>alert(1)</script>`, `&amp;` | Must render as literal text |

## Numbers and time

| Value | Breaks |
| --- | --- |
| `0`, `1` | Zero states, plurals ("1 Items") |
| `1284`, `1000000` | Separators (`1.284` in de, `1,284` in en), badge width |
| `142 %`, `-3 %` | Meters and bars past their bounds |
| `null`, `NaN` | Rendered literally |
| Now, 12 days ago, 3 years ago, in 3 days | Relative time thresholds, future dates |
| `2026-12-31T23:30:00+01:00` | Shows as another day in UTC |
| A 14-hour duration, a 90-second one | Duration formatting |

## Collections

| Value | Breaks |
| --- | --- |
| 0, 1, and 1,000+ members | Empty state, "1 of 1", pickers that list every member |
| 0, 1, and 300 children on one object | Empty state, paging, feed summaries |
| Exactly one page, and one page plus one | Off-by-one in "Load more" and counts |
| Twelve tags on one object | Chip rows that wrap into a wall; needs `+9` overflow |
| Two objects with the same name in one parent | Lists where the title is the only distinguishing field |
| One item ten times larger than the others | Grid rows stretching to the tallest item |

## States

| Value | Breaks |
| --- | --- |
| Loading | Skeletons that differ from the final layout, content shift |
| API error | Missing error state or a raw `TypeError` |
| Partial data | Optional fields set on some rows only; misaligned columns |
| Every status at once | Badge widths vary in one list |
| No permission | Disabled actions; the row still lays out the same |
