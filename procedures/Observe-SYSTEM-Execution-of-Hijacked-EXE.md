---
id: observe-exe-execution-acronis
tags:
  - system-execution
  - log-analysis
type: procedure
tools:
  - '[[tools/Procmon]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/procmon-review-events]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:28:52.221Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Observe-SYSTEM-Execution-of-Hijacked-EXE

## Summary

This procedure reviews Procmon logs to confirm that schedul2.exe, running as NT AUTHORITY\SYSTEM, successfully creates and executes the malicious 'C:\program.exe', validating the privilege escalation.

## Description

After installation, analyze captured events for the CreateFile operation on the hijacked path. Success is indicated by no 'NAME NOT FOUND' result and payload activation. This confirms arbitrary code execution at SYSTEM level. Expected outcome: Log entry with successful file access and execution details.

## Requirements

1. Procmon capture from previous steps
2. Knowledge of Procmon GUI for filtering
3. Malicious EXE with observable payload

## Defense

Defensive measures and detection strategies:

- Implement path validation in services
- Use integrity checks for expected binaries
- Monitor SYSTEM process spawns with ETW/Sysmon

## Objectives

1. Identify successful hijack in logs
2. Confirm SYSTEM privilege execution
3. Validate payload delivery

## Instructions

### Step 1: Stop Capture

**Context**: End Procmon logging post-installation.

In GUI, click Stop (Ctrl+E).

### Step 2: Filter and Review

**Context**: Search for relevant events.

Apply filter: Result is SUCCESS, Path contains Program.exe, Process is schedul2.exe.

Use [[commands/procmon-review-events]] if scripting:

```bash
# Procmon.exe /OpenLog acronis_capture.pml then GUI filter
```

> No direct CLI review; use GUI for details like PID 2976, Operation CreateFile.

### Step 3: Validate Execution

**Context**: Check for payload signs.

Look for pop-up or log of execution; expected: NT AUTHORITY\SYSTEM context.

> Success if file executed without failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used

- [[commands/procmon-review-events]]

## Tools Used

- [[tools/Procmon]]

## Tags

- [[log-review]]
- [[lpe-validation]]
