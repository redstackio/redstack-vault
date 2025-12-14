---
tags:
  - xss
  - server-start
  - node-js
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-server-script]]'
  - '[[commands/node-start-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:13.990Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: c1583c9c-758b-42f3-88e6-5de8921a0ad7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-tianma-static-Server

## Summary

This procedure launches the tianma-static Node.js module to serve static files from a directory containing the malicious filename, enabling the stored XSS to be delivered to accessing browsers.

## Description

The tianma-static module acts as a simple static file server. By requiring it in a Node.js script and calling its serve method, the server starts on a specified port (e.g., 3000) and lists files without sanitizing filenames. This renders the XSS payload when a directory is browsed. Target environment is a local Node.js setup; outcomes include the server exposing the vulnerability to any HTTP client. Prerequisites: Installed module and malicious file present.

## Requirements

1. Node.js runtime.
2. tianma-static@1.0.4 installed via npm.
3. Script file (server.js) in the project directory.

## Defense

Defensive measures and detection strategies:

- Update to a patched version of tianma-static or use a secure alternative like express with sanitization middleware.
- Run servers in isolated environments (e.g., containers) and monitor HTTP logs for anomalous requests.
- Implement input validation on file uploads or creations to block script tags in names.
- Use HTTPS and HSTS to prevent MITM, though not directly mitigating XSS here.

## Objectives

1. Expose the directory with malicious files via HTTP.
2. Enable unsanitized rendering of filenames.
3. Facilitate victim access leading to XSS execution.

## Instructions

### Step 1: Create Server Script

**Context**: Write a minimal Node.js script to initialize and start the tianma-static server.

**Command** ([[commands/create-server-script]]):
```bash
echo "const tianma = require('tianma-static');\ntianma.serve(__dirname, 3000);" > server.js
```

> This echo command writes the script. Expected output: server.js file created with the require and serve calls.

### Step 2: Launch the Server

**Context**: Execute the script to start serving files on port 3000.

**Command** ([[commands/node-start-server]]):
```bash
node server.js
```

> Runs the Node.js interpreter on server.js. Expected output: Server logs 'Listening on port 3000' or similar, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-server-script]]
- [[commands/node-start-server]]

## Tools Used


## Tags

- [[xss]]
- [[node-js]]
- [[static-server]]
