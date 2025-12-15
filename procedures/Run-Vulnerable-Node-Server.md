---
tags:
  - node-js
  - server-execution
  - vulnerability
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-app]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:12.642Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: befb076e-d589-408b-8945-7a70e0bd5ff9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Vulnerable-Node-Server

## Summary

This procedure starts the Node.js application configured with the vulnerable 'stattic' module, launching an HTTP server on port 8080 that serves static files and is susceptible to path traversal attacks.

## Description

Executing app.js with Node.js initializes the server, binding to localhost:8080. The vulnerability arises because incoming request paths are directly joined to the root folder without traversal prevention, allowing access to files like /etc/hosts.deny. This step is essential to make the endpoint live for exploitation testing.

## Requirements

1. app.js file created with stattic configuration
2. Node.js installed and in PATH
3. Port 8080 available

## Defense

Defensive measures and detection strategies:

- Run servers in isolated environments or containers
- Monitor process listings for unexpected Node.js instances on high ports
- Use firewalls to restrict access to development ports

## Objectives

1. Launch the vulnerable HTTP server
2. Confirm it's listening on the specified port
3. Enable incoming requests for exploitation

## Instructions

### Step 1: Execute the Application

**Context**: Run the script to start the server process.

**Command** ([[commands/node-run-app]]):
```bash
node app.js
```

> This launches the server, printing "Server running on port 8080" to console. Expected output: Confirmation message; server remains running until interrupted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/node-run-app]]

## Tools Used

- [[tools/node]]

## Tags

- node-js
- server-execution
- vulnerability
