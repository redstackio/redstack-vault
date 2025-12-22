---
type: command
executor: powershell
data: $T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# powershell-new-scheduledtasktrigger-logon

## Command

```powershell
$T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
```

## Description

Defines a trigger for the task to run at user logon, enabling persistence tied to sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -AtLogOn | Trigger on logon event | Yes |
| -User "Rasta" | Specific user (optional for any) | No |

## Examples

### Basic Usage

```powershell
$T = New-ScheduledTaskTrigger -AtLogOn
```

## Expected Output

Returns a TaskTrigger object configured for logon.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
