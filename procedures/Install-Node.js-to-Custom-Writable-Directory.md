---
id: proc-nodejs-install-writable
tags:
  - node.js
  - installation
  - permissions
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/mkdir-tools-directory]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:29:09.968Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
---
# Install-Node.js-to-Custom-Writable-Directory

## Summary

This procedure installs Node.js on Windows to a custom directory like C:\tools, exploiting the installer's failure to strip inherited permissions from the drive root, resulting in full write access for all local users (BUILTIN\Users) and automatic addition to the system PATH.

## Description

The Node.js Windows installer (e.g., version 14.17.0) does not properly secure the installation directory when using a custom path. Permissions inherit from C:\, granting BUILTIN\Users full control (including Create Files and Append Data). The directory is added to the PATH, enabling exploitation by unprivileged users. This sets the stage for privilege escalation via file drops or DLL placement. Prerequisites include admin rights for install but allows low-priv users to exploit post-install.

## Requirements

1. Windows OS with admin access for installation
2. Download access to Node.js installer from https://nodejs.org/en/download/
3. Local unprivileged user for later exploitation
4. PowerShell or Command Prompt access

## Defense

Defensive measures and detection strategies:

- Manually adjust ACLs post-install to remove BUILTIN\Users write access (e.g., via icacls)
- Monitor PATH changes and directory writes in sensitive paths using Windows Event Logs (Event ID 4656/4663)
- Use AppLocker or WDAC to restrict execution from non-standard directories
- Audit installer behaviors and verify permissions before adding to PATH

## Objectives

1. Establish a writable, PATH-exposed Node.js installation directory
2. Confirm inheritance of permissive ACLs from drive root
3. Enable subsequent hijacking by unprivileged attackers

## Instructions

### Step 1: Create Custom Directory

**Context**: Ensure the target directory exists; the installer may create it, but manual creation allows permission verification.

**Command** ([[commands/mkdir-tools-directory]]):
```powershell
mkdir C:\tools
```

> Creates C:\tools if it doesn't exist. Expected output: Directory created without errors.

### Step 2: Download and Install Node.js

**Context**: Use the GUI installer to target the custom directory, selecting options for necessary tools.

**Instructions**: Download the Windows installer (.msi) from https://nodejs.org/en/download/. Run it, choose custom setup, set path to C:\tools, and check 'Automatically install the necessary tools'. Complete installation.

> No command; GUI-based. Expected output: Installation success; Node.js and npm in C:\tools.

### Step 3: Verify Permissions and PATH

**Context**: Inspect ACLs to confirm BUILTIN\Users has full control and PATH update.

**Instructions**: Use `icacls C:\tools` to check permissions (look for BUILTIN\Users:(OI)(CI)F). Restart shell and run `echo $env:PATH` (PowerShell) to confirm C:\tools inclusion.

> Expected output: Permissions show full control; PATH includes C:\tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Registry Run Keys - Startup Folder]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-tools-directory]]

## Tools Used


## Tags

- node.js
- windows
- permissions
