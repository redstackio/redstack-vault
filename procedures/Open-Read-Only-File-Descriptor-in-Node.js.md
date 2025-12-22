---
id: proc-nodejs-open-readonly-fd-001
tags:
  - node.js
  - file-descriptor
  - permission-bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/node-fs-open-read-only]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:57.076Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Open-Read-Only-File-Descriptor-in-Node.js

## Summary

This procedure opens a target file in read-only mode using Node.js fs.open() to obtain a file descriptor that can later be used to bypass write permission checks in the experimental permission model.

## Description

In Node.js versions 20 and 21 with the experimental permission model enabled (e.g., via --allow-fs-read), file system operations are restricted based on paths. However, opening a file in read-only mode ('r') provides a file descriptor that is not checked for write permissions when used in descriptor-based functions like fchown or fchmod. This step sets up the bypass by acquiring the descriptor without triggering write checks, applicable in scenarios where the application relies on the permission model for security.

## Requirements

1. Node.js 20 or 21 installed with experimental permission model
2. --allow-fs-read flag enabled, but --allow-fs-write disabled
3. Access to the target file path
4. Local execution environment for Node.js scripts

## Defense

Defensive measures and detection strategies:

- Disable or avoid using the experimental permission model in production
- Monitor for unexpected fs.open calls with read-only modes on sensitive files
- Implement file descriptor usage auditing in Node.js applications

## Objectives

1. Obtain a valid read-only file descriptor for a target file
2. Avoid triggering permission model write restrictions
3. Prepare for subsequent descriptor-based modifications

## Instructions

### Step 1: Open the Target File in Read-Only Mode

**Context**: Use fs.openSync (or async variant) with 'r' flag to get a descriptor, ensuring only read permissions are requested.

**Command** ([[commands/node-fs-open-read-only]]):
```javascript
const fs = require('fs');
const fd = fs.openSync('target-file.txt', 'r');
console.log('File descriptor:', fd);
```

> This command opens 'target-file.txt' in read-only mode and logs the descriptor (e.g., 3). Success is indicated by no errors and a positive integer descriptor. Close the descriptor after use with fs.closeSync(fd) to avoid leaks.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/node-fs-open-read-only]]

## Tools Used


## Tags

- [[node.js]]
- [[file-descriptor]]
- [[permission-bypass]]
