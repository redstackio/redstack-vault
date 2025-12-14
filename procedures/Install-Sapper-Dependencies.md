---
id: proc-002
tags:
  - setup
  - dependencies
  - npm
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-dependencies]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.577Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Install-Sapper-Dependencies

## Summary

This procedure installs the project dependencies for the Sapper template, including the vulnerable version 0.27.10, to fully set up the environment for path traversal exploitation.

## Description

After cloning, dependencies must be fetched to enable Sapper's runtime. This step pulls in Sapper, Svelte, and other packages, creating a Node.js environment vulnerable to static file path traversal via the /client/ endpoint. Run this in the cloned directory.

## Requirements

1. Cloned Sapper project directory
2. Node.js v10.19.0 and NPM 6.13.4 installed
3. Internet access for package downloads

## Defense

Defensive measures and detection strategies:

- Pin dependency versions to avoid vulnerable releases
- Scan package.json for known vulnerable packages like Sapper <0.28

## Objectives

1. Install Sapper v0.27.10 and dependencies
2. Prepare node_modules for server execution
3. Enable vulnerable static file serving

## Instructions

### Step 1: Install Packages

**Context**: Fetch and install all required Node.js packages from package.json.

**Command** ([[commands/npm-install-dependencies]]):
```bash
npm i
```

> This runs in install mode, downloading packages. Expected output: List of installed modules, including Sapper, with no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-dependencies]]

## Tools Used

- [[tools/npm]]

## Tags

- [[setup]]
- [[dependencies]]
- [[tools/npm]]

---
