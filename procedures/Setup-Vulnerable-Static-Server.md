---
tags:
  - node-js
  - server-setup
  - vulnerability
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:12.645Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d4e73412-baab-4011-bf3e-2d6536027a79
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Setup-Vulnerable-Static-Server

## Summary

This procedure configures a basic Node.js application using the vulnerable 'stattic' module to serve static files from the current directory on port 8080, exposing the path traversal vulnerability.

## Description

By importing 'stattic' and configuring it with folder './' and port 8080, the server is set up without any path sanitization. Requests to paths like '/../../../../../etc/hosts.deny' will resolve to arbitrary locations due to unchecked path.join usage. This is done by creating app.js, which can then be executed to start the server. The setup is straightforward but critical for demonstrating the flaw in a controlled environment.

## Requirements

1. Vulnerable stattic module installed
2. Text editor to create app.js
3. Node.js runtime

## Defense

Defensive measures and detection strategies:

- Implement path normalization and canonicalization in custom servers
- Use secure alternatives like Express with helmet middleware
- Scan source code for vulnerable patterns like unchecked path joins

## Objectives

1. Create a runnable server script with vulnerable configuration
2. Expose the static file serving endpoint
3. Prepare for execution and exploitation

## Instructions

### Step 1: Create app.js

**Context**: Write the server script to import and configure the stattic module.

**Command** (Manual file creation):
```javascript
const stattic = require('stattic');
const server = stattic({
  folder: './',
  port: 8080
});
server.listen(8080, () => {
  console.log('Server running on port 8080');
});
```

> Save this as app.js. No command execution here; verify by running `node -c app.js` for syntax check. Expected output: No errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/node]]

## Tags

- node-js
- server-setup
- vulnerability
