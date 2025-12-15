---
id: proc-hangersteak-start-001
tags:
  - directory-traversal
  - node-js
  - execution
type: procedure
tools:
  - '[[tools/nodejs]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/nodejs-run-server]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:05.537Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-Hangersteak-Server

## Summary

This procedure launches the Node.js HTTP server using the hangersteak module, binding to port 3006 and exposing the directory traversal vulnerability to network requests.

## Description

Executing the index.js script starts a server that serves files from the current directory without path checks. It listens on 0.0.0.0:3006, allowing remote access. This step assumes the script is created and module installed. Outcomes include a ready-to-exploit server; monitor for port conflicts.

## Requirements

1. index.js script in current directory
2. hangersteak installed
3. Port 3006 available
4. Node.js executable in PATH

## Defense

Defensive measures and detection strategies:

- Firewall rules to restrict port 3006 access
- Process monitoring for nodejs instances with suspicious modules
- Log server startups and bind to localhost only

## Objectives

1. Initiate server runtime
2. Confirm listening state
3. Enable exploitation vector

## Instructions

### Step 1: Run the Server Script

**Context**: Use nodejs to execute index.js and start the HTTP server.

**Command** ([[commands/nodejs-run-server]]):
```bash
nodejs index.js
```

> This runs the script, outputting "Server running on port 3006". The process remains active; use Ctrl+C to stop. Expected output: Confirmation message, no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/nodejs-run-server]]

## Tools Used

- [[tools/nodejs]]

## Tags

- [[directory-traversal]]
- [[node-js]]
