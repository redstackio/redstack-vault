---
id: proc-uuid-1
name: Install Hekto Module
tags:
  - setup
  - node-js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/install-hekto-module]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:27.121Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install Hekto Module

## Summary

This procedure installs the vulnerable hekto Node.js module version 0.2.3 using npm, preparing the environment for reproducing the open redirect vulnerability.

## Description

The hekto module is a Node.js package that exposes directories for HTTP CRUD operations. In version 0.2.3, it contains an open redirect flaw in its redirection logic. Installing it locally allows setup of a vulnerable server instance. This step is the initial setup for the attack chain, requiring Node.js and npm to be present. Expected outcome is a successful installation without dependencies conflicts, enabling subsequent server launch.

## Requirements

1. Node.js v9.6.1 or compatible installed
2. npm v5.6.0 or compatible
3. Internet access for package download
4. Local directory for installation

## Defense

Defensive measures and detection strategies:

- Audit npm installs for known vulnerable packages using tools like npm audit
- Use package lockfiles to pin versions and avoid untrusted modules
- Monitor for installations of obscure or unused packages in logs

## Objectives

1. Acquire the vulnerable hekto module
2. Set up node_modules for server execution
3. Prepare for vulnerability reproduction

## Instructions

### Step 1: Install via npm

**Context**: Fetch and install the hekto package from the npm registry.

**Command** ([[commands/install-hekto-module]]):
```bash
npm install hekto
```

> This command downloads and installs hekto version 0.2.3 (or latest if not specified), adding it to the local node_modules. Expected output includes progress logs and a summary confirming installation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/install-hekto-module]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js
