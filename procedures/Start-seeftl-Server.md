---
tags:
  - xss
  - server-start
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/seeftl-start-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.691Z'
sub_techniques: []
id: 47789810-085c-4f04-b233-856ac5564637
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-seeftl-Server

## Summary

This procedure starts the seeftl static file server in a directory containing the malicious filename, generating an HTML directory listing that renders the XSS payload without sanitization.

## Description

The seeftl server serves static files and automatically generates directory listings in HTML. Due to no encoding of filenames, the injected JavaScript becomes executable attributes in the <a> tags of the listing, storing the XSS for any viewer. The server binds to http://127.0.0.1:8000/ by default.

## Requirements

1. seeftl installed globally via npm
2. Current directory contains the malicious file
3. Port 8000 available

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments (e.g., containers)
- Implement content security policies (CSP) to block inline scripts
- Log and monitor server startups and file access

## Objectives

1. Expose the directory listing with embedded XSS
2. Serve the vulnerable HTML to clients
3. Enable arbitrary script execution on access

## Instructions

### Step 1: Launch the Server

**Context**: From the directory with the malicious file, start the server to begin serving content.

**Command** ([[commands/seeftl-start-server]]):
```bash
seeftl
```

> This command starts the HTTP server on port 8000. Expected output: "Running at http://127.0.0.1:8000/". The server runs until interrupted (Ctrl+C).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/seeftl-start-server]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- server-start
