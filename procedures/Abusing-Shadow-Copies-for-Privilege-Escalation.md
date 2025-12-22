---
id: 798ed535-73a6-4e7d-b1b3-04c41c2a56d4
name: Abusing-Shadow-Copies-for-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.017370+00:00'
updated_at: '2023-04-10T20:37:37.792409+00:00'
tactics:
  - '[[tactics/Impact|TA0040 - Impact]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
  - '[[techniques/Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
sub_techniques:
  - '[[sub-techniques/PowerShell Profile|T1546.013 - PowerShell Profile]]'
tags:
  - '[[tags/EoP - Abusing Shadow Copies]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/diskshadow-list-shadow-copies]]'
  - '[[commands/vssadmin-list-shadow-copies]]'
  - '[[commands/mklink-create-symlink-to-shadow-copy]]'
platforms:
  - Windows
tools: []
validated: true
---

# Abusing-Shadow-Copies-for-Privilege-Escalation

## Summary

This procedure demonstrates how to abuse Windows Volume Shadow Copies to escalate privileges by accessing previous versions of protected system files, such as the SAM hive, which may contain unpatched or vulnerable configurations allowing arbitrary code execution at SYSTEM level. It involves enumerating available shadow copies and creating symlinks to access restricted data, useful in post-exploitation scenarios where administrative access is already obtained but higher privileges are needed.

## Description

Volume Shadow Copies, managed by the Volume Shadow Copy Service (VSS), create point-in-time snapshots of files and volumes on Windows systems for backup and recovery purposes. Attackers with administrative privileges can exploit these snapshots to bypass file protections on critical system files (e.g., %SystemRoot%\System32\config\SAM) that are locked during normal operation. By linking to a shadow copy version where the file was writable or modifiable, an attacker can copy sensitive data like password hashes for offline cracking or replace files to achieve privilege escalation. This technique is particularly effective on systems with automatic shadow copy scheduling enabled, such as domain controllers or file servers, and requires no additional tools beyond built-in Windows utilities.

## Requirements

1. Administrative privileges on the target Windows system (local or remote via tools like PsExec).
2. Volume Shadow Copy Service (VSS) enabled and shadow copies present (check via System Protection settings).
3. Access to Command Prompt or PowerShell with elevated privileges.
4. Target system running Windows Vista or later (shadow copies introduced in Server 2003 but enhanced in later versions).

## Defense

Defensive measures and detection strategies:

- Disable or restrict shadow copy creation for non-essential volumes via Group Policy (Computer Configuration > Administrative Templates > System > Shadow Copies).
- Monitor for unusual VSS activity using Windows Event Logs (Event ID 8222 for shadow copy creation/deletion) and tools like Sysmon for process creation involving vssadmin, diskshadow, or mklink.
- Implement least privilege: Limit administrative access and use Just Enough Administration (JEA) in PowerShell to restrict command execution.
- Regularly audit and delete old shadow copies using vssadmin delete shadows to minimize available snapshots.
- Deploy endpoint detection and response (EDR) solutions to alert on symlink creation to GLOBALROOT or shadow copy paths.

## Objectives

1. Enumerate available shadow copies to identify accessible snapshots.
2. Create a directory symlink to a shadow copy path for bypassing file locks.
3. Access and manipulate protected system files from the shadow copy to achieve privilege escalation or data extraction.
4. Restore or replace files to execute code with elevated privileges.

## Instructions

### Step 1: Enumerate Shadow Copies Using VSSAdmin

**Context**: This step lists all existing shadow copies on the system to identify snapshot IDs and volumes, which is necessary to target a specific shadow copy for access. VSSAdmin is a built-in tool for managing VSS and requires admin rights; it provides details like creation time and volume association.

**Command** ([[commands/vssadmin-list-shadow-copies]]):
```cmd
vssadmin list shadows
```

> Run this in an elevated Command Prompt. The command queries the VSS service and returns a list of shadow copies, including paths like \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopyX. Note the shadow copy ID (e.g., HarddiskVolumeShadowCopy1) for the next steps. If no shadows exist, enable System Protection or wait for scheduled backups.

### Step 2: Enumerate Shadow Copies Using DiskShadow

**Context**: As an alternative to VSSAdmin, DiskShadow provides more detailed scripting capabilities for shadow copy management. This step confirms the list from Step 1 and exposes additional metadata, helping verify the usability of snapshots for file access.

**Command** ([[commands/diskshadow-list-shadow-copies]]):
```cmd
diskshadow list shadows all
```

> Execute in an elevated Command Prompt. DiskShadow enters an interactive mode but 'list shadows all' outputs comprehensive details including persistent shadows and exposed volumes. Cross-reference with VSSAdmin output to select a viable shadow copy volume.

### Step 3: Create Symlink to Shadow Copy and Access Files

**Context**: Once a shadow copy is identified, create a directory junction (symlink) to map a local path to the shadow copy's global root. This bypasses locks on live system files, allowing read/write access to previous versions (e.g., copying the SAM file for hash dumping).

**Command** ([[commands/mklink-create-symlink-to-shadow-copy]]):
```cmd
mklink /d c:\shadowcopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
```

> Replace 'HarddiskVolumeShadowCopy1' with the actual ID from previous steps. Run in an elevated Command Prompt. Success creates a symlink at C:\shadowcopy pointing to the snapshot. Navigate to C:\shadowcopy\Windows\System32\config to access files like SAM or SYSTEM, then copy them (e.g., copy SAM C:\temp\sam.hive) for further analysis or exploitation, such as using secretsdump.py for credential extraction.
