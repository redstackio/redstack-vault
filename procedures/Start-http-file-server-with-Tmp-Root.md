---
id: proc-start-http-file-server
tags:
  - server-startup
  - node-js
  - vulnerable-service
type: procedure
tools:
  - '[[tools/http-file-server]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/start-http-file-server-with-tmp-root]]'
verified: false
platforms:
  - Web
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.589Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-http-file-server-with-Tmp-Root

## Summary

This procedure starts the http-file-server module serving files from the /tmp/ directory, binding to all host interfaces on port 1234, creating a vulnerable endpoint for path traversal exploitation.

## Description

By launching the server with /tmp/ as the root path, attackers can test directory traversal by appending '../' to URLs, accessing parent directories. The server listens on all interfaces, making it accessible remotely. This setup replicates the vulnerable configuration in Node.js environments, potentially exposing system files if exploited.

## Requirements

1. http-file-server 0.2.6 installed globally
2. Access to /tmp/ directory on the host system
3. Port 1234 available and not firewalled
4. Node.js execution environment with script permissions

## Defense

Defensive measures and detection strategies:

- Input validation on URL paths to block '../' sequences
- Run servers in chroot or containerized environments to limit file access
- Monitor for unusual port bindings and server startups via process auditing tools like auditd

## Objectives

1. Initialize the vulnerable server for testing
2. Confirm listening on specified port and host
3. Enable HTTP access to /tmp/ for baseline verification

## Instructions

### Step 1: Launch the Server Script

**Context**: Run the server.js script with parameters to set the web root to /tmp/, host to all interfaces, and port to 1234.

**Command** ([[commands/start-http-file-server-with-tmp-root]]):
```bash
./http-file-server.js --path=/tmp/ --host=* --port=1234
```

> This starts the server. Expected output: "http-file-server listening on *:1234". Test by curling http://localhost:1234/ to list /tmp/ files.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/start-http-file-server-with-tmp-root]]

## Tools Used

- [[tools/http-file-server]]

## Tags

- [[server-startup]]
- [[node-js]]
