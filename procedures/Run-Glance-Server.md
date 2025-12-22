---
id: proc-uuid-3
tags:
  - xss
  - server-setup
  - node-js
type: procedure
tools:
  - '[[tools/glance]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-glance-server]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.960Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Glance-Server

## Summary

This procedure starts the Glance HTTP server in a directory containing a malicious file, exposing the unsanitized directory listing that renders the XSS payload.

## Description

Glance serves static files and generates HTML directory listings by directly embedding file names, allowing the stored XSS to activate. Run from the directory with the malicious file; the server defaults to port 3000. This step assumes prior installation and file creation.

## Requirements

1. Glance installed via npm
2. Malicious file in the current directory
3. Node.js executable permissions

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments or containers
- Implement content security policies (CSP) to block inline scripts
- Log and alert on unusual server startups

## Objectives

1. Start server without errors
2. Serve the directory on localhost:3000
3. Enable access to the vulnerable listing

## Instructions

### Step 1: Execute Server Binary

**Context**: Launch the Glance server with verbose logging and specify the directory to serve.

**Command** ([[commands/run-glance-server]]):
```bash
./node_modules/glance/bin/glance.js --verbose --dir ./
```

> This runs the server, outputting verbose logs including startup and requests. Expected output: "Glance server listening on port 3000".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/run-glance-server]]

## Tools Used

- [[tools/glance]]

## Tags

- xss
- http-server
- exposure
