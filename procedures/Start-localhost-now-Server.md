---
tags:
  - server-setup
  - node-js
  - web-server
type: procedure
tools:
  - '[[tools/localhost-now]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/localhost-now-start-server]]'
verified: false
platforms:
  - Node.js
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:11.662Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0a868ea0-fb1f-4e76-8039-d774ffba3d7c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-localhost-now-Server

## Summary

This procedure starts a local web server using the vulnerable localhost-now module on port 5432, exposing the path traversal vulnerability for exploitation.

## Description

After installation, execute the localhost-now binary to bind a simple HTTP server to localhost:5432, serving files from the current directory. The vulnerability in lib/app.js allows path traversal attacks once running. This is typically done in a test environment on Linux with Node.js. Expected outcomes include the server listening and responding to basic requests.

## Requirements

1. localhost-now@1.0.2 installed via npm
2. Node.js runtime environment
3. Port 5432 available (no conflicts)
4. Working directory with accessible files

## Defense

Defensive measures and detection strategies:

- Firewall rules to block external access to local ports
- Use process monitoring to detect unexpected Node.js servers
- Patch or replace with secure alternatives like http-server

## Objectives

1. Initialize the vulnerable server instance
2. Confirm server is serving on specified port
3. Prepare for path traversal testing

## Instructions

### Step 1: Launch the Server

**Context**: Run the command to start the server, binding to port 5432 and serving current directory contents.

**Command** ([[commands/localhost-now-start-server]]):
```bash
localhost 5432
```

> This executes the module's entry point, starting an HTTP listener. Expected output: "Web Server started on localhost:5432". Test accessibility with `curl http://localhost:5432/` to see directory listing or index.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/localhost-now-start-server]]

## Tools Used

- [[tools/localhost-now]]

## Tags

- server-setup
- node-js
- web-server
