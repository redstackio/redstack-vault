---
id: 4331d5d5-5efd-488d-9ed7-fb0cb1ec2d69
name: Install-and-Setup-Featurebook-Server
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.852Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - setup
  - node-js
  - installation
commands:
  - '[[commands/npm-install-global]]'
  - '[[commands/cd-directory-navigate]]'
  - '[[commands/featurebook-serve]]'
platforms:
  - Linux
  - Node.js
tools:
  - '[[tools/npm]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Install-and-Setup-Featurebook-Server

## Summary

This procedure installs the vulnerable featurebook package version 0.0.32 globally using npm, navigates to a test directory, and starts the server on port 8081, preparing the environment for directory traversal exploitation.

## Description

In the context of testing the directory traversal vulnerability in featurebook v0.0.32, this procedure sets up the Node.js server in a controlled environment. The server serves content from the current directory, and without proper path sanitization, it becomes vulnerable to traversal attacks via the viewer endpoint. Prerequisites include Node.js installed and npm available. Expected outcomes include a running server accessible on port 8081, from which crafted URLs can exploit the flaw to read files like /etc/passwd.

## Requirements

1. Node.js runtime installed on a Linux system
2. npm package manager access
3. Root or sufficient permissions to install globally and change directories (e.g., to /root)
4. Port 8081 free for binding

## Defense

Defensive measures and detection strategies:

- Input validation: Sanitize URL hash parameters to block traversal sequences like '..%2f'
- Path normalization: Use libraries like path.normalize() in Node.js to resolve paths safely
- File access controls: Run the server in a chrooted or containerized environment to limit filesystem access
- Logging: Monitor for unusual file access patterns or error messages containing file contents

## Objectives

1. Prepare a vulnerable server instance for exploitation testing
2. Ensure the serving directory allows traversal to sensitive system files
3. Verify server startup without errors to confirm exploitability

## Instructions

### Step 1: Global Installation

**Context**: Install the specific vulnerable version of featurebook to replicate the environment.

**Command** ([[commands/npm-install-global]]):
```bash
npm install -g featurebook@0.0.32
```

> This command fetches and installs featurebook v0.0.32 globally, making the 'featurebook' binary available system-wide. Expected output includes download progress and a success message like "added X packages".

### Step 2: Directory Navigation

**Context**: Move to a directory (e.g., /root) to set the web root, enabling traversal to /etc/passwd.

**Command** ([[commands/cd-directory-navigate]]):
```bash
cd /root
```

> Changes the current working directory to /root. Expected output is no output if successful; verify with `pwd` showing "/root".

### Step 3: Server Startup

**Context**: Launch the server to expose the vulnerable viewer endpoint.

**Command** ([[commands/featurebook-serve]]):
```bash
featurebook serve --port 8081
```

> Starts the featurebook server listening on port 8081 from the current directory. Expected output: "Server is running on http://localhost:8081" or similar, with the process remaining active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-global]]
- [[commands/cd-directory-navigate]]
- [[commands/featurebook-serve]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js
- installation
