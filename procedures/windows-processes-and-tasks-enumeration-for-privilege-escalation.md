---
type: procedure
description: >-
  Enumerate running processes, services, scheduled tasks, and startup programs
  on a Windows system to identify potential privilege escalation vectors such as
  misconfigured services or tasks running as SYSTEM.
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Process Discovery|T1057 - Process Discovery]]'
  - '[[techniques/System Service Discovery|T1007 - System Service Discovery]]'
  - '[[techniques/Scheduled Task/Job|T1053 - Scheduled Task/Job]]'
  - >-
    [[techniques/Boot or Logon Autostart Execution|T1547 - Boot or Logon
    Autostart Execution]]
  - '[[techniques/Service Execution|T1035 - Service Execution]]'
  - '[[techniques/Process Injection|T1055 - Process Injection]]'
sub_techniques:
  - '[[techniques/Process Discovery/Process Discovery|T1057.001]]'
  - '[[techniques/Scheduled Task/Job/Scheduled Task|T1053.005]]'
  - >-
    [[techniques/Boot or Logon Autostart Execution/Registry Run Keys / Startup
    Folder|T1547.001]]
tags:
  - windows
  - privilege-escalation
  - enumeration
  - processes
  - services
  - scheduled-tasks
  - startup-programs
commands:
  - '[[commands/check-powershell-version]]'
  - '[[commands/list-system-user-processes-tasklist]]'
  - '[[commands/list-run-once-programs-registry-hkcu]]'
  - '[[commands/list-startup-programs-wmic]]'
  - '[[commands/list-startup-programs-all-users-start-menu]]'
  - '[[commands/list-startup-programs-current-user-start-menu]]'
  - '[[commands/list-startup-programs-registry-hkcu]]'
  - '[[commands/list-startup-programs-registry-hklm]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-processes-and-tasks-enumeration-for-privilege-escalation

## Summary

This procedure enumerates running processes, services, scheduled tasks, and startup programs on a Windows system to uncover potential privilege escalation opportunities. By identifying processes and tasks running with elevated privileges like SYSTEM, attackers can spot misconfigurations, vulnerable services, or injectable processes that allow escalation from low-privileged access to higher privileges, enabling further compromise of sensitive resources.

## Description

In a privilege escalation scenario on Windows, enumerating system processes, services, and scheduled tasks is crucial for discovering exploitable artifacts. This involves querying process owners to find SYSTEM-level executables suitable for injection (T1055), reviewing services for weak permissions (T1035), inspecting scheduled tasks for those executable by privileged accounts (T1053), and checking autostart locations for persistence mechanisms (T1547). The procedure assumes initial low-privileged shell access and uses built-in Windows tools like tasklist, schtasks, and PowerShell cmdlets. Success reveals targets for further exploitation, such as injecting into a SYSTEM process or modifying a scheduled task. This is typically performed in post-exploitation phases after initial access, targeting domain-joined Windows servers or workstations.

## Requirements

1. Low-privileged user access to a Windows system (local shell or remote via SMB/WMI).
2. PowerShell execution policy allowing script execution (or bypass if restricted).
3. No administrative privileges required for enumeration, but some queries may need SeDebugPrivilege for full process details.
4. Built-in tools only; no external dependencies like Impacket or PowerSploit.

## Defense

- Implement principle of least privilege: Restrict user access to process enumeration tools and monitor for anomalous queries via Sysmon (Event ID 1 for process creation, 10 for process access).
- Enable Windows Defender Application Control (WDAC) or AppLocker to prevent injection into privileged processes.
- Regularly audit scheduled tasks and services with tools like Autoruns; remove unnecessary SYSTEM-level tasks.
- Monitor Event Logs for scheduled task execution (Event ID 4698) and service changes (Event ID 7045).
- Use PowerShell logging (Module, Script Block, Transcription) to detect enumeration cmdlets like Get-Process or Get-Service.

## Objectives

1. Identify processes running as SYSTEM or other elevated users for potential injection or hijacking.
2. Enumerate services and scheduled tasks with modifiable permissions or weak configurations.
3. Discover autostart programs and registry entries that could be abused for persistence or escalation.
4. Collect data to inform targeted privilege escalation attacks, such as service exploitation or task modification.

## Instructions

### Step 1: Verify PowerShell Version

**Context**: Checking the PowerShell version ensures compatibility with advanced enumeration cmdlets like Get-WmiObject, which may behave differently across versions (e.g., v2 vs. v5+). This helps avoid errors in subsequent steps and identifies if constrained language mode is active.

**Command** ([[commands/check-powershell-version]]):
```cmd
REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion
```

> This queries the registry for the installed PowerShell version. If the version is below 3.0, some WMI queries may fail; consider falling back to WMIC. Expected output includes the version string, e.g., "PowerShellVersion    REG_SZ    5.1.19041.1237".

### Step 2: Enumerate All Running Processes and Owners

**Context**: This step gathers a comprehensive list of processes, including owners, to identify elevated ones excluding common svchost instances. It combines cmd and PowerShell tools for broad coverage, revealing potential injection targets like lsass.exe or winlogon.exe running as SYSTEM.

