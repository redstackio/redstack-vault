---
tags:
  - http-smuggling
  - setup
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/run-node-js-http-server]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 192816c9-459f-4550-9274-27346874f07a
created_at: '2025-12-13T09:01:21.597Z'
updated_at: '2025-12-13T09:01:21.597Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Node.js Test Server for HTTP Smuggling

## Summary

This procedure sets up a simple Node.js HTTP server to replicate and test the HTTP request smuggling vulnerability caused by improper Content-Length header parsing.

## Description

The server handles basic routes like /hello and /bye, logging headers and responding with plain text. It serves as a testbed for smuggling attacks in Node.js 18.x environments, where leading spaces in headers lead to parsing errors and request desynchronization.

## Requirements

1. Node.js 18.x installed
2. Local access to run the server on port 8082
3. Basic JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Update Node.js to patched versions
- Implement strict header validation in HTTP parsers

## Objectives

1. Create a vulnerable server for testing
2. Verify basic route functionality
3. Prepare for smuggling exploitation

## Instructions

### Step 1: Create and Run Server Script

**Context**: Executes the Node.js script to start the HTTP server.

**Command** ([[commands/run-node-js-http-server]]):
```javascript
const http = require('http'); const port = 8082; const server = http.createServer((req, res) => { if (req.url === '/hello') { console.log(JSON.stringify(req.headers)); console.log('%s', req.url); res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end('Hello, World!\n'); } else if (req.url === '/bye') { console.log('%s', req.url) console.log(JSON.stringify(req.headers)); res.writeHead(200, { 'Content-Type': 'text/plain' }); const name = req.headers['x-name'] || 'World'; res.end(`Goodbye, ${name}!\n`); } else { res.writeHead(404, { 'Content-Type': 'text/plain' }); res.end('Route not found\n'); } }); server.listen(port, () => { console.log(`Server running at http://localhost:${port}/`); });
```

> Runs the server and logs requests to console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/run-node-js-http-server]]

## Tools Used

- [[tools/Node-js]]

## Tags

- [[http-smuggling]]
- [[setup]]
