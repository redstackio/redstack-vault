---
tags:
  - server-start
  - node-js
  - http-server
type: procedure
tools:
  - '[[tools/glance]]'
  - '[[tools/nodejs]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/glance-start-server]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:16.686Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 26ae9bdc-ce60-484f-945c-21aececbcdf1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start-Glance-Static-File-Server

## Summary

This procedure launches the Glance static file server on port 8080, serving files from a specified directory and exposing the path traversal vulnerability for exploitation.

## Description

After installation, the Glance binary is executed with verbose logging and a directory to serve, starting an HTTP server. The vulnerability arises from no path sanitization, allowing traversal in requests. This is tested locally on Node.js, with outcomes including server logs and readiness for HTTP exploits. Prerequisites include the installed module and Node.js runtime.

## Requirements

1. Glance module installed via npm
2. Node.js environment
3. Specified directory (e.g., ./node_modules/) exists

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments or containers to limit file access
- Monitor for unusual server startups with tools like process monitoring

## Objectives

1. Initiate the vulnerable HTTP server
2. Confirm listening on port 8080
3. Log requests for verbose analysis

## Instructions

### Step 1: Launch Server

**Context**: Execute the Glance script to start serving files, enabling the path traversal attack surface.

**Command** ([[commands/glance-start-server]]):
```bash
./node_modules/glance/bin/glance.js --verbose --dir ./node_modules/
```

> This starts the server with verbose output, showing "glance serving node_modules/ on port 8080". Logs will capture all requests, including potential exploits.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/glance-start-server]]

## Tools Used

- [[tools/glance]]
- [[tools/nodejs]]

## Tags

- server-start
- http-server
