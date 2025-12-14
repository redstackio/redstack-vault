---
id: proc-curling-install-001
name: Install-Vulnerable-Curling-Module
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.434Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - npm
  - installation
  - supply-chain
commands:
  - '[[commands/npm-install-curling]]'
platforms:
  - Node.js
tools:
  - '[[tools/npm]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Install-Vulnerable-Curling-Module

## Summary

This procedure installs the vulnerable version (1.1.0) of the Node.js curling module using npm, setting up the environment for exploiting a command injection vulnerability that allows arbitrary curl option injection.

## Description

The curling module is a Node.js wrapper for the curl binary, but version 1.1.0 contains a regex flaw (/[\/\`$&{}\[;\|]/g.test(command)) that fails to block spaces, file:// URLs, and flags like -o. Installing this module in a Node.js project enables subsequent exploitation for RCE. This step assumes a local Node.js environment and is the prerequisite for running malicious payloads. Expected outcomes include the module being available for require() in scripts, leading to potential host file manipulation.

## Requirements

1. Node.js runtime installed (version 10+ recommended)
2. npm package manager access (internet connection for registry)
3. Local project directory for installation

## Defense

Defensive measures and detection strategies:

- Use npm audit to scan for known vulnerabilities before installation
- Pin dependencies to secure versions in package.json
- Monitor npm install logs for suspicious package names

## Objectives

1. Install the vulnerable curling module to gain access to the flawed run() function
2. Prepare the environment for payload execution without triggering immediate alerts
3. Enable RCE in subsequent steps by loading the module

## Instructions

### Step 1: Install the Curling Module

**Context**: This step uses npm to fetch and install the vulnerable package from the public registry, adding it to the local node_modules.

**Command** ([[commands/npm-install-curling]]):
```bash
npm i curling
```

> This command installs curling@1.1.0 (vulnerable version). Expected output includes download progress, dependency resolution, and confirmation like "added 1 package". Verify by checking node_modules/curling exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/npm-install-curling]]

## Tools Used

- [[tools/npm]]

## Tags

- npm
- installation
- supply-chain
