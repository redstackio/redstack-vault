---
id: proc-uuid-002
tags:
  - node-js
  - server-start
type: procedure
tools:
  - '[[tools/statics-server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/statics-server-start]]'
verified: false
platforms:
  - Linux
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.385Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Run-Statics-Server-in-Directory

## Summary

This procedure starts the statics-server in a specific directory, serving files on localhost:8080 and exposing the vulnerability to symlink-based path traversal.

## Description

Once installed, running statics-server serves the current directory's contents without validating symlinks, allowing attackers to read files outside the root via crafted links. This targets Linux environments with Node.js.

## Requirements

1. Statics-server installed globally
2. Working directory with write permissions
3. Port 8080 free

## Defense

Defensive measures and detection strategies:

- Run servers in chrooted or containerized environments
- Monitor for unexpected Node.js processes on port 8080
- Use secure static servers like nginx with symlink restrictions

## Objectives

1. Expose the served directory to HTTP requests
2. Enable symlink exploitation
3. Prepare for file access testing

## Instructions

### Step 1: Launch the Server

**Context**: Start serving files from the current directory.

**Command** ([[commands/statics-server-start]]):
```bash
statics-server
```

> Executes the server, binding to localhost:8080. Expected output: '服务器已经启动 访问localhost:8080'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/statics-server-start]]

## Tools Used

- [[tools/statics-server]]

## Tags

- node-js
- server-start