**Code** ([[codes/enumerate-all-processes-and-services-powershell]]):
```powershell
tasklist /v
net start
sc query
Get-Service
Get-Process
Get-WmiObject -Query "Select * from Win32_Process" | where {$_.Name -notlike "svchost*"} | Select Name, Handle, @{Label="Owner";Expression={$_.GetOwner().User}} | ft -AutoSize
```

> Run this in PowerShell to list processes via multiple methods: tasklist for verbose details, net start/sc query/Get-Service for services, Get-Process for basics, and WMI for owner info (filtered). Look for processes with SYSTEM or Administrator owners. Success if no errors and output shows process names, PIDs, and owners; pipe to file for analysis if verbose.

### Step 3: List Processes Running as SYSTEM

**Context**: Focusing on SYSTEM-owned processes narrows down high-value targets for escalation, such as services or daemons that might allow DLL hijacking or injection without alerting.

**Command** ([[commands/list-system-user-processes-tasklist]]):
```cmd
tasklist /v /fi "username eq system"
```

> Filters tasklist output to SYSTEM processes only. Expected output: A table of PIDs, images, and command lines for SYSTEM items, e.g., "svchost.exe 1234 Services 0 15,872 N/A SYSTEM". If empty or access denied, escalate to PowerShell WMI alternative.

### Step 4: Enumerate Installed Programs

**Context**: Listing installed software helps identify vulnerable applications (e.g., unpatched Java) or directories with weak permissions that could be exploited for binary planting leading to escalation.

**Code** ([[codes/enumerate-installed-programs-directories-and-registry]]):
```powershell
Get-ChildItem 'C:\Program Files', 'C:\Program Files (x86)' | ft Parent,Name,LastWriteTime
Get-ChildItem -path Registry::HKEY_LOCAL_MACHINE\SOFTWARE | ft Name
```

> Uses PowerShell to list executables in Program Files and registry keys under HKLM\SOFTWARE. This reveals installed apps and their install times. Success: Table output showing paths and names; check for writable directories post-enumeration.

### Step 5: Enumerate Running Services

**Context**: Services often run as SYSTEM and may have modifiable binaries or configs, enabling execution of arbitrary code with elevated privileges (T1035).

**Code** ([[codes/enumerate-running-services-multiple-methods]]):
```powershell
net start
wmic service list brief
tasklist /SVC
```

> Combines net start for running services, WMIC for brief details, and tasklist/SVC for process-service mapping. Expected: Lists of service names, states, and associated PIDs. Identify unquoted paths or weak ACLs for exploitation.

### Step 6: Enumerate Scheduled Tasks

**Context**: Scheduled tasks can execute as SYSTEM; enumerating them uncovers ones with stored credentials or modifiable actions for persistence/escalation (T1053).

**Code** ([[codes/enumerate-scheduled-tasks-and-system-tasks]]):
```powershell
schtasks /query /fo LIST 2>nul | findstr TaskName
schtasks /query /fo LIST /v > schtasks.txt; cat schtask.txt | grep "SYSTEM\|Task To Run" | grep -B 1 SYSTEM
Get-ScheduledTask | where {$_.TaskPath -notlike "\\Microsoft*"} | ft TaskName,TaskPath,State
```

> Queries tasks via schtasks (filtered for names and SYSTEM), exports verbose to file for grep (note: grep/cat are Unix-like; use PowerShell Select-String if unavailable), and PowerShell for non-Microsoft tasks. Success: List of task names, paths, states; focus on SYSTEM-run ones.

### Step 7: Enumerate Startup Programs

**Context**: Autostart locations like registry Run keys or Startup folders may allow adding malicious payloads that execute at logon with user or SYSTEM context (T1547.001).

**Context**: Use multiple commands to cover WMI, registry, and folders. If one fails (e.g., old paths), try alternatives like \ProgramData for modern Windows.

**Command** ([[commands/list-startup-programs-wmic]]):
```cmd
wmic startup get caption,command
```

> Lists WMI startup items. Expected: Caption and command columns.

**Command** ([[commands/list-startup-programs-registry-hklm]]):
```cmd
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```

> HKLM Run key (note: original incomplete path; assumes Run). Expected: Registry values with paths.

**Command** ([[commands/list-startup-programs-registry-hkcu]]):
```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

> HKCU Run key. Expected: User-specific startup entries.

**Command** ([[commands/list-run-once-programs-registry-hkcu]]):
```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```

> RunOnce for one-time starts. Expected: Temporary startup items.

**Command** ([[commands/list-startup-programs-all-users-start-menu]]):
```cmd
dir "C:\\Documents and Settings\\All Users\\Start Menu\\Programs\\Startup"
```

> All-users folder (XP-era; modern: C:\ProgramData\...). Expected: Directory listing.

**Command** ([[commands/list-startup-programs-current-user-start-menu]]):
```cmd
dir "C:\\Documents and Settings\\%username%\\Start Menu\\Programs\\Startup"
```

> Current user folder. Expected: User-specific shortcuts.
