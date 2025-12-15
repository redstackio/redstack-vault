---
tags:
  - server-start
  - node.js
  - web
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-angular-http-server]]'
verified: false
platforms:
  - Linux
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:11.734Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 77c2e3b0-457d-4288-8ec8-45490a8572a3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-Vulnerable-HTTP-Server

## Summary

This procedure launches the angular-http-server on port 6060, exposing the path traversal vulnerability for exploitation.

## Description

Running the server script from the installed module starts a local HTTP server that serves files from the current directory but fails to normalize paths with //, allowing traversal. This targets Node.js environments on Linux. Expected outcome is the server listening and ready for requests.

## Requirements

1. angular-http-server installed
2. index.html present
3. Port 6060 free
4. Node.js executable in PATH

## Defense

Defensive measures and detection strategies:

- Input validation on URL paths to strip traversal sequences
- Use secure file serving libraries that normalize paths
- Monitor server logs for unusual path requests

## Objectives

1. Initialize the vulnerable server instance
2. Bind to localhost:6060 for local testing
3. Enable HTTP requests for exploitation

## Instructions

### Step 1: Execute Server Script

**Context**: Run the JavaScript server file with port specification.

**Command** ([[commands/start-angular-http-server]]):
```bash
./node_modules/angular-http-server/angular-http-server.js -p 6060
```

> This starts the server. Expected output: "Server running at http://127.0.0.1:6060". Keep the process running.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/start-angular-http-server]]

## Tools Used

- [[tools/node]]

## Tags

- server-start
- node.js
