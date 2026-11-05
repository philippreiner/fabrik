# Test-pruning campaign

Campaign mode prunes one subsystem's whole test surface in one PR: a package
or one domain module. The value bar, retention bar,
candidate evidence, and validation in [SKILL.md](SKILL.md) apply to every
lane. This file adds the order of work and the lessons of a full campaign.
Each step ends on its completion criterion; do not start the next step early.

## 1. Baseline

Record the subsystem's test and support line counts and every test file's
pass/fail state at a pinned `main` SHA. Keep baseline failures in their own
list: a failing baseline test may be a real product bug, not a stale test.

Done when every in-scope test file has a recorded baseline result.

## 2. Lanes and inventory

Split the surface into **lanes** along production owner boundaries, not file
prefixes, such as persistence, permissions, jobs, transport, shared helpers,
harness, and end-to-end specs. Include the subsystem's cases at shared
boundaries and its Playwright specs.

Done when every test file and end-to-end scenario the subsystem owns belongs to exactly
one lane.

## 3. Read-only ledger per lane

Give each lane to its own read-only agent (`explorer`). The agent reads every assigned test
in full, including parameter tables. It also reads the production owners and
their entry points, callers, history, and CI routing. Each test declaration
goes into a written **ledger** with one mark. An `it.each` is one declaration
unless its rows need different marks; then mark each row.

- `R`: retain, naming the contract and the bug it catches; a retained test that
  only moves to a better-named file stays `R` with the move noted;
- `F`: retain the contract but repair the assertion, such as a vacuous negative
  that passes when only one of several items is missing;
- `C`: consolidate, naming the owner that absorbs the assertion first: a sibling
  table case, a stronger boundary suite, or the shared owner in another package;
- `D`: delete, naming the proof that remains, or why no contract exists.

Judge a test by its assertions, not its name. A test named for releasing
a lease may assert the lease was _not_ cleared.

Done when every declaration in the lane has a mark and an evidence line.

## 4. Layer plan per lane

Treat the per-test ledger as input, not as the edit list. A second read-only
pass, starting from the ledger, looks for the redundant **layer**. Typical case:
several suites replay the same shared helper through one mocked collaborator,
around a stronger database or fake-network suite. Name the
**keeper** suite for each contract. Prefer the real boundary (the database with real
migrations and domain transitions, or a fake at the external boundary) over a
mocked collaborator. Correct any ledger errors this pass
finds.

Done when each lane plan names its retired files, its keeper per contract, the
assertions to carry into keepers, and the test-only production seams unlocked.

Present the layer plans to the user and wait for confirmation before cutover.
Confirmation covers the lanes the user names; rework a lane the user changes.

## 5. Cutover

Edit lane by lane. Serialize changes to shared harnesses and support files
through one owner. With each lane, remove the test-only production seams it
unlocks: injection parameters, getters, reset exports, and indirection layers.
Register moved suites in the package `test` script and Turbo (`turbo.json`). Put durable test-ownership
rules in the owning doc (the `review-change` verification reference or the module's
docs), drawn from mistakes this campaign actually found.

Done when every lane plan is applied and each lane's keepers pass.

## 6. Preservation review

Before claiming completion, have an independent `codex` code review per
boundary group compare deleted coverage against the keepers. They look for
contracts that lost their only proof. They also look for new assertions that
cannot fail, such as a rejection row the production code never reaches. Expect
real gaps and the occasional unreachable assertion.

For each restored contract, make one deliberate **mutation** of the production
owner and confirm the keeper goes red. Then restore the source byte for byte.

Done when every reported gap is restored or rejected with source evidence, and
every restored contract has a caught mutation.

## 7. Product defects

A baseline failure that survives into a keeper is a bug report. Once the user
confirms the fix, repair it at its owner as a separate commit, and prove it through the real user flow, with a
**control** run that reverts the fix and shows the old behavior. Record
unrelated product discrepancies you find as follow-ups instead of fixing them
in the campaign.

Done when each repaired defect has a failing control and a passing candidate
on the same harness.

## 8. Reconcile and hand off

Campaigns outlive many `main` commits. Merge `main` rather than rebasing a
long campaign. When `main` modified a file the campaign
deleted, keep the deletion. Port the new contract into the keeper instead, and
confirm every new regression `main` added still has a home. Rerun the whole
subsystem suite and repeat the browser proof on the merged head.

Hand off with the [SKILL.md](SKILL.md) report, plus:

- baseline and final test/support line counts, with production counted separately;
- lanes, retired layers, and keepers;
- preservation gaps found and their mutations;
- product defects with control and candidate proof.
