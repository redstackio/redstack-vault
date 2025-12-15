---
id: proc-uuid-1234-5678
tags:
  - node-js
  - installation
  - vulnerability-setup
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-deliver-or-else]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:05.761Z'
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
# Install-Vulnerable-deliver-or-else-Module

## Summary

This procedure installs the vulnerable deliver-or-else Node.js module version 1.0.0 using npm, setting up the environment for reproducing the path traversal vulnerability.

## Description

The deliver-or-else module (v1.0.0) contains a path traversal flaw in its file serving logic. This step obtains the module locally to create a test server. It requires Node.js and npm installed. Once installed, the module can be required in scripts to handle HTTP requests without proper path sanitization, allowing later exploitation.

## Requirements

1. Node.js runtime (v10+ recommended)
2. npm package manager
3. Internet access for downloading from npm registry

## Defense

Defensive measures and detection strategies:

- Use npm audit to check for known vulnerabilities before installation
- Pin module versions to patched releases (avoid 1.0.0)
- Monitor package.json for suspicious dependencies

## Objectives

1. Install the specific vulnerable version for testing
2. Prepare node_modules for server script
3. Verify installation without errors

## Instructions

### Step 1: Install the Module

**Context**: Use npm to fetch and install deliver-or-else, which will be used to set up the vulnerable server.

**Command** ([[commands/npm-install-deliver-or-else]]):
```bash
npm i deliver-or-else
```

> This command installs the module in the current directory's node_modules. Expected output includes download progress and confirmation like "added 1 package".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/npm-install-deliver-or-else]]

## Tools Used

- [[tools/npm]]

## Tags

- node-js
- installation
