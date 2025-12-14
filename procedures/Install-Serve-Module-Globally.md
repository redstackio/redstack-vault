---
id: proc-398285-install-serve
tags:
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/yarn]]'
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/yarn-global-add-serve]]'
  - '[[commands/npm-install-serve-global]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.936Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Serve-Module-Globally

## Summary

This procedure installs the vulnerable serve Node.js module globally using yarn or npm, enabling the hosting of static directories with the exploitable directory listing feature for XSS injection.

## Description

In the context of exploiting the stored XSS in serve v9.6.0, global installation provides the serve command-line tool. This sets up the environment for serving files where filenames are rendered unsanitized in HTML, allowing subsequent payload injection and execution. Prerequisites include Node.js v10.9.0 or later installed on the system.

## Requirements

1. Node.js runtime installed (v10.9.0+)
2. Internet access for package download
3. Terminal access with package manager permissions

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit to detect outdated modules
- Restrict global installations and review dependencies for known XSS issues
- Monitor for unusual package installations in logs

## Objectives

1. Prepare the vulnerable serve tool for directory hosting
2. Enable command-line access to start the HTTP server
3. Set stage for XSS exploitation via directory listing

## Instructions

### Step 1: Install with Yarn

**Context**: Use yarn to globally add the serve package, targeting version 9.6.0 for vulnerability reproduction.

**Command** ([[commands/yarn-global-add-serve]]):
```bash
yarn global add serve
```

> This command downloads and installs serve globally, making the 'serve' CLI available. Expected output includes success messages and PATH updates.

### Step 2: Alternative Install with NPM

**Context**: Fallback to npm if yarn is unavailable, ensuring global accessibility.

**Command** ([[commands/npm-install-serve-global]]):
```bash
npm i serve -g
```

> Installs serve globally via npm. Expected output confirms installation and availability as a command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/yarn-global-add-serve]]
- [[commands/npm-install-serve-global]]

## Tools Used

- [[tools/yarn]]
- [[tools/npm]]

## Tags

- node.js
- installation
