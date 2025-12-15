---
tags:
  - node-js
  - server-start
  - local-host
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mdstart-server]]'
platforms:
  - Node.js
  - Linux
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: ea967ef8-7f6d-46fb-8dba-f1b4615fa6a5
created_at: '2025-12-14T17:26:05.906Z'
updated_at: '2025-12-14T17:26:05.906Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-md-fileserver-Server

## Summary

This procedure launches the md-fileserver local server on port 8080, exposing the path traversal vulnerability for exploitation in a controlled testing environment.

## Description

After installing the module, the mdstart command starts a Node.js-based HTTP server that serves files from the current directory but fails to validate paths, allowing traversal attacks. This is key to reproducing the vulnerability where requests like /etc/passwd bypass the root directory. The server runs on localhost:8080, making it accessible for local curl exploits. The scenario targets developers or testers inadvertently using this module.

## Requirements

1. md-fileserver installed globally via npm
2. Available port 8080 on localhost
3. Node.js runtime environment

## Defense

Defensive measures and detection strategies:

- Scan for and patch vulnerable Node.js modules using tools like Snyk or npm audit
- Monitor for unexpected server processes on non-standard ports like 8080
- Use firewalls to restrict local server access and log HTTP requests for anomalous paths

## Objectives

1. Initiate the vulnerable server process
2. Confirm it's listening on the expected endpoint
3. Prepare for path traversal testing

## Instructions

### Step 1: Launch the Server

**Context**: This step executes the mdstart command to bind the server to localhost:8080, starting the vulnerable endpoint.

**Command** ([[commands/mdstart-server]]):
```bash
mdstart
```

> The command runs the Node.js server without additional parameters. Expected output is a console message like "Server running at http://127.0.0.1:8080". Keep the terminal open as the server runs in the foreground; interrupt with Ctrl+C to stop.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/mdstart-server]]

## Tools Used


## Tags

- node-js
- server-launch
