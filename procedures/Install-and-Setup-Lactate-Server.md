---
id: proc-lactate-setup-001
name: Install-and-Setup-Lactate-Server
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.026Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - setup
  - node.js
  - installation
commands:
  - '[[commands/npm-install-lactate]]'
  - '[[commands/cd-root-directory]]'
platforms:
  - Linux
tools:
  - '[[tools/npm]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Install-and-Setup-Lactate-Server

## Summary

This procedure installs the vulnerable lactate Node.js static web server package (v0.13.12) globally and sets the web root directory to /root, preparing a test environment for demonstrating path traversal exploitation.

## Description

In a Linux environment with Node.js installed, this setup creates a controlled scenario where the lactate server can be run to serve files from /root. The vulnerability arises from improper path sanitization in lactate's handling of GET request paths, allowing traversal attacks. Prerequisites include administrative access for global npm installation and a clean Ubuntu-like system.

## Requirements

1. Node.js and npm installed on the host
2. Shell access (e.g., root or sudo privileges)
3. Internet connectivity for package download

## Defense

Defensive measures and detection strategies:

- Use package managers with vulnerability scanners like npm audit
- Run servers in isolated containers (e.g., Docker) to limit file access
- Monitor for unexpected npm installations via logging tools like auditd

## Objectives

1. Install lactate v0.13.12 globally
2. Configure the serving directory to /root
3. Prepare for server launch without errors

## Instructions

### Step 1: Install Lactate Globally

**Context**: Download and install the vulnerable package system-wide using npm.

**Command** ([[commands/npm-install-lactate]]):
```bash
npm install -g lactate
```

> This command fetches and installs lactate v0.13.12, outputting installation logs and version confirmation. Success is indicated by no errors and the binary available in PATH.

### Step 2: Change to Web Root Directory

**Context**: Set the current directory to /root to define the web root for the server.

**Command** ([[commands/cd-root-directory]]):
```bash
cd /root
```

> Changes the working directory; expected output is an updated shell prompt showing /root as current path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-lactate]]
- [[commands/cd-root-directory]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node.js
- installation
