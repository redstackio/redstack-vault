---
tags:
  - xss
  - server
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-statics-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.211Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 492eba7d-5447-4bea-862d-cd411ad5c136
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Statics-Server

## Summary

This procedure starts the statics-server on localhost:8080, serving the current directory and generating the vulnerable HTML index listing.

## Description

Executing the server's index.js script activates the module, which uses unescaped template literals (lines 6-11) to build <a> and <li> elements with filenames, enabling the XSS injection when the directory is accessed.

## Requirements

1. Statics-server installed via npm
2. Node.js executable in PATH
3. Port 8080 available

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments or containers
- Monitor for unexpected server startups on non-standard ports
- Patch or replace vulnerable modules with secure alternatives

## Objectives

1. Start the server to expose the directory listing
2. Enable HTTP access for exploitation
3. Confirm server readiness for browser access

## Instructions

### Step 1: Execute Server Script

**Context**: Run the index.js to launch the static file server.

**Command** ([[commands/run-statics-server]]):
```bash
./node_modules/statics-server/index.js
```

> This starts the server on port 8080. Expected output: "服务器已经启动 访问localhost:8080".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/run-statics-server]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- server
