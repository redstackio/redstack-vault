---
tags:
  - node-js
  - installation
  - vulnerability
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-stattic]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:16.608Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b4a1c2f2-65a9-4ac2-8893-8e0f82205fa4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-Stattic-Module

## Summary

This procedure installs the vulnerable version 0.2.3 of the 'stattic' Node.js module, which suffers from a path traversal vulnerability, enabling subsequent exploitation to read arbitrary files.

## Description

The 'stattic' module is a simple static file server for Node.js. Version 0.2.3 lacks proper path validation in its index.js file, specifically in the path.join(options.folder, pathname) function around lines 70-75, allowing '../' sequences to escape the root directory. This procedure sets up the environment by installing the module via npm, preparing for server setup and exploitation. It assumes a Node.js environment and is typically run locally for testing or on a target server with package management access.

## Requirements

1. Node.js and npm installed on the system
2. Internet access to npm registry
3. Write permissions in the project directory

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit to detect known vulnerable dependencies
- Pin dependencies to secure versions in package.json
- Monitor npm install logs for suspicious module installations

## Objectives

1. Install the vulnerable stattic module to replicate the environment
2. Prepare node_modules for server configuration
3. Enable testing of path traversal impacts

## Instructions

### Step 1: Install the Module

**Context**: Fetch and install stattic version 0.2.3 from the npm registry, creating the necessary node_modules directory.

**Command** ([[commands/npm-install-stattic]]):
```bash
npm install stattic
```

> This command downloads and installs the module, outputting installation progress and adding it to package.json if not present. Expected output includes logs like "added 1 package" and confirmation of version 0.2.3.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-stattic]]

## Tools Used

- [[tools/npm]]

## Tags

- node-js
- installation
- vulnerability
