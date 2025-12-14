---
tags:
  - xss
  - server-start
  - node-js
type: procedure
tools:
  - '[[tools/dy-server2]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/dy-server2-start-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.470Z'
sub_techniques: []
id: 9419059d-2b9c-4d9e-b248-eb523ccf5fca
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-dy-server2-Server

## Summary

This procedure launches the dy-server2 HTTP server on a specified port, serving the current directory including any malicious files or folders, which exposes the stored XSS vulnerability when accessed remotely or locally.

## Description

dy-server2 starts a simple web server that lists directory contents without sanitizing file or folder names, allowing XSS payloads to render as executable HTML/JS. In the attack, this step serves the malicious item created previously. Targets local or shared development setups. Expected outcome: Server listening on the port, ready for browser access to trigger exploitation.

## Requirements

1. dy-server2 installed globally
2. Port 8888 (or chosen) available and not in use
3. Current directory contains the malicious file/folder

## Defense

Defensive measures and detection strategies:

- Firewall rules to block unexpected HTTP servers on non-standard ports
- Monitor for processes running on ports like 8888 with tools like netstat
- Use audited alternatives to dy-server2, such as http-server with sanitization

## Objectives

1. Expose the directory with unsanitized listings
2. Enable HTTP access to trigger stored payloads
3. Facilitate victim interaction via browser

## Instructions

### Step 1: Launch Server

**Context**: Start the server from the directory with the malicious content, specifying the port to listen on.

**Command** ([[commands/dy-server2-start-server]]):
```bash
dy-server2 -p 8888
```

> The -p flag sets the port; server serves the current directory. Expected output: Message like 'Server listening on http://localhost:8888'.

### Step 2: Verify Server Status

**Context**: Ensure the server is running and accessible.

**Command** (Curl for test):
```bash
curl http://localhost:8888
```

> Fetches the directory listing. Expected output: HTML with file names, including the unescaped payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/dy-server2-start-server]]

## Tools Used

- [[tools/dy-server2]]

## Tags

- xss
- server-start
