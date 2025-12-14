---
tags:
  - path-traversal
  - directory-traversal
  - node.js
  - file-read
  - web-server
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Linux
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-angular-http-server-Module]]'
  - '[[procedures/Create-Index-HTML-File]]'
  - '[[procedures/Start-Vulnerable-HTTP-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:11.765Z'
description: >-
  A multi-stage attack chain exploiting a path traversal vulnerability in the
  angular-http-server Node.js module (v1.4.3) to read sensitive local files like
  /etc/passwd by manipulating URL paths with double slashes.
skill_level: intermediate
impact_level: high
id: 1b814b19-6d01-4290-91ad-f33525c06c78
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Server Directory Traversal in angular-http-server to Read Arbitrary Local Files

Multi-stage attack chain demonstrating the exploitation of a server directory traversal vulnerability in the angular-http-server Node.js module version 1.4.3. Attackers can read arbitrary local files on the server by using double slashes (//) in URL paths to bypass directory normalization, potentially exposing sensitive system information like user accounts in /etc/passwd.

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
    A[Install Module] --> B[Create Index File]
    B --> C[Start Server]
    C --> D[Exploit Traversal]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/curl]]

### Target Environment

- Node.js runtime installed
- Linux-based system (for /etc/passwd access)
- Port 6060 available

### Initial Access Requirements

- Local access to a machine where the vulnerable angular-http-server can be installed and run
- No remote credentials needed; this is a local reproduction of the server-side vulnerability

## Detailed Attack Procedures

### Step 1: Install the Module
procedure: [[procedures/Install-angular-http-server-Module]]

**Objective**: Set up the vulnerable angular-http-server module using npm to prepare for server execution.

**Instructions**: Install the package locally or globally to access the server script.

**Expected Output**: npm installation logs confirming the package is installed in node_modules.

**Success Indicators**:
- Package listed in node_modules directory
- No installation errors

### Step 2: Create Index File
procedure: [[procedures/Create-Index-HTML-File]]

**Objective**: Generate a basic index.html file required for the server to start without errors.

**Instructions**: Create a simple HTML file in the current directory.

**Expected Output**: File index.html created with basic content.

**Success Indicators**:
- index.html exists and contains the echoed content
- Server can reference this file on startup

### Step 3: Start the Server
procedure: [[procedures/Start-Vulnerable-HTTP-Server]]

**Objective**: Launch the HTTP server on port 6060 to expose the vulnerable endpoint.

**Instructions**: Execute the server script from the installed module.

**Expected Output**: Server message indicating it's listening on http://127.0.0.1:6060.

**Success Indicators**:
- Server process running
- Accessible via curl on localhost:6060

### Step 4: Exploit the Vulnerability
procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Traverse directories using double slashes in the URL to read sensitive files like /etc/passwd.

**Instructions**: Send a GET request with --path-as-is to preserve the traversal payload.

**Expected Output**: Contents of /etc/passwd, including user entries like root and nobody.

**Success Indicators**:
- File contents returned in response
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of the vulnerable server
2. Exposure of the path traversal flaw through URL manipulation
3. Unauthorized read of system files, demonstrating information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
