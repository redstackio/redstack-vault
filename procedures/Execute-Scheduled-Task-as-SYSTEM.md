---
id: uuid-execute-system
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
  - '[[commands/schtasks-run-elevated-task]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Scheduled Task]]'
updated_at: '2025-12-14T17:29:09.413Z'
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
# Execute Scheduled Task as SYSTEM

## Summary

This procedure runs the previously created scheduled task to execute code under NT AUTHORITY\SYSTEM privileges.

## Description

Using schtasks /run /I on the 'EOP' task ignores constraints and starts it immediately, running winver.exe (or custom payload) as SYSTEM. Requires the task from prior step and admin shell. Outcome: Full SYSTEM access confirmed via process execution.

## Requirements

1. 'EOP' scheduled task created with SYSTEM rights
2. Administrative command shell
3. schtasks.exe access

## Defense

Defensive measures and detection strategies:

- Monitor task runs (Event ID 4699/4700 in Security log)
- Disable interactive task runs via group policy
- Use EDR to flag SYSTEM processes from schtasks

## Objectives

1. Trigger SYSTEM-level execution
2. Validate full compromise
3. Enable payload delivery as highest privilege

## Instructions

### Step 1: Run the Task

**Context**: Invoke the task from the admin shell to execute as SYSTEM.

**Command** ([[commands/schtasks-run-elevated-task]]):

```cmd
schtasks /run /I /TN EOP
```

> Success: "SUCCESS: Attempted to run the scheduled task \"EOP\""; observe winver.exe in Task Manager under SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Scheduled Task]]

### Sub-Techniques


## Commands Used

- [[commands/schtasks-run-elevated-task]]

## Tools Used

- [[tools/Schtasks-EXE]]

## Tags

- [[privilege-escalation]]
- [[scheduled-task]]
- [[windows]]
