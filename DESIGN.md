# Design

- Use tokens from `[path to the design tokens]`.
- Use shared components from `[path to shared components]`.
- Use `[reference screen or layout]` for shells, layouts, and basic blocks.

## Character

- Design for `[feeling or job]`, not `[nearby but wrong product character]`.
- Aim for `[density, pace, or visual reference]`.
- `[Light/dark/responsive/accessibility direction]`.

Example: “Design a calm, precise work surface that makes the next action obvious.”

## Page structure

- Put the answer to the user's main question first.
- Give each page one primary action.
- Put actions next to the content they affect.
- State each fact once.
- Hide details until they are useful.
- Extend or replace an existing section. Do not add an unrelated box at the bottom.
- Design narrow-screen order intentionally; do not only stack every section.

## Compose

For a new page or flow:

- Name the feeling the user should have in one word before drawing.
- Draft three compositions that differ in kind, not only spacing. Pick with the user's main question.
- Give the page one memorable idea that serves its purpose.
- Remove redundant labels, containers, decoration, and custom components a shared one already does better.
- Critique the result before handover: what is overdone, generic, or hard to understand at first glance?

Example: “Relief. Make the blocked item and its next action the dominant element.”

## Layouts

Describe the layouts the product reuses:

- `[Layout name]`: `[when to use it and what owns scrolling, selection, and actions]`
- `[Layout name]`: `[when to use it and what owns scrolling, selection, and actions]`

Example: “List-detail: the list owns filtering and selection; the detail surface owns the selected record and its actions.”

## Visual rules

- Use `[color and token rule]`.
- Show importance with text weight, contrast, spacing, and borders before color.
- Do not rely on color alone.
- Use monospace only for machine values.
- Prefer borders to shadows; reserve shadows for content that floats.
- Use the product's date, time, and number format helpers.
- Meet WCAG AA contrast and keep keyboard focus visible.

## Components and behavior

- Keep shared component names unchanged. Give product-specific compositions a clear name.
- Use one control for the same action everywhere.
- Design loading, empty, error, partial, and complete states.
- Keep destructive actions quiet until confirmation and make reversibility explicit.
- Keep selection and navigation state in the URL when the framework supports it.
- Respect reduced-motion settings.
