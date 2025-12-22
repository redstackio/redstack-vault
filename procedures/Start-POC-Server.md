---
tags:
  - launch
  - server
  - node-js
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/node-run-poc]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.578Z'
sub_techniques: []
id: 07abd9a6-6b62-4ed9-bb74-45bc9c3c2ea3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-POC-Server

## Summary

This procedure launches the proof-of-concept Express server to host the vulnerable IP whitelisting application locally on port 3000.

## Description

After creating the POC script, this step executes it using Node.js to start the server. The application will listen for requests and apply the flawed middleware. This is essential for subsequent testing of access controls and exploitation. Expected outcome: Server running and ready for HTTP interactions.

## Requirements

1. poc.js file created and dependencies installed
2. Port 3000 available (no conflicts)
3. Node.js executable in PATH

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments (e.g., Docker) for testing
- Log server startups and monitor for unauthorized launches
- Use firewalls to restrict port access during POCs

## Objectives

1. Activate the vulnerable application
2. Confirm server readiness
3. Enable endpoint testing

## Instructions

### Step 1: Execute the POC Script

**Context**: Starts the Express server with the integrated middleware.

**Command** ([[commands/node-run-poc]]):
```bash
node poc.js
```

> Runs the JavaScript file to initialize the server. Expected output: "Server on 3000" or similar listen confirmation; server remains running until stopped (Ctrl+C).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/node-run-poc]]

## Tools Used

- [[tools/node]]

## Tags

- launch
- server
- node-js
