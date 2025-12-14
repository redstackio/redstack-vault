---
tags:
  - server-start
  - nodejs
type: procedure
tools:
  - '[[tools/nodejs]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/http-file-server-run]]'
  - '[[commands/nodejs-run-http-file-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:31.286Z'
sub_techniques: []
id: fc95bb6b-7a65-431a-93aa-b93581d52ff4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Run-http-file-server

## Summary

This procedure starts the http-file-server in a directory containing the malicious filename, exposing an unsanitized directory listing on localhost:8080 vulnerable to stored XSS.

## Description

The server generates HTML listings by directly inserting filenames without escaping, allowing the XSS payload to be rendered as executable JavaScript. Run from the target directory to serve local files, simulating a file-sharing scenario where victims access the listing.

## Requirements

1. http-file-server installed globally or locally
2. Node.js runtime
3. Port 8080 free
4. Current directory contains the malicious file

## Defense

Defensive measures and detection strategies:

- Run servers with input validation middleware
- Use WAF to block anomalous requests
- Monitor for unexpected Node.js processes on port 8080

## Objectives

1. Expose the directory listing publicly (localhost)
2. Load vulnerable HTML with injected payload
3. Enable browser access for exploitation

## Instructions

### Step 1: Start the Server

**Context**: Change to the directory with the malicious file and run the server command.

**Command** ([[commands/http-file-server-run]]):
```bash
cd ~/Desktop/
http-file-server
```

> Expected output: "http-file-server listening on http://localhost:8080". The server runs in the foreground; Ctrl+C to stop.

### Step 2: Alternative Direct Execution

**Context**: If global install fails, run the script directly with Node.js.

**Command** ([[commands/nodejs-run-http-file-server]]):
```bash
nodejs /usr/lib/node_modules/http-file-server/http-file-server.js
```

> Similar output to the global command, confirming the server is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-file-server-run]]
- [[commands/nodejs-run-http-file-server]]

## Tools Used

- [[tools/nodejs]]

## Tags

- server-start
- nodejs
