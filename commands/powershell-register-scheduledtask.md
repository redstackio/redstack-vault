---
type: command
executor: powershell
data: Register-ScheduledTask Backdoor -InputObject $D
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# powershell-register-scheduledtask

## Command

```powershell
Register-ScheduledTask Backdoor -InputObject $D
```

## Description

Registers the assembled task in the system scheduler under a given name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Backdoor | Task name | Yes |
| -InputObject $D | The task object | Yes |

## Examples

### Basic Usage

```powershell
Register-ScheduledTask "Backdoor" -InputObject $D
```

## Expected Output

Returns the registered task path or success confirmation.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
