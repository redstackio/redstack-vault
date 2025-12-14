---
tags:
  - node.js
  - windows
  - unc-path
  - permission-bypass
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/node-experimental-permission-unc-bypass]]'
platforms:
  - Windows
complexity: low
procedures:
  - '[[procedures/Reproduce-Node.js-UNC-Path-Permission-Bypass]]'
step_count: 1
techniques:
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Demonstrates bypassing Node.js experimental permission model restrictions to
  access UNC paths on Windows, allowing unintended file system reads on remote
  shares.
skill_level: intermediate
impact_level: low
id: 6f2d5e88-3200-4baa-914e-72c9070d2b9b
created_at: '2025-12-14T17:29:57.157Z'
updated_at: '2025-12-14T17:29:57.158Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Node.js Permission Bypass via UNC Path Manipulation

## Overview

This attack chain exploits a flaw in Node.js's experimental permission model, specifically in the handling of UNC paths on Windows. The vulnerability in the fs_permission.cc file's is_tree_granted function incorrectly assumes that paths starting with \\ have a fixed four-character prefix to ignore, leading to improper validation. Attackers can craft paths using Buffers to bypass restrictions, gaining access to remote shares (e.g., \\A\\C:\\Users) even when only local drives like C:\\* are permitted. The severity is low due to the need for experimental flags and specific Windows environments, but it highlights risks in permissioned Node.js deployments.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Node.js Environment] --> B[Execute Crafted UNC Path Access]
    B --> C[Access Remote Share]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Node.js v20.x or v22.x installed on Windows

### Target Environment

- Windows OS
- Node.js runtime with experimental permission model enabled
- File system access to local drives (e.g., C:\\*)

### Initial Access Requirements

- Local execution privileges on the Windows machine
- No network position required beyond local Node.js invocation
- Prior access to run Node.js commands

## Detailed Attack Procedures

### Step 1: Reproduce Permission Bypass
procedure: [[procedures/Reproduce-Node.js-UNC-Path-Permission-Bypass]]

**Objective**: Demonstrate the bypass by attempting to read a remote UNC directory despite local-only permissions.

**Instructions**: Enable the experimental permission model with read access limited to C:\\*, then use a Buffer to encode a crafted UNC path and call fs.readdirSync to list the directory contents.

Execute the bypass using [[commands/node-experimental-permission-unc-bypass]]:

```bash
node --experimental-permission --allow-fs-read=C:\\* -p "fs.readdirSync(Buffer.from('\\\\A\\\\C:\\Users'))"
```

**Expected Output**: A directory listing of the UNC path \\A\\C:\\Users (e.g., array of user directories) instead of an access denied error.

**Success Indicators**:
- No ERR_ACCESS_DENIED error is thrown
- Directory contents from the remote share are returned
- Confirmation via manual verification that the path resolves to a UNC resource

## Attack Chain Summary

### Key Achievements

1. Successful bypass of Node.js FS permission checks for UNC paths
2. Access to remote file shares without explicit grants
3. Reproduction of the vulnerability in a controlled environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01*
