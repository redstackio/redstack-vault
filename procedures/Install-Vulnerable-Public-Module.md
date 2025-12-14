---
id: proc-uuid-1
tags:
  - nodejs
  - installation
  - vulnerable-module
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-public]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:02.888Z'
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
# Install-Vulnerable-Public-Module

## Summary

This procedure installs the vulnerable 'public' Node.js module (version 0.1.3) using npm, setting up the environment for reproducing the stored XSS vulnerability in directory listings.

## Description

The 'public' module is a static file server for Node.js that enables directory indexing similar to Apache. In version 0.1.3, it fails to sanitize filenames, allowing XSS injection. This step obtains the module locally or globally, placing it in node_modules for execution. Prerequisites include Node.js and npm installed on the system. Expected outcome: Module ready for server launch, enabling the full exploit chain.

## Requirements

1. Node.js runtime installed (v8+ recommended)
2. npm package manager available
3. Write access to the current directory for node_modules
4. Internet access to npm registry

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit or Snyk to detect outdated modules
- Pin dependencies to secure versions in package.json
- Monitor npm install logs for suspicious package names

## Objectives

1. Acquire the vulnerable module for local exploitation testing
2. Prepare environment for file creation and server execution
3. Enable reproduction of the XSS in a controlled setup

## Instructions

### Step 1: Install the Module

**Context**: Use npm to fetch and install the 'public' package, which will be used to serve files with the XSS flaw.

**Command** ([[commands/npm-install-public]]):
```bash
npm install public
```

> This command downloads version 0.1.3 (vulnerable) by default if not specified, outputs installation progress, and creates node_modules/public with the bin/public executable. Verify with ls node_modules/public.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-public]]

## Tools Used

- [[tools/npm]]

## Tags

- nodejs
- installation
