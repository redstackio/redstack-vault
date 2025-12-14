---
id: proc-start-simplehttpserver
tags:
  - http-server
  - node-js
  - vulnerable-service
type: procedure
tools:
  - '[[tools/simplehttpserver]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/simplehttpserver-start]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.625Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Start simplehttpserver with Current Directory

## Summary

This procedure launches the vulnerable simplehttpserver module to serve the current directory as the web root over HTTP on port 8000, exposing the symlink setup to path traversal exploitation without any URL path validation.

## Description

The simplehttpserver directly concatenates URL paths to the web root, failing to resolve or restrict symlinks, which allows traversal attacks. In this attack scenario, the server is started locally after symlink creation and module installation, making the exploit accessible via a browser. Expected outcomes include the server running indefinitely until stopped, serving files including the malicious symlink. Prerequisites: Installed module and prepared directory.

## Requirements

1. simplehttpserver installed globally
2. Current directory contains the symlink (e.g., symdir)
3. Port 8000 available (no conflicts)
4. Localhost access

## Defense

Defensive measures and detection strategies:

- Avoid using unmaintained modules like simplehttpserver in production; opt for secure alternatives like nginx or Express with middleware
- Configure servers to deny symlink following and validate paths (e.g., using `realpath` in Node.js)
- Monitor for suspicious HTTP servers starting on non-standard ports via process monitoring (e.g., ps aux | grep node)
- Use web application firewalls (WAF) to block traversal patterns like '../'

## Objectives

1. Deploy the vulnerable HTTP server
2. Expose the web root including symlinks
3. Enable HTTP access for exploitation

## Instructions

### Step 1: Launch the Server

**Context**: This starts the server with './' as the root, appending URL paths without validation, allowing symlink resolution to parent directories.

**Command** ([[commands/simplehttpserver-start]]):
```bash
simplehttpserver ./
```

> The './' argument sets the current directory as web root. Expected output: 'Serving ./ on port 8000' or similar startup message. The server listens on localhost:8000; test accessibility with curl http://localhost:8000/ before proceeding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/simplehttpserver-start]]

## Tools Used

- [[tools/simplehttpserver]]

## Tags

- http-server
- vulnerable
