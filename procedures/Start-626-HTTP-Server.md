---
tags:
  - path-traversal
  - node-js
  - server-start
type: procedure
tools:
  - '[[tools/node-js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-626-server]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:12.212Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: c65e1412-b99e-4ddd-8a6e-1c9ef133e8ac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start-626-HTTP-Server

## Summary

This procedure launches the HTTP server from the vulnerable 626 Node.js module, exposing it on localhost:8080 for path traversal exploitation.

## Description

The index.js file in the 626 module starts a basic HTTP server using Node's http module, listening on port 8080. It resolves req.url directly with path.resolve without sanitization, enabling traversal. This targets a local or remote Node.js environment; prerequisites include the installed module. Expected outcome is the server running and accessible, vulnerable to crafted requests.

## Requirements

1. 626 module installed via npm
2. Node.js runtime (v8.9.3)
3. Port 8080 available (no conflicts)

## Defense

Defensive measures and detection strategies:

- Input validation on file paths in Node.js apps (e.g., path.normalize, basename checks)
- Run servers in isolated environments (containers) to limit file access
- Monitor process listings for unexpected Node.js servers on non-standard ports

## Objectives

1. Initialize the vulnerable server instance
2. Confirm listening state on port 8080
3. Enable HTTP endpoint for exploitation

## Instructions

### Step 1: Execute Server Script

**Context**: Run the index.js to start the HTTP listener, which serves files based on the URL path.

**Command** ([[commands/start-626-server]]):
```bash
./node_modules/626/index.js
```

> This launches the Node.js script, binding to port 8080. Expected output: 'Listening on 8080' message, with the process remaining active. Interrupt with Ctrl+C to stop.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/start-626-server]]

## Tools Used

- [[tools/node-js]]

## Tags

- path-traversal
- node-js
- execution
