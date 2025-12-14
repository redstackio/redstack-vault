---
tags:
  - server-launch
  - web-server
type: procedure
tools:
  - '[[tools/takeapeek]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/takeapeek-launch]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.249Z'
sub_techniques: []
id: 398c7aa3-9d3c-41fc-838c-01001fd1fbce
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Launch-takeapeek-Server

## Summary

This procedure starts the takeapeek static web server in the current directory, exposing the directory listing with the malicious filename to enable XSS exploitation.

## Description

The takeapeek server listens on port 3141 by default and generates an HTML directory listing without sanitizing filenames, allowing the javascript: payload to become an executable hyperlink. This simulates a scenario where an attacker controls file creation on a shared server. Expected outcome: server ready for browser access.

## Requirements

1. takeapeek installed globally
2. Port 3141 free on localhost
3. Directory containing the malicious file

## Defense

Defensive measures and detection strategies:

- Disable directory listings in web servers or use sanitized views
- Run servers with least privilege and monitor for unexpected launches
- Firewall rules to restrict port 3141 exposure

## Objectives

1. Expose vulnerable directory listing
2. Serve malicious file links
3. Facilitate user interaction for XSS

## Instructions

### Step 1: Start the Server

**Context**: Execute the takeapeek command from the directory with the payload file to begin serving content.

**Command** ([[commands/takeapeek-launch]]):
```bash
takeapeek
```

> No parameters needed; server starts immediately. Expected output: confirmation of listening on http://localhost:3141.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/takeapeek-launch]]

## Tools Used

- [[tools/takeapeek]]

## Tags

- server-launch
- web-server
