---
tags:
  - xss
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-dy-server2]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.475Z'
sub_techniques: []
id: 89a17bf4-f50e-4304-99b3-ad8e14fec30d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-dy-server2-Package

## Summary

This procedure installs the vulnerable dy-server2 Node.js package globally via npm, enabling the setup of a lightweight HTTP server that serves files without sanitizing file or folder names, which is a prerequisite for exploiting the stored XSS vulnerability.

## Description

The dy-server2 package is a simple HTTP server for file transfer and frontend previews. Installing it globally allows execution from any directory. In the attack scenario, this sets up the environment to serve maliciously named files or folders, leading to XSS when accessed via a browser. The target environment is any system with Node.js and npm installed. Expected outcomes include the server command being available for launch, with no immediate exploitation until subsequent steps.

## Requirements

1. Node.js and npm installed on the system
2. Internet access for package download from npm registry
3. Terminal or command-line interface access

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages like dy-server2 in security logs
- Use npm audit to scan for known vulnerabilities before installation
- Restrict global npm installs via policy or require approval

## Objectives

1. Prepare the vulnerable server for exploitation
2. Ensure dy-server2 is executable system-wide
3. Set up for serving unsanitized directory listings

## Instructions

### Step 1: Global Installation

**Context**: Install dy-server2 globally to add it to the system's PATH, allowing server startup from any directory.

**Command** ([[commands/npm-install-dy-server2]]):
```bash
npm i -g dy-server2
```

> This command fetches and installs the package from the npm registry. Expected output includes progress bars for download and installation, ending with a success message like 'added X packages'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-dy-server2]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- node-js
- installation
