---
tags:
  - server
  - node.js
type: procedure
tools:
  - '[[tools/buttle]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/buttle-run-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.846Z'
sub_techniques: []
id: fd1a078c-d50e-4231-96a8-bc2df3b49e08
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Buttle-Server

## Summary

This procedure starts the buttle static file server on port 8080, enabling the directory listing that renders the injected HTML and triggers XSS.

## Description

Buttle uses connect's directory middleware to generate HTML listings from filenames. The unsanitized output allows the malicious filename to inject the iframe, which loads the payload. Running the server exposes this locally.

## Requirements

1. Buttle installed
2. Malicious files created
3. Port 8080 free

## Defense

Defensive measures and detection strategies:

- Update to sanitized middleware or disable listings
- Firewall local ports
- Log server startups and monitor for anomalies

## Objectives

1. Host files for access
2. Render vulnerable directory listing
3. Facilitate XSS trigger

## Instructions

### Step 1: Execute Server Binary

**Context**: Launch buttle to serve the current directory on specified port.

**Command** ([[commands/buttle-run-server]]):
```bash
./node_modules/buttle/bin/buttle -p 8080
```

> The -p flag sets the port. Expected output: "Listening on port 8080" and server readiness.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/buttle-run-server]]

## Tools Used

- [[tools/buttle]]

## Tags

- server
- node.js
