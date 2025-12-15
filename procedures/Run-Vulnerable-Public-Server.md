---
id: proc-uuid-2
tags:
  - path-traversal
  - node-js
  - server-launch
type: procedure
tools:
  - '[[tools/public-module]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-public-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:11.801Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Vulnerable-Public-Server

## Summary

This procedure launches a static file server using the vulnerable 'public' Node.js module on port 8080, exposing the path traversal vulnerability for exploitation.

## Description

After installation, the module's bin/public script is executed to start serving files from the specified base directory (current directory './'). The server listens on localhost:8080 without path sanitization, directly joining the requested pathname with the base dir using path.join and reading files via fs.readFile. This setup on Linux with Node.js allows immediate exploitation. Prerequisites include the installed module and an available port.

## Requirements

1. Installed 'public' module in node_modules
2. Node.js runtime environment
3. Port 8080 free on localhost

## Defense

Defensive measures and detection strategies:

- Run servers in isolated containers or VMs
- Use firewalls to restrict port 8080 access
- Audit running processes for unexpected Node.js servers

## Objectives

1. Start the vulnerable server to host static files
2. Confirm the server is listening and responsive
3. Prepare for path traversal requests

## Instructions

### Step 1: Launch the Server

**Context**: Execute the binary to initialize the HTTP server serving the current directory.

**Command** ([[commands/run-public-server]]):
```bash
./node_modules/public/bin/public ./ 8080
```

> This runs the script, binding to port 8080 and serving './' as root. Expected output: 'Public.js server running with './' on port 8080'. The server will handle GET requests without traversal checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/run-public-server]]

## Tools Used

- [[tools/public-module]]

## Tags

- path-traversal
- node-js
