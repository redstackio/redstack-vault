---
tags:
  - http-server
  - poc-hosting
  - cors-bypass
type: procedure
tools:
  - '[[tools/Python-Built-in-HTTP-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-python-http-server]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:25:53.228Z'
sub_techniques: []
id: 877c2d45-d195-4067-9089-febbd401e2ff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Start-Local-HTTP-Server-for-PoC-Hosting

## Summary

This procedure starts a local Python HTTP server to host a proof-of-concept (PoC) HTML file, enabling browser access without triggering CORS restrictions that would occur when opening local files directly.

## Description

In web-based attacks involving client-side PoCs, browsers enforce CORS policies that prevent local HTML files from connecting to remote endpoints. By hosting the PoC on a local server, it simulates a remote origin, allowing the WebSocket connection to the target GraphQL endpoint. This is essential for executing the introspection query without authentication barriers. The procedure assumes Python 3 is installed and the PoC file (e.g., ws.html) is in the current directory.

## Requirements

1. Python 3 installation on the attacker's machine
2. PoC HTML file in the working directory
3. Network access to the target (no special privileges needed)

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected local HTTP servers on developer machines
- Enforce CORS policies strictly on all endpoints
- Log and alert on WebSocket connections from unusual origins

## Objectives

1. Host the PoC file locally to evade CORS
2. Provide a stable origin for browser-based WebSocket initiation
3. Enable seamless execution of the subsequent introspection step

## Instructions

### Step 1: Prepare Directory

**Context**: Ensure the PoC HTML file is ready in the current directory to be served.

No command needed; verify ws.html exists.

### Step 2: Start the HTTP Server

**Context**: Launch the Python module to serve files on port 8000, allowing browser access to http://localhost:8000/ws.html.

**Command** ([[commands/start-python-http-server]]):
```bash
python3 -m http.server
```

> This command runs the http.server module as a script, binding to all interfaces on port 8000 by default. Expected output includes the serving message; the server runs until interrupted (Ctrl+C).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Python

### Sub-Techniques


## Commands Used

- [[commands/start-python-http-server]]

## Tools Used

- [[tools/Python-Built-in-HTTP-Server]]

## Tags

- http-server
- poc-hosting
- cors-bypass
