---
name: agent-browser
description: "Browser automation for web UI checks: navigation, clicking, form entry, and screenshots against the running development app. The user's own Chrome session belongs to claude-in-chrome."
allowed-tools: Bash(agent-browser:*), Bash(npx agent-browser:*)
hidden: true
---

# agent-browser

Fast browser automation CLI for AI agents. Chrome/Chromium via CDP with
accessibility-tree snapshots and compact `@eN` element refs.

Install: `npm i -g agent-browser && agent-browser install`

Local test credentials may be passed on the command line. Never paste production credentials.

## Start here

This file is a discovery stub, not the usage guide. Before running any
`agent-browser` command, load the actual workflow content from the CLI:

```bash
agent-browser skills get core             # workflows, common patterns, troubleshooting
```

The CLI supplies version-matched usage instructions. The repository policy below
sets the scope of verification.

## Bounded UI verification

Use a browser when the changed UI needs runtime or visual evidence. Small copy
or mechanical edits need only the smallest relevant check.

- Reuse the running development server. If needed, start it with the documented
  development command. Read the repository's local development docs for the URL,
  startup, and test-account guidance; use existing fixtures.
- Check the changed flow in one focused pass. Capture and inspect a screenshot
  when layout or visible state matters. A screenshot does not prove persistence
  or external-service behavior.
- Stop the affected check at unavailable accounts, connected services, external
  data, credentials, or consent. Verify the reachable parts, then give the user
  the remaining action and expected result. User verification is a valid handoff;
  mark it unverified until evidence arrives and end the turn rather than polling.
- Do not connect accounts, reset data, invent fixtures, or repeatedly retry setup
  just to finish this check. After a concrete in-scope fix, recheck only the
  affected behavior. Do not restart broad browser or screenshot cycles once
  sufficient evidence is available.

## Specialized skills

Load a specialized skill when the task falls outside browser web pages:

```bash
agent-browser skills get electron          # Electron desktop apps
agent-browser skills get slack             # Slack workspace automation
agent-browser skills get dogfood           # Exploratory testing and QA
agent-browser skills get vercel-sandbox    # agent-browser inside Vercel Sandbox
agent-browser skills get agentcore         # AWS Bedrock AgentCore cloud browsers
```

Run `agent-browser skills list` to see everything available on the installed version.

## Observability dashboard

The dashboard runs independently of browser sessions on port 4848 and can also be opened through a proxied or forwarded URL such as `https://dashboard.agent-browser.localhost`. Agents should stay on the dashboard origin: session tabs, status, and stream traffic are proxied internally, so session ports do not need to be exposed.
