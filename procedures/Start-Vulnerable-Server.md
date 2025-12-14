---
id: proc-uuid-3456-7890
tags:
  - node-js
  - server-start
  - vulnerability-repro
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-test-script]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:05.739Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start-Vulnerable-Server

## Summary

This procedure runs the test.js script to start a local HTTP server using the vulnerable deliver-or-else module, exposing the path traversal vulnerability on localhost.

## Description

Executing the script launches the server on 127.0.0.1:80, logging 'Starting server...'. The server handles requests via the module's deliver method, which does not properly sanitize paths, setting the stage for traversal exploits. Ensure no other process uses port 80.

## Requirements

1. test.js script created
2. deliver-or-else installed
3. Port 80 available

## Defense

Defensive measures and detection strategies:

- Run servers in containers with restricted file access
- Use firewalls to limit localhost exposure
- Log server startups and monitor for anomalous processes

## Objectives

1. Activate the vulnerable server
2. Confirm listening on correct port
3. Prepare for request testing

## Instructions

### Step 1: Run the Script

**Context**: Execute the Node.js script to initialize and start the HTTP server.

**Command** ([[commands/node-run-test-script]]):
```bash
node test.js
```

> This starts the server process. Expected output: 'Starting server...' and no errors; server remains running until stopped (Ctrl+C).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- [[JavaScript]] JavaScript

## Commands Used

- [[commands/node-run-test-script]]

## Tools Used

- [[tools/node]]

## Tags

- node-js
- server-start
