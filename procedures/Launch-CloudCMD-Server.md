---
id: proc-uuid-2
tags:
  - web-server
  - nodejs
type: procedure
tools:
  - '[[tools/cloudcmd]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cloudcmd-launch-server]]'
verified: false
platforms:
  - Node.js
  - Web
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:15:31.079Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Launch-CloudCMD-Server

## Summary

This procedure starts the CloudCMD web file manager server, exposing the vulnerable directory listing interface on port 8080 for XSS exploitation.

## Description

After installation, the CloudCMD binary is executed with the --root flag to set the current directory as the file system root. The server runs a web interface at http://127.0.0.1:8080, where filenames are rendered unsafely in HTML, allowing stored XSS. This step assumes the module is installed and requires no authentication.

## Requirements

1. CloudCMD installed via npm
2. Port 8080 free
3. Current directory permissions for file access
4. Node.js executable in PATH

## Defense

Defensive measures and detection strategies:

- Block unauthorized web servers on internal ports
- Use firewalls to restrict access to port 8080
- Monitor for unexpected Node.js processes
- Apply patches to CloudCMD or avoid using vulnerable versions

## Objectives

1. Host the vulnerable web interface
2. Enable directory listing access
3. Prepare for file creation and browsing

## Instructions

### Step 1: Execute the Binary

**Context**: Run the CloudCMD script to start the server with the current directory as root.

**Command** ([[commands/cloudcmd-launch-server]]):
```bash
./node_modules/cloudcmd/bin/cloudcmd.js --root .
```

> This launches the server, binding to localhost:8080. Expected output: 'CloudCmd v9.1.5 is started: http://127.0.0.1:8080' or similar startup confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/cloudcmd-launch-server]]

## Tools Used

- [[tools/cloudcmd]]

## Tags

- web-server
- nodejs
