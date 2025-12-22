---
id: proc-uuid-1
tags:
  - rce
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-commit-msg]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:19.358Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Vulnerable-commit-msg-Module

## Summary

This procedure installs the vulnerable commit-msg Node.js module (version 0.2.3) globally using npm, setting up the environment for exploiting an RCE vulnerability in Git commit message validation.

## Description

The commit-msg module is a Git hook validator that processes commit messages. In version 0.2.3, it suffers from insecure command formatting where user input is concatenated directly into shell commands in the bin/validate script (line 128), allowing command injection. This procedure targets developers who install third-party Git hooks, enabling local RCE during routine Git operations. Prerequisites include Node.js and npm installed on a Linux system.

## Requirements

1. Node.js runtime (v10+ recommended)
2. npm package manager
3. Local shell access on Linux
4. Internet access for package download

## Defense

Defensive measures and detection strategies:

- Audit and pin dependencies to secure versions (e.g., update commit-msg beyond 0.2.3)
- Use npm audit to scan for known vulnerabilities before installation
- Implement shell escaping or use safe APIs like child_process.execFile instead of shell execution
- Monitor global npm installations for suspicious packages

## Objectives

1. Install the specific vulnerable version of commit-msg
2. Make the module available system-wide for Git integration
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Install the Module

**Context**: Use npm to globally install commit-msg at the vulnerable version 0.2.3, ensuring the insecure bin/validate script is accessible.

**Command** ([[commands/npm-install-commit-msg]]):
```bash
npm i commit-msg@0.2.3 -g
```

> This command downloads and installs the package globally. Expected output includes installation progress and a success message like "+ commit-msg@0.2.3 added". Verify with `commit-msg --version` showing 0.2.3.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-commit-msg]]

## Tools Used

- [[tools/npm]]

## Tags

- rce
- node-js
- installation
