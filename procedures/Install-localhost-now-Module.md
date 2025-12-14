---
tags:
  - setup
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-localhost-now]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.672Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d01bf724-fec7-44f9-be54-536cc73bfdd8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-localhost-now-Module

## Summary

This procedure installs the vulnerable 'localhost-now' Node.js module version 1.0.2 using npm, preparing the environment for exploiting a path traversal vulnerability in a local web server setup.

## Description

The localhost-now module is a simple Node.js tool for starting a local web server to serve HTML/JS files. Version 1.0.2 contains a path traversal flaw in lib/app.js line 17, where '../' strings are deleted but paths are not normalized, allowing bypasses like '..././' to access arbitrary files. This installation step is a prerequisite for running the server and demonstrating the exploit. It requires Node.js and npm installed on a Linux system.

## Requirements

1. Node.js v8.10.0 or compatible installed
2. NPM 5.6.0 or later
3. Internet access to npm registry
4. Local write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit before installation
- Pin versions to patched releases (avoid 1.0.2)
- Monitor npm install logs for suspicious packages

## Objectives

1. Download and install localhost-now@1.0.2
2. Verify module integrity for exploitation testing
3. Set up node_modules for server execution

## Instructions

### Step 1: Install the Module

**Context**: Use npm to fetch and install the specific vulnerable version from the registry.

**Command** ([[commands/npm-install-localhost-now]]):
```bash
npm install localhost-now@1.0.2
```

> This command downloads the package and dependencies, placing them in node_modules. Expected output includes progress bars and a summary like "added 1 package in 2s". Verify with `ls node_modules/localhost-now` to see lib/app.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-localhost-now]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js
- installation
