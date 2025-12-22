---
id: proc-001
tags:
  - npm
  - installation
  - dependency
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/install-treekill-module]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:20.599Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Vulnerable-treekill-Module

## Summary

This procedure installs the vulnerable version (1.0.0) of the treekill Node.js module using npm, setting up the environment for exploiting the RCE vulnerability on Windows.

## Description

The treekill module is used to kill processes by PID in Node.js applications. Version 1.0.0 contains a command injection flaw on Windows due to direct concatenation of user input into taskkill. This procedure reproduces the setup from the HackerOne report #703415 by installing the module locally, enabling subsequent exploitation via a PoC script. It requires Node.js and npm installed on a Windows system.

## Requirements

1. Windows OS with Node.js runtime
2. npm package manager
3. Internet access to npm registry

## Defense

Defensive measures and detection strategies:

- Audit dependencies with tools like npm audit
- Pin versions to patched releases (update to treekill >1.0.0)
- Monitor npm installations in CI/CD pipelines

## Objectives

1. Install treekill@1.0.0
2. Prepare environment for PoC execution
3. Enable vulnerability reproduction

## Instructions

### Step 1: Install the Module

**Context**: Fetch and install the vulnerable treekill package from the npm registry.

**Command** ([[commands/install-treekill-module]]):
```bash
npm i treekill
```

> This command installs treekill version 1.0.0 by default if no version is specified. Expected output includes package resolution, download progress, and a success message confirming installation in node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/install-treekill-module]]

## Tools Used

- [[tools/npm]]

## Tags

- npm
- installation
- node-js
