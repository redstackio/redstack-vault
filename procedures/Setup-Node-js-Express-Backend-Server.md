---
tags:
  - setup
  - node-js
  - express
type: procedure
tools:
  - '[[tools/Node-js]]'
  - '[[tools/Express]]'
  - '[[tools/npm]]'
  - '[[tools/body-parser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-express]]'
  - '[[commands/node-run-express-app]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 42b8553e-b71c-4eca-bf6c-2ecb83166bfd
created_at: '2025-12-13T09:01:22.131Z'
updated_at: '2025-12-13T09:01:22.131Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Node.js Express Backend Server

## Summary

This procedure sets up a Node.js Express application as a backend server, creating endpoints that can be exploited via HTTP request smuggling due to Node.js's handling of duplicate headers.

## Description

Install Express via npm, then create and run an app.js file defining GET /, GET /flag (restricted), and POST / endpoints. The server listens on port 8080 and uses body-parser middleware, making it vulnerable when behind a proxy like HAProxy.

## Requirements

1. Node.js installed (versions 14.13.1 or 12.19.0)
2. npm package manager
3. app.js file prepared with Express configuration

## Defense

Defensive measures and detection strategies:

- Update Node.js to versions that properly handle duplicate headers
- Implement strict header validation in backend applications

## Objectives

1. Deploy a vulnerable backend server
2. Expose endpoints for testing smuggling
3. Verify server functionality

## Instructions

### Step 1: Install Express

**Context**: Install the Express framework dependency.

**Command** ([[commands/npm-install-express]]):
```bash
npm install express
```

> Installs Express in the node_modules directory.

### Step 2: Run Express App

**Context**: Start the server with debug mode enabled.

**Command** ([[commands/node-run-express-app]]):
```bash
DEBUG=express:* node app.js
```

> Runs the app.js script, enabling debug logging for Express modules, and starts listening on port 8080.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/npm-install-express]]
- [[commands/node-run-express-app]]

## Tools Used

- [[tools/Node-js]]
- [[tools/Express]]
- [[tools/npm]]
- [[tools/body-parser]]

## Tags

- [[setup]]
- [[tools/Node-js]]
- [[tools/Express]]
