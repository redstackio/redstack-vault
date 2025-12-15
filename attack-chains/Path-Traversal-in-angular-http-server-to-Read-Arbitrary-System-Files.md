---
id: ac-uuid-001
tags:
  - path-traversal
  - node-js
  - file-read
  - arbitrary-file-access
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/angular-http-server]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Node.js
  - Linux
  - macOS
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-angular-http-server]]'
  - '[[procedures/Setup-and-Run-angular-http-server]]'
  - '[[procedures/Verify-Server-Operation]]'
  - '[[procedures/Exploit-Path-Traversal-with-curl]]'
step_count: 5
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:16.734Z'
description: >-
  Demonstrates exploiting a path traversal vulnerability in the
  angular-http-server Node.js module to read arbitrary files on the server, such
  as /etc/passwd, by crafting HTTP requests with directory traversal sequences.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Path Traversal in angular-http-server to Read Arbitrary System Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the angular-http-server Node.js module, allowing remote reading of arbitrary files on the server.

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
    B --> C[Verify Access]
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
- [[tools/angular-http-server]]
- [[tools/curl]]

### Target Environment

- Node.js runtime (version 8.9.3 or similar)
- macOS or Linux OS
- Port 8080 available
- Local network access to localhost

### Initial Access Requirements

- Local machine with Node.js and npm installed
- No remote credentials needed; exploits local server setup
- Administrative access not required for exploitation

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-angular-http-server]]

**Objective**: Obtain the vulnerable angular-http-server module using npm to set up the exploitable environment.

**Instructions**: Execute the installation command to download the module.

**Expected Output**: npm logs showing successful installation of angular-http-server.

**Success Indicators**:
- Module installed in node_modules directory
- No errors in npm output

### Step 2: Setup and Run Server
procedure: [[procedures/Setup-and-Run-angular-http-server]]

**Objective**: Create a basic static file and launch the vulnerable server to host the single-page application environment.

**Instructions**: First, create a simple index.html file in the current directory. Then, start the server using [[commands/angular-http-server-run]]:

```bash
angular-http-server --path ./
```

**Expected Output**: Server logs indicating path specified as ./, using index.html, and listening on port 8080.

**Success Indicators**:
- Server starts without errors
- Port 8080 is bound

### Step 3: Verify Server Operation
procedure: [[procedures/Verify-Server-Operation]]

**Objective**: Confirm the server is accessible and serving content correctly before exploitation.

**Instructions**: Open a browser and navigate to http://127.0.0.1:8080 to view the index.html content.

**Expected Output**: Display of the basic HTML page served by the angular-http-server.

**Success Indicators**:
- Page loads successfully in browser
- No connection errors

### Step 4: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-curl]]

**Objective**: Craft an HTTP request with directory traversal sequences to read an arbitrary system file like /etc/passwd.

**Instructions**: Use [[commands/curl-path-traversal-exploit]] to send the malicious request:

```bash
curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/passwd
```

**Expected Output**: Verbose curl output including the content of /etc/passwd, and server logs showing the file being sent with Content-Type application/octet-stream.

**Success Indicators**:
- Arbitrary file content retrieved
- No path normalization occurs due to --path-as-is flag

### Step 5: Analyze Impact

**Objective**: Review the exposed data and potential for further attacks.

**Instructions**: Examine the retrieved file content for sensitive information such as usernames and hashed passwords.

**Expected Output**: Readable content from /etc/passwd revealing system user details.

**Success Indicators**:
- Sensitive data exposed
- Potential for chaining to RCE or other exploits identified

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable server
2. Verification of server accessibility
3. Exploitation of path traversal to read /etc/passwd
4. Demonstration of arbitrary file read capability leading to information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
