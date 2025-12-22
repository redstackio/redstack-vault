---
tags:
  - symlink
  - overwrite
  - abuse
type: procedure
tools:
  - '[[tools/symboliclink-testing-tools]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/create-symlink-quarantine]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:51.598Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2174674f-d65e-4a26-aa10-15accc35b57b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Symlink-in-Quarantine-for-Overwrite

## Summary

This procedure creates a symbolic link within the Acronis quarantine folder that points to a target system executable, allowing the subsequent SYSTEM-privileged copy to overwrite it with malicious content.

## Description

Exploiting the fact that the quarantine folder is user-writable, a symlink is created from a expected quarantine path (e.g., Quarantine\ProgramData\ransomware_sim.exe) to a system file like C:\Windows\SysWOW64\dpnsvr.exe. When the service copies the detected file as SYSTEM, it follows the symlink and overwrites the target. This abuses the lack of path validation in anti_ransomware_service.exe.

## Requirements

1. Quarantine folder created and writable
2. CreateSymlink.exe from symboliclink-testing-tools available
3. Detected ransomware file ready
4. Target system file identified (e.g., a service binary)

## Defense

Defensive measures and detection strategies:

- Implement symlink following restrictions in services (e.g., via SeCreateSymbolicLinkPrivilege checks)
- Audit file operations in protected directories like SysWOW64
- Use filesystem monitoring tools like Sysmon to detect symlink creations

## Objectives

1. Link quarantine path to system file
2. Enable arbitrary overwrite as SYSTEM
3. Avoid detection during setup

## Instructions

### Step 1: Execute Symlink Creation

**Context**: Use the tool to create the symlink in the quarantine directory.

**Command** ([[commands/create-symlink-quarantine]]):
```cmd
CreateSymlink.exe "C:\Acronis Active Protection Storage\Quarantine\ProgramData\ransomware_sim.exe" "C:\Windows\SysWOW64\dpnsvr.exe"
```

> Creates the symlink; verify with dir /a:l on the quarantine path.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/create-symlink-quarantine]]

## Tools Used

- [[tools/symboliclink-testing-tools]]

## Tags

- symlink
- overwrite
- abuse
