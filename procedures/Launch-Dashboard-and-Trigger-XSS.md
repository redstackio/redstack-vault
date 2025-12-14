---
tags:
  - execution
  - xss-trigger
  - dashboard
type: procedure
tools:
  - '[[tools/atlasboard]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/atlasboard-start]]'
  - '[[commands/node-start-js]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:30.362Z'
sub_techniques: []
id: 21b5cc7d-8bfc-4d15-b1ed-4fbf10cd04af
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Launch-Dashboard-and-Trigger-XSS

## Summary

This procedure starts the Atlasboard server and accesses the configured dashboard to render JIRA issues, triggering the XSS payload in the 'blockers' widget and executing client-side JavaScript.

## Description

With the server running, the dashboard fetches JIRA data and uses the vulnerable widget to append summaries to the DOM, executing injected scripts. This leads to arbitrary code execution in the browser, such as alerts or data exfiltration. Requires prior setup and injection; outcome is confirmed payload execution.

## Requirements

1. Configured Atlasboard project with JIRA integration
2. Injected payload in a retrievable JIRA issue
3. Local port 3000 available
4. Browser for accessing localhost

## Defense

Defensive measures and detection strategies:

- Escape HTML in all DOM insertions (e.g., use textContent instead of append)
- Implement browser-based XSS filters or CSP headers
- Log and alert on unexpected script executions in dashboards

## Objectives

1. Host the dashboard locally
2. Load the vulnerable example1 view
3. Observe and confirm XSS execution

## Instructions

### Step 1: Start Atlasboard Server

**Context**: Launch the server to host the dashboard and fetch JIRA data.

**Command** ([[commands/atlasboard-start]]):
```bash
atlasboard start
```

> Starts the Node.js server, binding to localhost:3000. Expected output: Logs showing 'Server running on port 3000' and readiness.

### Step 2: Alternative Server Launch

**Context**: Fallback method using direct Node.js execution if CLI fails.

**Command** ([[commands/node-start-js]]):
```bash
node start.js
```

> Executes the entry script. Expected output: Similar server startup logs.

### Step 3: Access Dashboard and Trigger

**Context**: Visit the endpoint to render the widget and execute the payload.

**Command** (Browser Access):
Open 'http://localhost:3000/example1'.

> The page loads JIRA issues; the blockers widget appends the summary, firing the script. Expected output: Alert popup or network request to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/atlasboard-start]]
- [[commands/node-start-js]]

## Tools Used

- [[tools/atlasboard]]
- [[tools/node]]

## Tags

- [[Execution]]
- [[xss-trigger]]
- [[dashboard]]
