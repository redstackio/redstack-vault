---
id: 8350f0ed-32d9-423c-b8ee-f7a1151a89bd
name: Featurebook Directory Traversal for Arbitrary File Disclosure
type: attack_chain
description: >-
  Multi-stage attack exploiting directory traversal in the Node.js featurebook
  package to read arbitrary files from the host filesystem.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.857Z'
procedures:
  - '[[procedures/Install-and-Setup-Featurebook-Server]]'
  - '[[procedures/Exploit-Directory-Traversal-via-URL-Hash]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
tags:
  - directory-traversal
  - path-traversal
  - file-disclosure
  - node-js
platforms:
  - Web
  - Linux
  - Node.js
tools:
  - '[[tools/npm]]'
  - '[[tools/Chrome]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---

# Featurebook Directory Traversal for Arbitrary File Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting a directory traversal vulnerability in the Node.js 'featurebook' package version 0.0.32. The attack allows reading arbitrary files outside the web root by crafting requests to the viewer endpoint using URL hash parameters with traversal sequences like '..%2f'. This can lead to disclosure of sensitive files such as /etc/passwd, application source code, or system configuration data.

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
    A[Setup Server] --> B[Start Featurebook] --> C[Craft Malicious URL] --> D[Access Arbitrary File]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/Chrome]]

### Target Environment

- Node.js runtime
- Linux-based server (e.g., for testing in /root directory)
- Port 8081 available
- Network access to the server

### Initial Access Requirements

- Local access to install and run the featurebook server
- No prior credentials needed, as this exploits a public-facing web server
- Attacker must control or have access to a test environment running featurebook v0.0.32

## Detailed Attack Procedures

### Step 1: Install Featurebook Globally
procedure: [[procedures/Install-and-Setup-Featurebook-Server]]

**Objective**: Install the vulnerable featurebook package to prepare for server setup.

**Instructions**: Use [[commands/npm-install-global]] to install featurebook globally via npm.

```bash
npm install -g featurebook@0.0.32
```

**Expected Output**: Installation completes without errors, and featurebook is available in the global PATH.

**Success Indicators**:
- Featurebook command is executable (verify with `featurebook --help`)
- No dependency conflicts

### Step 2: Navigate to Test Directory
procedure: [[procedures/Install-and-Setup-Featurebook-Server]]

**Objective**: Position the server in a directory from which traversal can access sensitive system files.

**Instructions**: Change to a root-level directory using [[commands/cd-directory-navigate]] to set the serving location.

```bash
cd /root
```

**Expected Output**: Current working directory is /root (confirm with `pwd`).

**Success Indicators**:
- Directory changed successfully
- Permissions allow serving from this location

### Step 3: Start the Featurebook Server
procedure: [[procedures/Install-and-Setup-Featurebook-Server]]

**Objective**: Launch the vulnerable server on port 8081 to expose the traversal endpoint.

**Instructions**: Execute [[commands/featurebook-serve]] to start serving content from the current directory.

```bash
featurebook serve --port 8081
```

**Expected Output**: Server starts and logs "Server listening on port 8081".

**Success Indicators**:
- Server is running and accessible
- No startup errors

### Step 4: Exploit Directory Traversal
procedure: [[procedures/Exploit-Directory-Traversal-via-URL-Hash]]

**Objective**: Send a crafted request to the viewer endpoint to traverse directories and read a sensitive file like /etc/passwd.

**Instructions**: Open [[tools/Chrome]] and navigate to the malicious URL: http://<server-IP>:8081/#/viewer/..%2f..%2fetc%2fpasswd.

**Expected Output**: The browser displays the contents of /etc/passwd in an error message, confirming file disclosure.

**Success Indicators**:
- Sensitive file contents visible in the response
- Traversal sequence (..%2f) successfully navigates outside the web root

## Attack Chain Summary

### Key Achievements

1. Successful installation and startup of the vulnerable featurebook server.
2. Exploitation of unsanitized path parameters in the URL hash to perform directory traversal.
3. Disclosure of arbitrary host files, such as /etc/passwd, demonstrating potential for source code or config leakage.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
