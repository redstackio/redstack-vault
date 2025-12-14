---
tags:
  - installation
  - supply-chain
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-logkitty]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:32.505Z'
sub_techniques: []
id: d887d129-7187-4a0c-be50-737c2d73fb10
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Vulnerable-Logkitty-Module

## Summary

This procedure installs the vulnerable version (0.7.0) of the logkitty Node.js module using npm, setting up the environment necessary for exploiting the RCE vulnerability in its ADB command handling.

## Description

Logkitty is a CLI tool for displaying Android and iOS logs, but version 0.7.0 contains a command injection flaw in src/android/adb.ts at line 55, where user-supplied app names are interpolated into shell commands without sanitization. This procedure uses npm to fetch and install this specific vulnerable version, enabling subsequent exploitation on a Node.js-enabled Linux system with ADB available.

## Requirements

1. Node.js and npm installed
2. Internet access for npm registry
3. Linux shell environment

## Defense

Defensive measures and detection strategies:

- Pin dependencies to patched versions (e.g., logkitty >0.7.1)
- Use npm audit to scan for known vulnerabilities
- Monitor package installations in CI/CD pipelines

## Objectives

1. Install logkitty v0.7.0
2. Prepare vulnerable environment for RCE testing
3. Verify installation integrity

## Instructions

### Step 1: Install Specific Vulnerable Version

**Context**: Use npm to install logkitty at the exact vulnerable version.

**Command** ([[commands/npm-install-logkitty]]):
```bash
npm i logkitty@0.7.0
```

> This installs logkitty version 0.7.0 into node_modules. Expected output includes download progress, installation confirmation, and addition to package.json if applicable.

### Step 2: Verify Installation

**Context**: Confirm the version to ensure vulnerability is present.

**Command**:
```bash
npm list logkitty
```

> Outputs the installed version; look for 0.7.0 to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-logkitty]]

## Tools Used

- [[tools/npm]]

## Tags

- [[installation]]
- [[supply-chain]]
