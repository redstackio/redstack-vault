---
id: 123e4567-e89b-12d3-a456-426614174002
name: Start-hnzserver-Static-Server
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.469Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - node-js
  - server-start
  - static-server
commands:
  - '[[commands/hnzserver-start]]'
platforms:
  - Linux
  - Node.js
tools:
  - '[[tools/hnzserver]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Start-hnzserver-Static-Server

## Summary

This procedure launches the hnzserver static file server in a specified directory (e.g., ~/Desktop), binding to port 8888 and serving files from the current directory, which exposes the path traversal vulnerability for exploitation.

## Description

hnzserver v2.0.6 is a lightweight Node.js-based static file server that listens on localhost:8888 by default. When started, it serves files from the current working directory without proper path validation, allowing subsequent traversal attacks. This step is crucial in the attack chain for creating an exploitable instance. The target environment is a local Linux setup with the module installed. Expected outcomes include the server running and accessible, with console output confirming the bind address.

## Requirements

1. hnzserver module installed globally (v2.0.6)
2. Access to a directory like ~/Desktop for serving files
3. Available port 8888 on localhost
4. Node.js runtime

## Defense

Defensive measures and detection strategies:

- Run servers in isolated containers or VMs to limit file access
- Implement path normalization and sanitization in custom servers
- Monitor for unexpected server processes on non-standard ports like 8888

## Objectives

1. Initiate the vulnerable server instance
2. Confirm serving from a controlled directory
3. Prepare for path traversal exploitation

## Instructions

### Step 1: Launch the Server

**Context**: Execute the hnzserver command in the desired directory to start the static server, which will handle HTTP requests without sanitizing paths.

**Command** ([[commands/hnzserver-start]]):
```bash
hnzserver
```

> Running this in ~/Desktop starts the server serving files from there. Expected output: "server running is :http://localhost:8888". The server remains active until manually stopped (Ctrl+C). Test accessibility with a simple curl to http://127.0.0.1:8888.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/hnzserver-start]]

## Tools Used

- [[tools/hnzserver]]

## Tags

- node-js
- server-start
- static-server
