---
name: document-product
description: "Explain current user-facing product behavior or write behavior documentation. Short factual answers need no skill. Implementation specs belong to to-spec; engineering docs to documentation."
---

# Document product

Describe what the user sees, can do, and what happens next, including interruption and recovery where they matter. Use the product's words and current behavior.

## Scope

Answer a focused question directly in the conversation. Read only the relevant behavior; do not turn a short explanation into a full behavior specification.

For requested durable documentation, use the named destination and existing structure. If no destination is named, deliver in the conversation. For a whole system, establish a common vocabulary and outline, then document one representative feature before extending the pattern.

## Evidence

Read the relevant interaction handlers, domain state, tests, UI, and defaults. Use `PRODUCT.md` and the `CONTEXT.md` glossary for names. Inspect the running product where visibility or timing cannot be established from code. Tests are evidence, not a substitute for checking conflicting implementation.

Separate observed behavior, inference, and unresolved questions. Describe suspected defects as such. Do not smooth them into intended behavior or fix them during a documentation request. Record new repository terms under the scope rules in `AGENTS.md`; do not create a competing glossary.

## Comprehensive behavior documents

Use these sections when the user requests a full feature or system description. Reuse the same order across comparable features, and omit sections without a relevant interaction.

1. Summary and normal user path.
2. States and actions, including what is saved or sent and when.
3. Variants that change behavior, such as role, record state, or configuration.
4. Cancel, interruption, and recovery: navigating away, reload, network or session failure, and concurrent changes where applicable.
5. Interactions with permissions, other objects, history, and notifications that affect this feature.
6. Unconfirmed behavior and suspected defects.

Use a state diagram or comparison table when it makes these relationships clearer. Do not fill matrices with repeated “no effect” cells. Cover real failure paths and surprising behavior; do not invent variants to complete a template.

For a multi-document task, keep progress in the existing destination so another executor can continue. Cite the inspected commit in durable documents. Claim runtime verification only when performed; disclose what remains unverified.

Write direct prose with concrete actions and outcomes. Include implementation details only when they explain something the user would notice.
