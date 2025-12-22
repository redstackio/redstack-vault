---
id: proc-uuid-1
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
  - '[[commands/npm-install-public]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:11.813Z'
skill_level: intermediate
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

This procedure installs the vulnerable 'public' Node.js module version 0.1.2 from the npm registry, setting up the environment for exploiting a path traversal vulnerability in static file serving.

## Description

The 'public' module is a simple static file server for Node.js, but version 0.1.2 fails to sanitize pathnames, allowing traversal attacks. This step uses npm to download and install it locally, creating the node_modules directory with the vulnerable binary script. It requires Node.js and npm installed on a Linux system, and assumes local execution privileges. Successful installation enables the subsequent server launch and exploitation, leading to arbitrary file reads on the host.

## Requirements

1. Linux environment with Node.js v8.9.4 LTS and npm 5.6.0 installed
2. Internet access to the npm registry
3. Local write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit before installation
- Pin dependencies to patched versions (upgrade beyond 0.1.2 if available)
- Monitor npm install logs for suspicious package names

## Objectives

1. Download and install the 'public' module to prepare the vulnerable server
2. Verify the module's binary is accessible for execution
3. Set up the node_modules structure without errors

## Instructions

### Step 1: Install the Module

**Context**: Fetch the vulnerable package using npm to create the exploitable binary.

**Command** ([[commands/npm-install-public]]):
```bash
npm install public
```

> This command queries the npm registry, downloads version 0.1.2 (default latest vulnerable), and installs it into node_modules/public. Expected output includes package resolution logs and a summary like 'added 1 package'.

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

- path-traversal
- node-js
