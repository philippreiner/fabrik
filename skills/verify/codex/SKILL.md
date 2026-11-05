---
name: codex
description: "Run a job on the other vendor's model through its CLI, read-only: a code or deep review, a goal review, a second opinion, or a parallel exploration. From Claude this runs Codex; from Codex it runs Claude. Use before handover of a new feature, data model, permission, or durable work, for a goal review on long runs, or when asked."
---

# Codex

A model from another vendor has other blind spots. It sees only what you hand
it, so the brief carries everything.

## 1. Brief

Write `.context/codex-<job>-<yyyymmdd-hhmm>.md`: the outcome in the user's own
words, the base ref and diff scope (name untracked files), the plan path if
any, the shipped baseline to compare with (a URL or screenshots), constraints,
and the question. Leave out your conclusions; the other model should not
confirm them.

## 2. Run

Pick the job:

| Job | Model, effort | Instruction |
| --- | --- | --- |
| Deep review | `gpt-6-astra`, `medium` | Review the change in the brief with `.agents/skills/review-change/references/deep-review.md`. |
| Code review | `gpt-6.1-sol`, `high` | Review implementation with `.agents/skills/review-change/SKILL.md`; use Deep review for concepts, data models, permissions, or durable work. |
| Goal review | `gpt-6-astra`, `high` | Check the brief's outcome against the worktree: what is done and proven, what is missing, what regressed against the baseline, and what goes beyond the ask. Verify by reading code and running read-only commands. |
| Second opinion | `gpt-6-astra`, `high` | The open question, answered from first principles with two or three options and a pick. |
| Explore | `gpt-6-luna`, `low` | Answer the question with paths and one line each. |

One run may cover both design and completion; include both questions in the
brief. Run from the repository root using the harness's background process
support, and continue independent work:

```bash
codex exec -m <model> -c model_reasoning_effort=<effort> -s read-only \
  -o .context/codex-<job>-<stamp>.out "<instruction> The brief is on stdin." \
  < .context/codex-<job>-<stamp>.md
```

One process per job: a slow run is no reason to start another.

From Codex, run Claude the same way (it needs network, so run outside the
sandbox):

```bash
claude -p --model claude-opus-5-5 --effort high --permission-mode dontAsk \
  --allowedTools "Read,Grep,Glob,Bash(git diff *),Bash(git log *),Bash(git show *),Bash(git status *),Bash(rg *),Bash(ls *)" \
  "<instruction> The brief is on stdin." < <brief> > <out>
```

## 3. Use the answer

Read the `.out` file. Treat each finding as a claim: keep it when its trigger
and outcome hold in the code, reject it in one line when they do not. Score
what holds with the `review-change` Report rule, including its severity override.
For implementation work, fix in-scope findings that meet that policy; for
review-only requests, report without editing. Name the job, model, and verdict
in the handover.
