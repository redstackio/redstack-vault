---
id: proc-ponse-start-001
tags:
  - node-js
  - server-start
  - execution
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-ponse-server]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:06.641Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-Ponse-Server

## Summary

This procedure launches the Node.js server script configured with the vulnerable ponse module, making the path traversal endpoint available for exploitation.

## Description

Executing the index.js file starts an HTTP server on port 8080 using ponse for static file serving. The vulnerability is active once the server is running, as requests to the static endpoint will process paths without validation. This step is crucial for local reproduction before sending exploit requests.

## Requirements

1. index.js file created from previous procedure
2. ponse module installed
3. Port 8080 available on localhost

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments or containers to limit file access
- Monitor for unexpected server startups using process monitoring tools
- Use firewalls to restrict server exposure during testing

## Objectives

1. Activate the vulnerable server
2. Confirm it's listening and responsive
3. Enable subsequent exploitation steps

## Instructions

### Step 1: Execute Server Script

**Context**: Run the Node.js script to start the HTTP server.

**Command** ([[commands/start-ponse-server]]):
```bash
node index.js
```

> This launches the server, which will log 'Server listening on port 8080'. Expected output: Console message confirming the port, with the process running in the foreground.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/start-ponse-server]]

## Tools Used

- [[tools/node]]

## Tags

- node-js
- execution
