---
tags:
  - server-setup
  - node-js
  - web-server
type: procedure
tools:
  - '[[tools/serve-here]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/here-start-server]]'
verified: false
platforms:
  - Linux
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:11.896Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3e02dd71-cb2f-4c2f-bc7d-bb013f46d54c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-serve-here-Server

## Summary

This procedure starts the serve-here static web server from the current directory on port 8081, creating a vulnerable endpoint that serves files from the web root, such as /root, for path traversal exploitation.

## Description

The serve-here package runs a simple Node.js HTTP server to deliver static files. In version 3.2.0, it lacks proper path sanitization, allowing attackers to traverse directories. This step is performed after installation and directory setup. The target environment is a local Linux host, with the outcome being an active server ready for crafted requests to disclose files.

## Requirements

1. serve-here@3.2.0 installed via npm
2. Current directory set to the intended web root (e.g., /root)
3. Port 8081 free and firewall allowing local access

## Defense

Defensive measures and detection strategies:

- Restrict Node.js servers to non-privileged ports and bind to localhost only
- Use web application firewalls (WAF) to block traversal patterns like '../'
- Monitor for unexpected HTTP servers on non-standard ports like 8081

## Objectives

1. Launch the server to expose the web root
2. Bind to a specific port for controlled access
3. Confirm server is operational without errors

## Instructions

### Step 1: Launch Server

**Context**: Run the serve-here command to start serving files from the current directory on the specified port.

**Command** ([[commands/here-start-server]]):
```bash
here -p 8081
```

> The -p flag specifies the port. Expected output is a startup message like "Serving current directory on http://0.0.0.0:8081". The server runs in the foreground; use Ctrl+C to stop.

### Step 2: Verify Server Access

**Context**: Test basic access to confirm the server is responding from the web root.

**Command** ([[commands/curl-basic-test]]):
```bash
curl http://localhost:8081
```

> This fetches the index or directory listing. Expected output includes files from /root or a default page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/here-start-server]]
- [[commands/curl-basic-test]]

## Tools Used

- [[tools/serve-here]]
- [[tools/cURL]]

## Tags

- server-setup
- node-js
- web-server
