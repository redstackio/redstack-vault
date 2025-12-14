---
tags:
  - setup
  - node-js
  - npm
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-expressjs-ip-control]]'
  - '[[commands/npm-install-express]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.581Z'
sub_techniques: []
id: cfecf68f-dbed-44c7-b5de-3afe7339ec72
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-expressjs-ip-control-Module

## Summary

This procedure installs the vulnerable expressjs-ip-control Node.js module, which is used for IP-based access control in Express applications but suffers from a flaw allowing header-based bypasses.

## Description

In the context of testing the expressjs-ip-control vulnerability, this step sets up the project dependencies by installing the module via npm. The module provides middleware for whitelisting IPs but trusts the client-supplied X-Forwarded-For header without validation, enabling spoofing attacks. Prerequisites include a Node.js environment with npm initialized (run `npm init -y` if needed). Expected outcome: The module is ready for integration into an Express app to demonstrate the authorization bypass.

## Requirements

1. Node.js and npm installed on the local machine
2. A project directory with package.json (create via `npm init` if absent)
3. Internet access for package download

## Defense

Defensive measures and detection strategies:

- Use audited and maintained packages; avoid unmaintained modules like expressjs-ip-control
- Implement proper proxy validation for headers like X-Forwarded-For (e.g., trust only reverse proxy IPs)
- Monitor npm installs for vulnerable packages using tools like npm audit

## Objectives

1. Prepare the vulnerable module for POC setup
2. Ensure dependencies are available for Express integration
3. Validate installation to prevent runtime errors

## Instructions

### Step 1: Install the Vulnerable Module

**Context**: This installs the core vulnerable component used for IP whitelisting.

**Command** ([[commands/npm-install-expressjs-ip-control]]):
```bash
npm i expressjs-ip-control
```

> This command fetches and installs the expressjs-ip-control package from the npm registry. Expected output includes progress logs and a summary confirming addition to dependencies.

### Step 2: Install Express if Needed

**Context**: Resolves any missing Express dependency errors during POC execution.

**Command** ([[commands/npm-install-express]]):
```bash
npm i express
```

> Installs the Express web framework. Expected output: Installation confirmation without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-expressjs-ip-control]]
- [[commands/npm-install-express]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js
- npm
