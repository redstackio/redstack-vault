---
id: proc-uuid-1
tags:
  - xss
  - setup
  - dummy-server
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/node-dummy-github-server]]'
  - '[[commands/sudo-node-dummy-server-example]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:19.884Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Dummy-GitHub-Server-for-Malicious-Labels

## Summary

This procedure sets up a local Node.js server mimicking GitHub's API to serve project labels with malicious color values containing JavaScript payloads, enabling the exploitation of GitLab's unsanitized import feature for stored XSS.

## Description

In the context of exploiting a stored XSS in GitLab, this step creates a controlled environment where label colors are set to arbitrary strings like 'javascript:alert(document.domain)', which GitLab imports without validation. The server responds to GitLab's import requests, providing the malicious data. Prerequisites include Node.js installed and a public IP for accessibility. Expected outcome: A running server ready for API import triggers, leading to XSS payload injection.

## Requirements

1. Node.js installed on a machine with public IP access
2. dummy-server.tar.gz extracted (from vulnerability report)
3. Port 80 or similar open (may require sudo)
4. Basic networking knowledge for IP/port configuration

## Defense

Defensive measures and detection strategies:

- Monitor for unusual Node.js processes on ports mimicking GitHub (e.g., 80/443)
- Network logs showing API calls to non-standard GitHub hostnames
- Block or scan for JavaScript in label color fields during imports

## Objectives

1. Host malicious GitHub-compatible API endpoint
2. Serve labels with XSS payloads in color attributes
3. Enable seamless import into GitLab without detection

## Instructions

### Step 1: Prepare and Run Dummy Server

**Context**: Decompress and start the Node.js server to mimic GitHub, serving malicious labels.

**Command** ([[commands/node-dummy-github-server]]):
```bash
node ./index.js YOUR_IP YOUR_PORT
```

> This command starts the server on the specified IP and port, loading mock data with malicious colors. Replace YOUR_IP with your public IP (e.g., 51.75.74.52) and YOUR_PORT with 80. Expected output: Console log "Server listening on port YOUR_PORT".

### Step 2: Run with Elevated Privileges if Needed

**Context**: For low ports like 80, use sudo to bind the server.

**Command** ([[commands/sudo-node-dummy-server-example]]):
```bash
sudo node index.js 51.75.74.52 80
```

> Example execution with specific IP/port. Expected output: Server bound to port 80 without permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/node-dummy-github-server]]
- [[commands/sudo-node-dummy-server-example]]

## Tools Used

- [[tools/Node.js]]

## Tags

- xss
- setup
- dummy-server
