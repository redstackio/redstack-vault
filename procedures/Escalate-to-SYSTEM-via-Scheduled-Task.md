---
id: uuid-escalate-system
tags:
  - privilege-escalation
  - scheduled-task
  - windows
type: procedure
tools:
  - '[[tools/Schtasks-EXE]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/schtasks-create-elevated-task]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Scheduled Task]]'
updated_at: '2025-12-14T17:29:09.421Z'
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
# Escalate to SYSTEM via Scheduled Task

## Summary

This procedure uses administrative access to create a scheduled task running as NT AUTHORITY\SYSTEM, enabling full system compromise.

## Description

From the admin cmd.exe, schtasks creates a weekly task with /RU SYSTEM, /IT for immediate start, and /RL HIGHEST. Targets a benign executable like winver.exe for testing, but can be replaced with payload. Requires admin shell. Outcome: Task ready for SYSTEM execution.

## Requirements

1. Administrative command shell
2. schtasks.exe available (built-in on Windows)
3. No UAC restrictions on task creation

## Defense

Defensive measures and detection strategies:

- Audit scheduled task creation (Event ID 4698 in Security log)
- Restrict schtasks usage for non-admins via AppLocker
- Monitor for SYSTEM-run tasks with unusual triggers using Sysmon (Event ID 1)

## Objectives

1. Escalate from admin to SYSTEM privileges
2. Achieve persistent high-privilege execution
3. Enable full system control

## Instructions

### Step 1: Create the Scheduled Task

**Context**: Use schtasks to set up the elevated task in the admin shell.

**Command** ([[commands/schtasks-create-elevated-task]]):

```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

> Success: "SUCCESS: The scheduled task \"EOP\" has successfully been created."

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Scheduled Task]]

### Sub-Techniques


## Commands Used

- [[commands/schtasks-create-elevated-task]]

## Tools Used

- [[tools/Schtasks-EXE]]

## Tags

- [[privilege-escalation]]
- [[scheduled-task]]
- [[windows]]
