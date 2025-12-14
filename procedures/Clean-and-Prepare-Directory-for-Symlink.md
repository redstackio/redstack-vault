---
id: acronis-prep-symlink-dir
tags:
  - lpe
  - symlink
  - preparation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rmdir-remove-acronis-directory]]'
  - '[[commands/mkdir-create-acronis-directory]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.755Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Clean-and-Prepare-Directory-for-Symlink

## Summary

This procedure removes any existing Acronis DriverSetup directory in the temp folder and creates the necessary parent directory to set up for a symlink attack during the Acronis True Image update process.

## Description

In the context of exploiting the Acronis True Image update vulnerability, this preparation step ensures a clean environment in the user-writable %temp% path. The update installer writes to %temp%\Acronis\DriverSetup\inst.log with SYSTEM privileges without path validation, making symlink attacks possible. Cleaning prevents interference from prior installations, and creating the parent directory allows the symlink to be placed correctly. This is a prerequisite for redirecting log writes to protected files like system drivers.

## Requirements

1. Local user access on Windows with write permissions to %temp%
2. Command prompt or PowerShell available
3. Acronis True Image installed (Version 2021, Build 32010)

## Defense

Defensive measures and detection strategies:

- Monitor file system changes in %temp% directories via EDR tools
- Restrict symlink creation privileges using AppLocker or similar
- Audit Acronis update processes for unexpected file operations

## Objectives

1. Remove existing directories to avoid symlink creation failures
2. Establish directory structure for exploitation
3. Prepare for safe symlink placement without errors

## Instructions

### Step 1: Remove Existing Directory

**Context**: Deletes the %temp%\Acronis\DriverSetup directory and its contents to clear the path for the new symlink.

**Command** ([[commands/rmdir-remove-acronis-directory]]):
```cmd
rmdir /S /Q %temp%\Acronis\DriverSetup
```

> This command recursively (/S) and quietly (/Q) removes the directory. Expected output: None if successful; error if directory doesn't exist or permissions denied.

### Step 2: Create Parent Directory

**Context**: Creates the %temp%\Acronis folder as the parent for the DriverSetup symlink.

**Command** ([[commands/mkdir-create-acronis-directory]]):
```cmd
mkdir %temp%\Acronis
```

> This creates the directory if it doesn't exist. Expected output: None if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/rmdir-remove-acronis-directory]]
- [[commands/mkdir-create-acronis-directory]]

## Tools Used


## Tags

- lpe
- symlink
- preparation
