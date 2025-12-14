---
tags:
  - setup
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-buttle]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:30.884Z'
sub_techniques: []
id: 5a2bae53-6c31-4841-b165-bcbd9188b7b6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Install-Buttle-Module

## Summary

This procedure installs the vulnerable buttle Node.js module (version 0.2.0) using npm, setting up the environment for exploiting the stored XSS vulnerability in directory listings.

## Description

The buttle module is a simple static file and markdown server that relies on an outdated connect module for directory listings. Without sanitization, filenames can inject HTML. This step prepares the local environment by installing the package, which pulls in the vulnerable dependencies. It requires Node.js and npm to be installed on the system.

## Requirements

1. Node.js runtime installed
2. npm package manager available
3. Internet access for downloading the package

## Defense

Defensive measures and detection strategies:

- Use package managers with vulnerability scanning (e.g., npm audit)
- Avoid installing unmaintained packages like buttle 0.2.0
- Monitor for suspicious npm installations in logs

## Objectives

1. Install buttle to enable server setup
2. Prepare for file creation and server execution
3. Establish baseline for reproduction

## Instructions

### Step 1: Install the Package

**Context**: Use npm to fetch and install buttle from the registry.

**Command** ([[commands/npm-install-buttle]]):
```bash
npm i buttle
```

> This command installs buttle version 0.2.0 (default at time of vulnerability) into node_modules. Expected output includes download progress and confirmation of added dependencies like connect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used

- [[commands/npm-install-buttle]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node.js
