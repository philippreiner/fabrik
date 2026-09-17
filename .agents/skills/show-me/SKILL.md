---
name: show-me
description: Improve shared understanding with a diagram, code-shape sketch, or focused HTML artifact. Use when structure or flow is the question and prose explains it worse.
---

# Show me

Pick the smallest visual that makes the current question easier to understand. Keep supporting prose brief and next to the visual.

- Logic or an algorithm: pseudocode.
- Runtime flow: a shallow call tree.
- UI composition: a component tree with relevant state and module boundaries.
- Ownership or file layout: a shallow file tree.
- Interaction or data flow: Mermaid.
- Changes to an existing shape: a focused diff.
- A mostly new shape, or a copyable target: the complete relevant block.

For example, a call tree can show where behavior belongs:

```text
submitForm
  createSession
    persistPrompt
    launchAgent
  navigateToSession
```

Keep only the calls, files, props, states, and relationships the question needs. Use real names from inspected code; label proposed shapes as proposals. One clear view is usually enough.

For a visual UI or comparison too dense for an inline diagram, create one self-contained HTML file in `.context/show-me-<topic>.html`, unless the user names another destination. Match the product's visual language when illustrating its UI. Use real labels and supplied data, or clearly marked examples.

Open HTML with an available browser or preview tool. On local macOS, `open` is an option; do not assume it exists elsewhere. Give the user a clickable artifact path. A throwaway explanation needs no persistence, application integration, or tests.
