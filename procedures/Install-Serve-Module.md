---
tags:
  - installation
  - node-js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-serve]]'
platforms:
  - Node.js
techniques:
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: dc78e62c-6cba-4279-a84b-a45c0a039df6
created_at: '2025-12-14T03:15:41.895Z'
updated_at: '2025-12-14T03:15:41.895Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Install-Serve-Module

## Summary

This procedure installs the vulnerable serve Node.js module using npm, enabling the setup of a static file server prone to stored XSS in directory listings.

## Description

The serve module (versions 7.0.1 to 10.0.1) is a popular static file server for Node.js. Installing it locally allows reproduction of the XSS vulnerability where malicious filenames inject JavaScript into HTML-rendered directory listings. This step is the foundation for hosting files that can exploit the lack of sanitization. Prerequisites include Node.js and npm installed on the system.

## Requirements

1. Node.js runtime installed
2. npm package manager available
3. Internet access to npm registry

## Defense

Defensive measures and detection strategies:

- Use package managers with vulnerability scanners like npm audit
- Pin versions to patched releases (serve >10.0.1)
- Monitor npm installations in CI/CD pipelines

## Objectives

1. Acquire the vulnerable serve module
2. Prepare environment for server execution
3. Enable static file serving with directory listings

## Instructions

### Step 1: Install via npm

**Context**: Fetch and install the serve package, targeting a vulnerable version if needed (default installs latest, but specify for repro).

**Command** ([[commands/npm-install-serve]]):
```bash
npm i serve
```

> This command downloads serve from the npm registry and adds it to node_modules. Expected output includes installation progress and confirmation of serve@version (e.g., 7.0.1).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-serve]]

## Tools Used

- [[tools/npm]]

## Tags

- installation
- node-js
