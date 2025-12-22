---
id: 123e4567-e89b-12d3-a456-426614174001
name: Install-Vulnerable-hnzserver-Module
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.472Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - node-js
  - installation
  - vulnerable-package
commands:
  - '[[commands/npm-install-hnzserver]]'
platforms:
  - Linux
  - Node.js
tools:
  - '[[tools/npm]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Install-Vulnerable-hnzserver-Module

## Summary

This procedure installs the vulnerable hnzserver Node.js module (version 2.0.6) globally using npm, setting up the environment for reproducing the path traversal vulnerability in a local static file server scenario.

## Description

The hnzserver module is a simple static file server for Node.js that, in version 2.0.6, suffers from a path traversal flaw due to inadequate input sanitization. This procedure focuses on the initial setup by installing the module globally, making the 'hnzserver' command available for execution. It is typically used in penetration testing or vulnerability research to simulate an environment where the server can be run and exploited. Prerequisites include a Linux system with Node.js and npm (version 6.9 or later) installed. Expected outcomes include successful global installation without errors, enabling subsequent server startup.

## Requirements

1. Linux operating system with Node.js runtime
2. npm package manager (version 6.9)
3. Internet access for downloading the package from npm registry
4. Terminal access with sufficient permissions for global installation

## Defense

Defensive measures and detection strategies:

- Audit and restrict global npm installations via package managers or firewalls
- Use vulnerability scanners like npm audit to detect known vulnerable packages before installation
- Monitor system logs for unauthorized npm installs

## Objectives

1. Prepare the attack environment by installing the affected hnzserver module
2. Ensure the module version 2.0.6 is installed for accurate reproduction
3. Verify command availability for server execution

## Instructions

### Step 1: Install hnzserver Globally

**Context**: Use npm to download and install the vulnerable package system-wide, targeting version 2.0.6 implicitly via the latest available at the time of the report.

**Command** ([[commands/npm-install-hnzserver]]):
```bash
npm install -g hnzserver
```

> This command fetches the hnzserver package from the npm registry and installs it globally. Expected output includes progress logs, dependency resolutions, and a confirmation message like "+ hnzserver@2.0.6 added 1 package". Verify by running `hnzserver --version` to confirm v2.0.6.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-hnzserver]]

## Tools Used

- [[tools/npm]]

## Tags

- node-js
- installation
- vulnerable-package
