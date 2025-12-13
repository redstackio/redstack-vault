---
tags:
  - node.js
  - server-setup
  - vulnerability-reproduction
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/setup-nodejs-server]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: cf9a3a50-17cc-45f1-935e-e2155fd2ae8d
created_at: '2025-12-13T09:01:17.232Z'
updated_at: '2025-12-13T09:01:17.232Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Node.js Test Server

## Summary

This procedure sets up a basic Node.js HTTP server to handle and log incoming requests, used for reproducing vulnerabilities in the http module's llhttp parser.

## Description

The server listens on port 5000, collects the request body, logs headers and body to the console, and responds with the body length. It targets the Node.js environment (v20.2.0) to demonstrate parsing issues with malformed HTTP requests.

## Requirements

1. Node.js installed (version 20.2.0 or compatible)
2. Local access to run scripts
3. Port 5000 available

## Defense

Defensive measures and detection strategies:

- Use updated Node.js versions with patched llhttp parser
- Monitor server logs for unusual header parsing

## Objectives

1. Establish a test environment for HTTP parsing vulnerabilities
2. Log request details for analysis
3. Prepare for sending crafted payloads

## Instructions

### Step 1: Run Server Script

**Context**: Executes the Node.js code to start the server.

**Command** ([[commands/setup-nodejs-server]]):
```javascript
const http = require("http"); http.createServer((request, response) => { let body = []; request.on("error", (err) => { response.end("Request Error: " + err); }).on("data", (chunk) => { body.push(chunk); }).on("end", () => { body = Buffer.concat(body).toString(); console.log("Response"); console.log(request.headers); console.log(body); console.log("---"); response.on("error", (err) => { response.end("Response Error: " + err); }); response.end("Body length: " + body.length.toString() + " Body: " + body); }); }).listen(5000);
```

> Starts the server and begins listening for requests, logging details upon receipt.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/setup-nodejs-server]]

## Tools Used

- [[tools/Node.js]]

## Tags

- [[tools/Node.js]]
- [[server-setup]]
