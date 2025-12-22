---
tags:
  - poc
  - express
  - middleware
type: procedure
tools:
  - '[[tools/Express]]'
  - '[[tools/node]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.580Z'
sub_techniques: []
id: 1c856d69-d624-4588-b0a1-0a5c0bb042ea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-POC-Express-Application

## Summary

This procedure creates a proof-of-concept Express application that integrates the vulnerable expressjs-ip-control middleware to enforce IP whitelisting on a sensitive endpoint.

## Description

To demonstrate the vulnerability, a simple Express server is built where the ipControl middleware whitelists specific IPs (e.g., 127.0.0.1, 192.168.10.10) and protects the root path with a response containing mock sensitive data like a secret token. The module's flaw lies in trusting the X-Forwarded-For header, allowing bypass. This runs in a Node.js environment and requires no external services. Expected outcome: A runnable script that simulates a protected API.

## Requirements

1. Installed expressjs-ip-control and express modules
2. Text editor or IDE for JavaScript
3. Local Node.js runtime

## Defense

Defensive measures and detection strategies:

- Validate proxy headers against trusted sources (e.g., using express's trust proxy setting)
- Use more robust access control like JWT or OAuth instead of simple IP whitelists
- Code review middleware for header trust issues

## Objectives

1. Simulate a real-world protected endpoint
2. Configure vulnerable IP controls
3. Prepare for testing and exploitation

## Instructions

### Step 1: Write the POC Script

**Context**: Manually create the poc.js file to set up the server and middleware.

**Command** (No CLI command; manual file creation):

Create poc.js with:
```javascript
const express = require('express');
const ipControl = require('expressjs-ip-control');
const app = express();

app.use('/', ipControl(['127.0.0.1', '192.168.10.10']));

app.get('/', (req, res) => {
  res.send('SECRET TOKEN ACCESSIBLE ONLY BY LOCAL PC');
});

app.listen(3000, () => console.log('Server on 3000'));
```

> This code initializes Express, applies the middleware to the root path, and serves sensitive content only to whitelisted IPs. Expected output: Valid file without syntax errors (test with `node -c poc.js`).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Express]]
- [[tools/node]]

## Tags

- poc
- express
- middleware
