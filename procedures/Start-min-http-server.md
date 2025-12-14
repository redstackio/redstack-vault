---
id: proc-uuid-1235
tags:
  - server-start
  - node-js
  - http-server
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/min-http-server-start]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:17.329Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start-min-http-server

## Summary

This procedure launches the min-http-server, creating a local HTTP server vulnerable to path traversal attacks, typically listening on port 8000.

## Description

min-http-server serves static files from the current directory without configuration. Due to improper path sanitization, it allows traversal attacks. This step exposes the vulnerability for exploitation. Target environment is local Node.js; outcomes include a running server ready for request testing.

## Requirements

1. min-http-server installed globally
2. Local directory with test files (optional)
3. Port 8000 available

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments or containers
- Monitor for unexpected server processes
- Use firewalls to restrict server access

## Objectives

1. Initiate the vulnerable HTTP service
2. Confirm server is listening on the expected port
3. Prepare for incoming exploitation requests

## Instructions

### Step 1: Launch the Server

**Context**: This starts the zero-configuration server, binding to localhost:8000 by default.

**Command** ([[commands/min-http-server-start]]):
```bash
min-http-server
```

> Expected output: "Server running at http://localhost:8000". The server will continue running until interrupted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/min-http-server-start]]

## Tools Used


## Tags

- server-start
- node-js
