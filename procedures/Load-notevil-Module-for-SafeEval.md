---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Load-notevil-Module-for-SafeEval
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.399Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - sandbox-escape
  - nodejs
commands:
  - '[[commands/require-notevil]]'
platforms:
  - Node.js
tools:
  - '[[tools/notevil]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Load-notevil-Module-for-SafeEval

## Summary

This procedure loads the vulnerable notevil module (version 1.3.2) in a Node.js environment, providing access to the safeEval function intended for restricted JavaScript evaluation but exploitable for sandbox escape.

## Description

The notevil module uses esprima to parse JavaScript into an AST and evaluates it in a wrapped context to prevent access to global objects like Function or process. However, version 1.3.2 contains a bypass allowing prototype manipulation to escape restrictions. This step sets up the environment for crafting and executing payloads leading to RCE. Prerequisites include Node.js installed and npm access to install notevil.

## Requirements

1. Node.js runtime (v10+ recommended for compatibility)
2. npm package manager
3. Local file system write access for script execution

## Defense

Defensive measures and detection strategies:

- Audit dependencies for vulnerable versions of notevil and upgrade to patched releases
- Implement runtime monitoring for unexpected module loads (e.g., util in safe contexts)
- Use AST validation tools beyond esprima to detect prototype manipulations

## Objectives

1. Obtain safeEval function for payload testing
2. Verify module loads without errors
3. Prepare for sandbox bypass exploitation

## Instructions

### Step 1: Install notevil

**Context**: Install the specific vulnerable version via npm to reproduce the issue.

**Command** ([[commands/npm-install-notevil]]):
```bash
npm install notevil@1.3.2
```

> This installs notevil version 1.3.2 locally. Expected output: Package installed in node_modules.

### Step 2: Require the Module

**Context**: Load the module in a Node.js script to access safeEval.

**Command** ([[commands/require-notevil]]):
```javascript
var safeEval = require("notevil");
```

> This assigns the safeEval function to a variable. Expected output: No errors; safeEval is a function.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/require-notevil]]

## Tools Used

- [[tools/notevil]]

## Tags

- [[sandbox-escape]]
- [[nodejs]]
