---
id: proc-uuid-4
tags:
  - server-launch
  - nodejs
  - directory-serving
type: procedure
tools:
  - '[[tools/public-module]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-public-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:02.878Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Run-Public-Server

## Summary

This procedure starts the 'public' module's static file server on port 8000, serving the current directory with indexing enabled, which triggers the XSS when accessed.

## Description

The server binary at node_modules/public/bin/public handles requests and generates unsanitized HTML listings. Running it with ./ 8000 serves the local dir, exposing the malicious filename. Vulnerability at line 106 concatenates filenames directly. Expected: Server binds to localhost:8000, ready for browser access to execute payload.

## Requirements

1. Installed 'public' module from prior step
2. Port 8000 free
3. Execute permissions on bin/public
4. Malicious files in current directory

## Defense

Defensive measures and detection strategies:

- Firewall rules to block unnecessary ports like 8000
- Use secure alternatives like nginx with sanitization
- Log server startups and monitor for vulnerable binaries

## Objectives

1. Host directory to render vulnerable listing
2. Enable automatic XSS on index access
3. Simulate public exposure for impact demo

## Instructions

### Step 1: Launch the Server

**Context**: Execute the binary to start serving, binding to the specified port and directory.

**Command** ([[commands/run-public-server]]):
```bash
./node_modules/public/bin/public ./ 8000
```

> Outputs server startup message; keeps running until Ctrl+C. Verify with netstat or curl http://127.0.0.1:8000 to see listing HTML with injected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/run-public-server]]

## Tools Used

- [[tools/public-module]]

## Tags

- server-launch
- nodejs
