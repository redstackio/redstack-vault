---
tags:
  - rce
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-tree-kill]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:32.671Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2307dd97-35a9-45a6-b637-55f57ba4b27f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Vulnerable-tree-kill-Module

## Summary

This procedure installs the vulnerable version 1.2.1 of the tree-kill Node.js module using npm, setting up the environment for exploiting the command injection vulnerability on Windows.

## Description

The tree-kill module is used to terminate processes in Node.js applications. Version 1.2.1 has a flaw in its Windows implementation where user input for PID/signal is concatenated directly into the 'taskkill' command without sanitization, enabling RCE. This step prepares the local Node.js project by installing the module, assuming a Windows environment with Node.js installed. Prerequisites include having npm available and a clean project directory.

## Requirements

1. Windows OS with Node.js and npm installed
2. Local access to command prompt or PowerShell
3. No internet restrictions for npm registry access

## Defense

Defensive measures and detection strategies:

- Use package managers with vulnerability scanning (e.g., npm audit)
- Pin dependencies to patched versions (>1.2.1)
- Monitor for installations of known vulnerable packages

## Objectives

1. Install tree-kill v1.2.1 to enable exploitation
2. Verify module availability in node_modules
3. Establish baseline for reproduction

## Instructions

### Step 1: Install the Module

**Context**: Use npm to fetch and install the specific vulnerable version.

**Command** ([[commands/npm-install-tree-kill]]):
```bash
npm i tree-kill@1.2.1
```

> This command installs tree-kill version 1.2.1, adding it to node_modules and updating package.json. Expected output includes download progress and confirmation like "added 1 package".

### Step 2: Verify Installation

**Context**: Check that the vulnerable version is installed.

**Command** ([[commands/npm-list-tree-kill]]):
```bash
npm list tree-kill
```

> Lists installed packages; look for tree-kill@1.2.1. Expected output: "tree-kill@1.2.1".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- [[commands/npm-install-tree-kill]]
- [[commands/npm-list-tree-kill]]

## Tools Used

- [[tools/npm]]

## Tags

- rce
- node-js
- setup
