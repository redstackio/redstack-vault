---
id: proc-uuid-4
name: Start flsaba Server
tags:
  - server-setup
  - exposure
type: procedure
tools:
  - '[[tools/flsaba]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/flsaba-start]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.357Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Start flsaba Server

## Summary

This procedure launches the flsaba HTTP server in the current directory, serving files and listings that expose the stored XSS payloads without sanitization.

## Description

Fl saba listens on port 3000 by default and generates HTML directory listings by directly inserting names into <a> tags, vulnerable at server.js lines 58 (href) and 64 (text). This step activates the server for payload triggering.

## Requirements

1. Fl saba installed globally
2. Port 3000 free
3. Current directory contains malicious files/directories

## Defense

Defensive measures and detection strategies:

- Firewall rules to block unexpected HTTP servers on port 3000
- Process monitoring for flsaba or similar unknown binaries
- Network IDS to detect local HTTP traffic

## Objectives

1. Expose directory listing via HTTP
2. Ensure payloads are served unsanitized
3. Confirm server stability

## Instructions

### Step 1: Launch Server

**Context**: Run flsaba to start serving; it defaults to current dir and port 3000.

**Command** ([[commands/flsaba-start]]):
```bash
flsaba
```

> Expected output: "flsaba v1.1.0 server listening on port 3000 Directory: /path/to/current/dir". Server runs in foreground.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/flsaba-start]]

## Tools Used

- [[tools/flsaba]]

## Tags

- server-setup
- exposure

