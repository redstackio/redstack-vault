---
tags:
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/node-run-server]]'
platforms:
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3f2a3442-f140-4cc7-9a3a-45fb649eec69
created_at: '2025-12-13T09:01:17.168Z'
updated_at: '2025-12-13T09:01:17.168Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set Up Node.js HTTP Test Server

## Summary

This procedure sets up a simple Node.js HTTP server using the http module to test vulnerabilities like HTTP Request Smuggling by logging requests and responding with body length.

## Description

The server is created to reproduce parsing issues in the llhttp parser of Node.js v18.7.0. It listens on port 5000, logs incoming headers and body, and serves as a target for malformed requests. This is essential for verifying how the server handles improper header terminations.

## Requirements

1. Node.js v18.7.0 installed
2. Local machine access
3. app.js script with basic HTTP server code

## Defense

Defensive measures and detection strategies:

- Update Node.js to a patched version
- Monitor server logs for unusual header formats

## Objectives

1. Establish a test environment for vulnerability reproduction
2. Enable logging of requests for analysis
3. Confirm server is running without errors

## Instructions

### Step 1: Run the Server Script

**Context**: Execute the Node.js script to start the HTTP server.

**Command** ([[commands/node-run-server]]):

```bash
node app.js
```

> This command runs the app.js file, which creates an HTTP server that logs requests and responds with the body length.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/node-run-server]]

## Tools Used

- [[tools/Node-js]]

## Tags

- [[tools/Node-js]]
- [[setup]]
