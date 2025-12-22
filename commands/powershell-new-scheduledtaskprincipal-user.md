---
type: command
executor: powershell
data: $P = New-ScheduledTaskPrincipal "Rasta"
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# powershell-new-scheduledtaskprincipal-user

## Command

```powershell
$P = New-ScheduledTaskPrincipal "Rasta"
```

## Description

Sets the security principal (user context) for the task execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "Rasta" | User account or group | Yes |

## Examples

### Basic Usage

```powershell
$P = New-ScheduledTaskPrincipal "SYSTEM"
```

## Expected Output

Returns a TaskPrincipal object.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
