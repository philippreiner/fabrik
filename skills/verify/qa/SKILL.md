---
name: qa
description: "Check a change the way its user meets it, once before handover: screens, flows, interface strings, and click dummies. Use when the quality gate asks for it, when a user sees the change, or when asked. Code correctness is review-change."
---

# QA

QA asks whether this is the best version for the person who uses it, before the user has to ask whether you looked. Run it after the last edit to what the user sees, once.

## 1. See it

- Open each screen whose layout or content changed, in the running app or the click dummy, with realistic data. Screenshot it in the state the change touches; leave unchanged screens and states alone.
- Put each screenshot beside its baseline: the same screen on production or `main` for a shipped screen, otherwise the click dummy or the user's screenshot. Anything that worked there and is gone or worse now is a regression; restore it or name it on the Simplification ladder (`review-change`).
- Give every feedback point from this session a line: what changed it, or why it stays.

Done when each changed screen has its screenshot beside its baseline and every feedback point its line.

## 2. Ask

Run the `redline` skill's Review lenses on the screenshots, then answer each question in a line per screen:

- Can a first-time user say what it is for and the next step, in one sentence? If not, run `vernunft`.
- Does every word, control, and manual step earn its place? A tagline, helper, or second label the screen needs is a layout to fix.
- Does it work where and how someone used to the tools named in `PRODUCT.md` expects?
- For AI output, read the raw input beside the output: right, short, and traceable to its source?
- What would the best version of this feature do, and what is the smallest step toward it inside this change?

Done when every question has its answer.

## 3. Go deeper where the change calls for it

| Change | Add |
| --- | --- |
| A tweak to a part or region | The `redline` skill's quick path on the region, before and after |
| A new screen or click dummy | A fresh `tester` with only the screenshots and the user's goal; empty, one, many, the longest language, loading, and failed, plus the dark theme once |
| A new or substantially changed flow | One or two `tester` agents, one charter each (below) |
| A new list, table, card, or detail of user or AI data | `break-ui` |
| New or changed strings | `microcopy`, every language included |

A tester charter names the persona (role, context, familiarity), the goal in the persona's words, the start (URL, seeded account and role, viewport, default 1440x900), the data and allowed changes, a budget of about 60 browser actions, and the output path `.context/user-testing/<run>/<id>.md`. Give task facts, never the desired UI, permission verdicts, or known issues. Use seeded local accounts and data only (`docs/development/setup.md`). Keep the tested revision stable while testers run. Merge findings by job impact: blocks, hurts, nit; repeats add confidence, not severity.

## The browser

- `agent-browser --session <name> <command>` drives the browser; save screenshots under `.context/shots/`. Run `agent-browser skills get core` once for the command set. After a page-changing action, wait for the expected element, text, or URL.
- Reuse this worktree's dev server; `docs/development/setup.md` says how to find its URL. A server started with `run_in_background` dies at the task time limit, so when none answers, ask the user to start it.
- Take refs from one snapshot and script the flow with stable selectors. Before clicking, `scrollintoview` the target; an offscreen click can report success. Verify the URL, expanded state, or persisted value before calling an unchanged screen a defect.
- Stop at accounts, connected sources, credentials, or consent you do not have: verify the reachable parts and hand the rest to the user as unverified. Close the session with `agent-browser close` when done.

## 4. Fix and report

Fix what fails in one round and screenshot only what the fix changed. In the handover, embed the one or two screenshots that show the change beside their baseline, with the URL of the running app. Then the feedback lines, what QA changed, and what it left with the reason. E2E runs only when asked.
