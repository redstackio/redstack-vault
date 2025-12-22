---
id: proc-uuid-001
tags:
  - path-traversal
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-angular-http-server]]'
verified: false
platforms:
  - Node.js
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:16.730Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-angular-http-server

## Summary

This procedure installs the vulnerable angular-http-server Node.js module using npm, setting up the environment for demonstrating path traversal exploitation.

## Description

The angular-http-server module contains a path traversal vulnerability in its file serving logic (angular-http-server.js lines 66-82), where fs.readFileSync is used without path sanitization. Installing it locally or globally allows running the server to host a test single-page application, enabling subsequent exploitation via crafted HTTP requests with '../' sequences to access files outside the served directory, such as system files.

## Requirements

1. Node.js (version 8.9.3 or compatible) installed
2. npm (version 5.5.1 or compatible) available
3. Internet access for package download
4. Local directory for installation

## Defense

Defensive measures and detection strategies:

- Use audited and updated packages; avoid unmaintained modules like angular-http-server
- Implement path validation in custom servers using libraries like path.normalize() or path.resolve()
- Monitor npm installations for known vulnerable packages via tools like npm audit
- Log and alert on unusual file access patterns in server logs

## Objectives

1. Download and install the vulnerable module
2. Prepare the environment for server setup
3. Enable testing of the path traversal vulnerability

## Instructions

### Step 1: Install the Module

**Context**: Use npm to install angular-http-server, which will be used to run the vulnerable HTTP server.

**Command** ([[commands/npm-install-angular-http-server]]):
```bash
npm install angular-http-server
```

> This command downloads and installs the package into the local node_modules directory. Expected output includes installation logs like 'added X packages' and no errors indicating successful setup.

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

- path-traversal
- node-js
- installation
