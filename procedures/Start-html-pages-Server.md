---
id: proc-uuid-3
tags:
  - server
  - node-js
type: procedure
tools:
  - '[[tools/html-pages]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/html-pages-start-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:16:02.820Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
---
# Start-html-pages-Server

## Summary

This procedure launches the html-pages HTTP server, which serves files and generates vulnerable directory listings that reflect unsanitized directory names.

## Description

The server runs on a specified port (6060) and automatically lists directories in HTML without escaping, allowing the previously created malicious name to inject JavaScript. This step exposes the stored XSS to any browser accessing the root or encoded path.

## Requirements

1. html-pages installed
2. Malicious directory created
3. Port 6060 free

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments
- Use WAF to block XSS payloads in URLs
- Log server access and monitor for alert executions

## Objectives

1. Activate the vulnerable server
2. Enable directory listing exposure
3. Facilitate payload triggering

## Instructions

### Step 1: Launch the Server

**Context**: Execute the binary script to start the development server on port 6060.

**Command** ([[commands/html-pages-start-server]]):
```bash
./node_modules/html-pages/bin/index.js -p 6060
```

> Output shows server listening; keep the process running for access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques


### Sub-Techniques


## Commands Used

- [[commands/html-pages-start-server]]

## Tools Used

- [[tools/html-pages]]

## Tags

- server
- node-js
