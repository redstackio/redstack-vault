---
id: proc-uuid-1
tags:
  - nodejs
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-i-cloudcmd]]'
verified: false
platforms:
  - Node.js
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:15:31.085Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Install-CloudCMD-Module

## Summary

This procedure installs the vulnerable CloudCMD Node.js module using npm, preparing the environment for exploiting the stored XSS vulnerability in its file manager interface.

## Description

CloudCMD is an orthodox web file manager for Node.js. Version 9.1.5 contains a stored XSS flaw where filenames are not sanitized before being injected into the HTML directory listing. This procedure fetches the module from the npm registry, enabling subsequent steps to launch the server and create malicious files. It requires Node.js and npm installed on a Linux or macOS system.

## Requirements

1. Node.js runtime (version 10+ recommended)
2. npm package manager
3. Internet access to the npm registry
4. Local directory for installation

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages like cloudcmd in production environments
- Use package vulnerability scanners (e.g., npm audit) to detect known issues
- Restrict npm installs to trusted sources or use lockfiles

## Objectives

1. Obtain the CloudCMD module for local exploitation
2. Set up the node_modules directory
3. Prepare for server launch without errors

## Instructions

### Step 1: Install the Package

**Context**: Use npm to download and install CloudCMD from the registry, creating the necessary binaries.

**Command** ([[commands/npm-i-cloudcmd]]):
```bash
npm i cloudcmd
```

> This command installs the latest version (9.1.5 at the time of the report) into node_modules. Expected output includes progress logs and a summary confirming installation success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/npm-i-cloudcmd]]

## Tools Used

- [[tools/npm]]

## Tags

- nodejs
- installation
