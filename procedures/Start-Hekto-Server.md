---
id: proc-uuid-3
name: Start Hekto Server
tags:
  - server-launch
  - node-js
type: procedure
tools:
  - '[[tools/hekto]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/start-hekto-server]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:27.115Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start Hekto Server

## Summary

This procedure launches the hekto HTTP server to serve the current directory on port 3000, exposing the vulnerable redirection logic for testing.

## Description

After installing hekto and creating the trigger file, running the server binary activates the module's HTTP service. The server listens on localhost:3000 and handles requests, including the flawed redirect for paths starting with '//'. This step requires the node_modules path to be accessible. The expected outcome is a running server ready for incoming requests that can trigger the vulnerability.

## Requirements

1. Hekto module installed
2. Trigger file in current directory
3. Node.js runtime
4. Port 3000 available

## Defense

Defensive measures and detection strategies:

- Firewall rules to restrict server exposure to localhost only
- Validate and sanitize redirect URLs in server code
- Monitor for unexpected server startups in development environments

## Objectives

1. Expose the directory via HTTP
2. Activate vulnerable redirection handler
3. Prepare for request testing

## Instructions

### Step 1: Launch Server

**Context**: Execute the hekto binary with the serve command.

**Command** ([[commands/start-hekto-server]]):
```bash
./node_modules/hekto/bin/hekto.js serve
```

> Starts the server, outputting a message like 'Server listening on http://127.0.0.1:3000'. Keep the process running for testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/start-hekto-server]]

## Tools Used

- [[tools/hekto]]

## Tags

- server-launch
- node-js
