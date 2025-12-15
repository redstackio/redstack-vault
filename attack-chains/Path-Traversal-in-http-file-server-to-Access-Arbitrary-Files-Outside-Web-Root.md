---
id: ac-path-traversal-http-file-server
tags:
  - path-traversal
  - node-js
  - file-disclosure
  - directory-traversal
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/http-file-server]]'
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
  - '[[procedures/Install-Vulnerable-http-file-server]]'
  - '[[procedures/Start-http-file-server-with-Tmp-Root]]'
  - '[[procedures/Exploit-Path-Traversal-with-Burp-Suite]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.602Z'
description: >-
  Demonstrates exploitation of path traversal vulnerability in http-file-server
  0.2.6 to read arbitrary files and directories on the server.
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
# Path Traversal in http-file-server to Access Arbitrary Files Outside Web Root

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the Node.js http-file-server module version 0.2.6, allowing attackers to access and list files outside the intended web root directory, potentially exposing sensitive information like credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable Server] --> B[Start File Server] --> C[Exploit Path Traversal]
    C --> D[Access Sensitive Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/Burp-Suite]]
- [[tools/http-file-server]]

### Target Environment

- Node.js runtime (v8.9.3 or compatible)
- Linux-based server with /tmp/ directory accessible
- Port 1234 open for HTTP traffic
- Network access to the server's interface

### Initial Access Requirements

- Local or remote access to install and run Node.js modules
- No prior credentials needed for exploitation, as it's a public-facing server
- Ability to send raw HTTP requests to the server

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Server
procedure: [[procedures/Install-Vulnerable-http-file-server]]

**Objective**: Install the vulnerable http-file-server module to prepare for reproduction of the path traversal issue.

**Instructions**: Use [[commands/npm-install-global-http-file-server]] to install the module globally via npm.

```bash
npm install -g http-file-server
```

**Expected Output**: Installation logs confirming the module is installed, including version 0.2.6.

**Success Indicators**:
- Module installed without errors
- Verify with `http-file-server --version` showing 0.2.6

### Step 2: Start File Server
procedure: [[procedures/Start-http-file-server-with-Tmp-Root]]

**Objective**: Launch the http-file-server with /tmp/ as the web root, binding to all interfaces on port 1234, to create the vulnerable endpoint.

**Instructions**: Execute [[commands/start-http-file-server-with-tmp-root]] from the module's directory.

```bash
./http-file-server.js --path=/tmp/ --host=* --port=1234
```

**Expected Output**: Server startup message like "Server listening on port 1234".

**Success Indicators**:
- Server responds to HTTP requests on port 1234
- Access http://server-ip:1234/ to see /tmp/ contents

### Step 3: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-Burp-Suite]]

**Objective**: Use path traversal sequences to access files outside /tmp/, such as parent directories, to list arbitrary files and expose sensitive data.

**Instructions**: Configure [[tools/Burp-Suite]] as a proxy, intercept a request to the server, and modify the URL path to include '../' sequences, e.g., http://server-ip:1234/../../../../etc/passwd. Send the raw request to bypass browser normalization.

**Expected Output**: HTTP response listing files from the targeted directory, like /etc/ contents.

**Success Indicators**:
- Response contains unintended file listings
- Sensitive files (e.g., config files with credentials) are accessible

## Attack Chain Summary

### Key Achievements

1. Successful installation and startup of the vulnerable server
2. Bypassing path validation to traverse directories
3. Exposure of arbitrary files, enabling further attacks like credential theft or RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
