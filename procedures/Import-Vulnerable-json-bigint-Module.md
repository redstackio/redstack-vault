---
id: proc-uuid-1
tags:
  - dos
  - node-js
  - setup
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/install-json-bigint]]'
  - '[[commands/node-require-module]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.307Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Import Vulnerable json-bigint Module

## Summary

This procedure sets up a Node.js environment by installing and importing the vulnerable json-bigint module (v0.3.1), preparing for prototype pollution exploitation leading to DoS.

## Description

In Node.js applications, third-party modules like json-bigint are commonly required for handling large JSON numbers. Version 0.3.1 contains a vulnerability (CVE-2020-8237) where parsing JSON with __proto__ keys pollutes the global Object prototype, affecting dependent libraries like bignumber.js. This step ensures the vulnerable module is loaded, enabling the attack on applications processing untrusted input. Prerequisites include Node.js installed and npm access.

## Requirements

1. Node.js v10+ installed
2. npm package manager available
3. Target application or test script using json-bigint for JSON parsing

## Defense

Defensive measures and detection strategies:

- Upgrade to json-bigint v1.0.0 or later, which patches __proto__ handling
- Use Object.create(null) for parsing to avoid prototype pollution
- Monitor for unusual memory usage or hangs in Node.js processes

## Objectives

1. Install and load the vulnerable module without errors
2. Verify compatibility with bignumber.js
3. Set stage for malicious input injection

## Instructions

### Step 1: Install Vulnerable Module

**Context**: Install json-bigint v0.3.1 specifically to exploit the known vulnerability.

**Command** ([[commands/install-json-bigint]]):
```bash
npm install json-bigint@0.3.1
```

> This installs the exact vulnerable version. Expected output: Package installation success message.

### Step 2: Require Module in Script

**Context**: Import the module in a Node.js script to confirm loading.

**Command** ([[commands/node-require-module]]):
```bash
node -e "const JSONbig = require('json-bigint'); console.log('Loaded:', JSONbig);"
```

> This requires the module and logs it. Expected output: Module object printed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/install-json-bigint]]
- [[commands/node-require-module]]

## Tools Used


## Tags

- dos
- node-js
- prototype-pollution
