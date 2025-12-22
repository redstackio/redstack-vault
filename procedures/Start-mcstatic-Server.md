---
tags:
  - path-traversal
  - node-js
  - server-start
type: procedure
tools:
  - '[[tools/mcstatic]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mcstatic-start-server]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 83814e47-0c68-456f-a9fa-0276bf2cfebe
created_at: '2025-12-14T17:26:16.799Z'
updated_at: '2025-12-14T17:26:16.799Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start-mcstatic-Server

## Summary

This procedure launches the mcstatic static HTTP server on a specified port, exposing the path traversal vulnerability in its file serving mechanism.

## Description

Once installed, the mcstatic module's binary is executed to start a simple HTTP server that serves static files. Due to lack of path normalization, requests with '../' sequences can traverse outside the intended directory. This step binds the server to localhost:6060, making it ready for exploitation in a local or remote setup.

## Requirements

1. mcstatic module installed via npm
2. Node.js executable permissions on the bin script
3. Available port (e.g., 6060) not in use

## Defense

Defensive measures and detection strategies:

- Run servers in isolated containers or VMs to limit file system access
- Use web application firewalls (WAF) to block traversal patterns like '../'
- Monitor process listings for unexpected Node.js servers on non-standard ports

## Objectives

1. Activate the vulnerable server component
2. Expose the HTTP endpoint for traversal attacks
3. Simulate a public-facing application for exploitation testing

## Instructions

### Step 1: Launch Server

**Context**: This runs the mcstatic binary, starting the server and listening for HTTP requests on the defined port.

**Command** ([[commands/mcstatic-start-server]]):
```bash
./node_modules/mcstatic/bin/mcstatic --port 6060
```

> The --port flag sets the listening port to 6060. Expected output is a message confirming the server is running, such as "mcstatic server started on port 6060". The process remains active until stopped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/mcstatic-start-server]]

## Tools Used

- [[tools/mcstatic]]

## Tags

- path-traversal
- server-start
