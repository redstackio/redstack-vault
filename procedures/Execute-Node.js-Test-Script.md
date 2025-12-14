---
tags:
  - execution
  - node-js
  - test
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/node-run-test-script]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.253Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: eacb2e8e-3a93-4ffe-a28d-c1ff2fdc889b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Execute-Node.js-Test-Script

## Summary

This procedure runs the JavaScript test script to execute path.join() and observe the traversal bypass in UNC paths, confirming the vulnerability allows escape from the designated network share.

## Description

Executing the script invokes path.join() with the UNC base and malicious input, where the normalize function strips the device name 'CON:' without the '.\\' prefix from the CVE fix, resolving relative paths from the share root and enabling access to files like private passwords on Windows file servers.

## Requirements

1. Prepared test.js script from previous procedure
2. Node.js runtime on Windows
3. Command prompt or terminal access

## Defense

Defensive measures and detection strategies:

- Run Node.js apps in sandboxed environments to limit file access
- Implement runtime hooks to intercept and validate path operations
- Use EDR tools to detect anomalous file reads on UNC shares

## Objectives

1. Trigger the path resolution to produce an escaped path
2. Capture console output for verification
3. Simulate real-world impact in file-serving scenarios

## Instructions

### Step 1: Run the Script

**Context**: Execute the test script to perform the vulnerable path join.

**Command** ([[commands/node-run-test-script]]):
```bash
node test.js
```

> This runs the getNetworkFile function. Expected output: '\\\\fileserver\\\\public\\\\private\\\\passwords.txt', showing escape from uploads.

### Step 2: Capture and Log Output

**Context**: Redirect output if needed for analysis.

**Command** ([[commands/node-run-with-log]]):
```bash
node test.js > output.txt
```

> Expected: File with traversed path, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/node-run-test-script]]
- [[commands/node-run-with-log]]

## Tools Used

- [[tools/Node.js]]

## Tags

- execution
- traversal-bypass
- unc
