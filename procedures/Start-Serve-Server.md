---
tags:
  - server-start
  - static-hosting
type: procedure
tools:
  - '[[tools/serve]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/serve-start-server]]'
platforms:
  - Node.js
techniques:
  - '[[Windows Command Shell]]'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 86147bbd-f1dd-4a61-9137-ceec272dc380
created_at: '2025-12-14T03:15:41.892Z'
updated_at: '2025-12-14T03:15:41.892Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Start-Serve-Server

## Summary

This procedure launches the serve static file server on localhost port 3000, exposing directory listings vulnerable to stored XSS from unsanitized filenames.

## Description

The serve module's binary starts a simple HTTP server that lists directory contents in HTML without escaping special characters in filenames. This enables stored XSS when malicious files are present. The server runs in the current directory, making it ideal for testing local exploits. Ensure the installation from the previous procedure is complete.

## Requirements

1. Serve module installed
2. Port 3000 free
3. Current directory writable

## Defense

Defensive measures and detection strategies:

- Disable directory listings in production servers
- Use HTTPS and CSP headers to mitigate XSS
- Monitor for unexpected server processes on port 3000

## Objectives

1. Host the directory for access
2. Enable HTML rendering of file listings
3. Prepare for payload injection and triggering

## Instructions

### Step 1: Execute Serve Binary

**Context**: Start the server to begin listening for connections and serving files.

**Command** ([[commands/serve-start-server]]):
```bash
./node_modules/serve/bin/serve.js
```

> Runs the serve.js script, starting the server. Expected output: "Serving!" followed by the URL http://127.0.0.1:3000. Press Ctrl+C to stop.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/serve-start-server]]

## Tools Used

- [[tools/serve]]

## Tags

- server-start
- static-hosting
