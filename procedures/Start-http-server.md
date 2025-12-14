---
tags:
  - server-start
  - http-server
  - vulnerable-service
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/http-server-start]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.803Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1d2c2b83-c40d-443a-9eab-27d7e5a22d96
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-http-server

## Summary

This procedure launches the http_server in the current directory to serve files on localhost:8888, exposing the directory listing with unsanitized malicious filenames for XSS exploitation.

## Description

The http_server module starts a static file server without filename validation, rendering directory contents in raw HTML. In this scenario, it serves the prepared directory, allowing payloads to be injected into the client's browser. Target environment is local Node.js; outcomes include an active server vulnerable to stored XSS upon access.

## Requirements

1. http_server module installed globally
2. Current directory contains malicious files
3. Port 8888 free

## Defense

Defensive measures and detection strategies:

- Disable directory listings or use sanitized templates
- Run servers in isolated environments
- Log server startups and monitor for anomalous ports

## Objectives

1. Expose the vulnerable directory listing
2. Start serving on default port
3. Confirm server readiness

## Instructions

### Step 1: Launch Server

**Context**: Execute the http_server command from the directory with malicious files to begin serving.

**Command** ([[commands/http-server-start]]):
```bash
http_server
```

> Starts the server; expected output: "server running is :http://localhost:8888". Keep the terminal open to maintain the server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-server-start]]

## Tools Used

- [[tools/npm]]

## Tags

- service-exposure
