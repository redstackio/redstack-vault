---
id: proc-uuid-2345-6789
tags:
  - node-js
  - server-setup
  - script-creation
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:26:05.743Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[JavaScript]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Create-Test-Server-Script

## Summary

This procedure creates a Node.js script (test.js) that sets up a local HTTP server using the vulnerable deliver-or-else module to serve files from a 'public' directory, enabling reproduction of the path traversal vulnerability.

## Description

The script imports the Deliver class, sets the document root to ./public, creates an HTTP server on port 80, and uses deliver.deliver(req, res) to handle requests with basic 404 error catching. This setup mimics a real application using the module, where path traversal can be tested. A 'public' directory should be created empty for testing.

## Requirements

1. Installed deliver-or-else module
2. Node.js environment
3. Text editor for script creation

## Defense

Defensive measures and detection strategies:

- Review server scripts for unsanitized path handling in third-party modules
- Use linters like ESLint to flag insecure file serving
- Implement path validation in custom code

## Objectives

1. Configure server to use vulnerable module
2. Limit serving to 'public' directory initially
3. Prepare for running and exploitation

## Instructions

### Step 1: Write the Server Script

**Context**: Manually create test.js with code that initializes the Deliver instance and starts the server.

**Command** (Manual file creation):
```javascript
const Deliver = require('deliver-or-else');
const path = require('path');
const http = require('http');

const deliver = new Deliver(path.join(__dirname, 'public'));
const server = http.createServer((req, res) => {
  deliver.deliver(req, res).catch(err => {
    if (err.status === 404) {
      res.writeHead(404);
      res.end('Not Found');
    }
  });
});
server.listen(80, '127.0.0.1', () => {
  console.log('Starting server...');
});
```

> Save the file as test.js. Expected outcome: Script ready for execution, with root set to prevent initial traversals but vulnerable to bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- [[JavaScript]] JavaScript

## Commands Used

- None (manual script creation)

## Tools Used

- [[tools/node]]

## Tags

- node-js
- server-setup
