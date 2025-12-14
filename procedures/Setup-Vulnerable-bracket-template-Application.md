---
tags:
  - setup
  - node.js
  - template
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/Node.js]]'
  - '[[tools/bracket-template]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-bracket-template]]'
  - '[[commands/node-run-app]]'
platforms:
  - Node.js
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c89dede6-08dc-4981-9674-2c15dd4f89ef
created_at: '2025-12-14T03:16:37.188Z'
updated_at: '2025-12-14T03:16:37.188Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Setup-Vulnerable-bracket-template-Application

## Summary

This procedure installs the vulnerable bracket-template module and creates a sample Node.js application that interpolates unsanitized GET parameters into templates, setting up the environment for XSS exploitation.

## Description

In the context of reproducing the reflected XSS in bracket-template v1.1.5, this involves using npm to install the module and writing a basic HTTP server in Node.js. The server reads a 'name' parameter from the URL query and embeds it directly into a template without additional sanitization, making it vulnerable to injection attacks. Prerequisites include Node.js installed on the system. Expected outcomes: A running local server on port 8080 ready for testing payloads.

## Requirements

1. Node.js runtime (version 8.9.3 or later)
2. npm package manager
3. Local file system access to create app.js
4. No network access beyond localhost

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before template interpolation using libraries like DOMPurify
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for unusual hex-escaped characters in logs
- Update to patched versions or switch to secure templating engines like Handlebars with strict mode

## Objectives

1. Prepare a reproducible vulnerable environment
2. Enable testing of template rendering behaviors
3. Facilitate payload injection without external dependencies

## Instructions

### Step 1: Install the Module

**Context**: Begin by adding the vulnerable bracket-template to your project dependencies.

**Command** ([[commands/npm-install-bracket-template]]):
```bash
npm install bracket-template
```

> This command fetches and installs bracket-template v1.1.5 (or latest vulnerable) from npm, adding it to node_modules. Expected output includes installation progress and confirmation in package.json.

### Step 2: Create the Sample Application

**Context**: Write the Node.js server code to demonstrate unsafe interpolation.

**Command** (No direct command; manual file creation):

Create app.js with the following content:
```javascript
const http = require('http');
const bt = require('bracket-template');

http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const name = url.searchParams.get('name') || 'World';
  const tpl = `[[ const n = '${name}'; ]] <strong>Hello [[= n ]]</strong>`;
  const createHTML = bt.compile(tpl);
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end(createHTML());
}).listen(8080);
console.log('server is listening on 8080');
```

> This sets up an HTTP server that compiles and executes the template with the raw 'name' input.

### Step 3: Run the Application

**Context**: Start the server to host the vulnerable endpoint.

**Command** ([[commands/node-run-app]]):
```bash
node app.js
```

> Launches the server on localhost:8080. Expected output: 'server is listening on 8080'. Verify by accessing http://localhost:8080 in a browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-bracket-template]]
- [[commands/node-run-app]]

## Tools Used

- [[tools/npm]]
- [[tools/Node.js]]
- [[tools/bracket-template]]

## Tags

- setup
- node.js
- template
