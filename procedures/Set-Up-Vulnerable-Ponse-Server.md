---
id: proc-ponse-setup-001
tags:
  - node-js
  - server-setup
  - vulnerable-config
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:06.650Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Vulnerable-Ponse-Server

## Summary

This procedure creates a sample Node.js server script that utilizes the vulnerable ponse module to serve static files, intentionally exposing the path traversal issue in the getStatic function for reproduction purposes.

## Description

By requiring the ponse and http modules, this setup configures an HTTP server that calls ponse.static(__dirname) without path validation, allowing directory traversal attacks. The server listens on port 8080, simulating a public-facing application vulnerable to arbitrary file reads. This is based on code analysis from the HackerOne report, where the flaw stems from direct use of user paths in file operations.

## Requirements

1. ponse module installed via previous procedure
2. Basic knowledge of Node.js scripting
3. Text editor to write the index.js file

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all file paths using libraries like path.normalize or validator.js
- Implement access controls to restrict file serving to specific directories
- Use secure static file servers like express.static with options for path resolution

## Objectives

1. Create a reproducible vulnerable server configuration
2. Ensure the getStatic function is exposed
3. Prepare for server execution and exploitation

## Instructions

### Step 1: Create index.js File

**Context**: Write the server code to import modules and set up the vulnerable static handler.

**Command** (Manual file creation):
```javascript
// index.js
const ponse = require('ponse');
const http = require('http');
const server = http.createServer(ponse.static(__dirname));
server.listen(8080, () => {
  console.log('Server listening on port 8080');
});
```

> Save this as index.js in the project directory. This code directly uses ponse.static without safeguards, replicating the vulnerability. Expected outcome: A syntactically valid script ready to run.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/node]]

## Tags

- node-js
- server-setup
