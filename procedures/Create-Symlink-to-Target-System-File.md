---
id: acronis-create-symlink
tags:
  - lpe
  - symlink
  - exploitation
type: procedure
tools:
  - '[[tools/CreateSymlink]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/CreateSymlink-create-log-symlink]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.751Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Symlink-to-Target-System-File

## Summary

This procedure creates a symbolic link from the vulnerable log file path in Acronis True Image's temp directory to a protected system file, enabling redirection of privileged writes during the update process.

## Description

The Acronis update installer (setupapp_amd64.exe) runs with SYSTEM privileges and writes to %temp%\Acronis\DriverSetup\inst.log without validating symlinks or paths. By creating a symlink at this location pointing to a sensitive file like C:\Windows\System32\drivers\pci.sys, an attacker can cause the installer to overwrite the target file. This leads to arbitrary file modification and potential local privilege escalation to SYSTEM. Requires the parent directory to be prepared beforehand.

## Requirements

1. Prepared %temp%\Acronis directory
2. Access to CreateSymlink tool or equivalent (e.g., mklink in elevated context, but tool used here)
3. Local user permissions to create symlinks in %temp%
4. Target file exists and is writable via symlink (e.g., pci.sys)

## Defense

Defensive measures and detection strategies:

- Enable symlink restrictions via registry (e.g., DisableLinkCreate in HKLM\SYSTEM\CurrentControlSet\Control\Session Manager)
- Use file integrity monitoring to detect changes to system drivers
- Log and alert on symlink creations in temp directories

## Objectives

1. Redirect log writes to overwrite protected files
2. Set up for privilege escalation via file corruption
3. Achieve arbitrary code execution potential post-overwrite

## Instructions

### Step 1: Establish Symlink

**Context**: Use the CreateSymlink tool to link the log path to the target system driver, preparing for the overwrite during installation.

**Command** ([[commands/CreateSymlink-create-log-symlink]]):
```cmd
CreateSymlink %temp%\Acronis\DriverSetup\inst.log C:\Windows\System32\drivers\pci.sys
```

> This creates a symbolic link (reparse point) from the source to the target. Expected output: Success confirmation; verify with dir /aL %temp%\Acronis\DriverSetup.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/CreateSymlink-create-log-symlink]]

## Tools Used

- [[tools/CreateSymlink]]

## Tags

- lpe
- symlink
- exploitation
