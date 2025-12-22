---
id: proc-load-notevil
tags:
  - nodejs
  - sandbox-escape
type: procedure
tools:
  - '[[tools/notevil]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/notevil-sandbox-escape-poc-nodejs]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.461Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Load Vulnerable notevil Module in Node.js

## Summary

This procedure loads the vulnerable notevil module (v1.3.2) in a Node.js environment, providing access to the safeEval function that can be exploited for sandbox escape.

## Description

The notevil module is a sandboxed eval alternative for JavaScript, using esprima to parse AST and restrict dangerous operations. Version 1.3.2 contains a flaw allowing bypass via constructor property manipulation. This step sets up the environment for payload execution, targeting Node.js runtimes where notevil is a dependency.

## Requirements

1. Node.js installed (v10+ recommended)
2. npm access to install packages
3. Local or online Node.js executor like RunKit

## Defense

Defensive measures and detection strategies:

- Upgrade to notevil v1.3.3+ or use vm2 for sandboxing
- Monitor npm installs for vulnerable versions
- Audit dependencies with tools like npm audit

## Objectives

1. Import safeEval for subsequent exploitation
2. Verify module vulnerability
3. Prepare for RCE payload

## Instructions

### Step 1: Install the Module

**Context**: Install the specific vulnerable version via npm.

**Command** ([[commands/notevil-install]]):
```bash
npm install notevil@1.3.2
```

> This installs notevil v1.3.2 locally. Expected output: package.json updated with dependency.

### Step 2: Require the Module

**Context**: Load the module in a script to access safeEval.

**Command** ([[commands/notevil-require]]):
```javascript
var safeEval = require('notevil');
```

> safeEval function is now available. Expected output: No errors, function defined.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/notevil-sandbox-escape-poc-nodejs]]

## Tools Used

- [[tools/notevil]]

## Tags

- nodejs
- sandbox-escape
