---
id: proc-uuid-001
tags:
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-statics-server-global]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:17.389Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Statics-Server-Globally

## Summary

This procedure installs the vulnerable statics-server Node.js module (v0.0.9) globally using npm, preparing the environment for exploiting the path traversal vulnerability.

## Description

The statics-server module is a simple static file server that, in version 0.0.9, lacks symlink validation, allowing path traversal attacks. Global installation makes the 'statics-server' command available system-wide. This step requires Node.js and npm installed on a Linux system with sufficient permissions.

## Requirements

1. Node.js and npm installed
2. Internet access for package download
3. Write permissions to global npm directory

## Defense

Defensive measures and detection strategies:

- Audit npm global installations for untrusted packages
- Use package managers with vulnerability scanning (e.g., npm audit)
- Restrict global installs via policies

## Objectives

1. Prepare the vulnerable tool for execution
2. Enable server startup from any directory
3. Set up for subsequent exploit steps

## Instructions

### Step 1: Install the Module

**Context**: Globally install statics-server to make it executable.

**Command** ([[commands/npm-install-statics-server-global]]):
```bash
npm install statics-server -g
```

> This command downloads and installs the package globally. Expected output includes installation progress and confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/npm-install-statics-server-global]]

## Tools Used

- [[tools/npm]]

## Tags

- node-js
- installation
