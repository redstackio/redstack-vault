---
tags:
  - path-traversal
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-626]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.215Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: da668b5c-0b44-4f76-bda9-aa6ff3709433
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-626-Module

## Summary

This procedure installs the vulnerable 626 Node.js module (version 1.1.1) using npm, setting up the environment for exploiting its path traversal vulnerability in subsequent steps.

## Description

The 626 module is a third-party Node.js package with a path traversal flaw in its HTTP server implementation. Installing it creates the node_modules/626 directory containing the vulnerable index.js. This step requires npm and targets a local development or test environment running Node.js. Prerequisites include a clean Node.js setup; expected outcome is a successful installation without errors, preparing for server execution.

## Requirements

1. Node.js installed (v8.9.3 or later)
2. npm package manager (v5.5.1 or compatible)
3. Local filesystem write access for node_modules

## Defense

Defensive measures and detection strategies:

- Audit dependencies with tools like npm audit to identify vulnerable packages
- Use lockfiles (package-lock.json) to pin versions and avoid unvetted installs
- Monitor npm install logs for suspicious package names

## Objectives

1. Download and install the 626 module to replicate the vulnerable setup
2. Verify package integrity for exploitation testing
3. Prepare node_modules for server launch

## Instructions

### Step 1: Install the Module

**Context**: Use npm to fetch and install the specific vulnerable version of the 626 package.

**Command** ([[commands/npm-install-626]]):
```bash
npm install 626
```

> This command resolves the package from the npm registry, installs version 1.1.1 by default (vulnerable), and outputs logs showing dependency resolution and file creation in node_modules/626. Expected output includes 'added 1 package' confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-626]]

## Tools Used

- [[tools/npm]]

## Tags

- path-traversal
- node-js
- setup
