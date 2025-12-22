---
tags:
  - setup
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-angular-http-server]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.750Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bf85f1e8-b1d8-4ed1-8db8-2cace3c3564c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-angular-http-server-Module

## Summary

This procedure installs the vulnerable angular-http-server Node.js module (version 1.4.3) using npm, preparing the environment to reproduce the directory traversal vulnerability.

## Description

The angular-http-server module is a simple HTTP server for Angular applications, but version 1.4.3 contains a path traversal flaw. Installing it locally allows running the server to test exploitation. This step requires Node.js and npm installed on a Linux system. Expected outcome is the module available in node_modules for subsequent server startup.

## Requirements

1. Node.js and npm installed on the target machine
2. Internet access for package download
3. Write permissions in the current directory

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit before installation
- Restrict npm installations to trusted sources and versions
- Monitor for installations of known vulnerable packages via audit logs

## Objectives

1. Install the affected module to enable server execution
2. Verify package integrity for reproduction
3. Set up dependencies without errors

## Instructions

### Step 1: Install the Package

**Context**: Use npm to download and install angular-http-server in the current directory.

**Command** ([[commands/npm-install-angular-http-server]]):
```bash
npm i angular-http-server
```

> This command installs the package locally. Expected output includes download progress and confirmation like "added 1 package".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-angular-http-server]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node.js
