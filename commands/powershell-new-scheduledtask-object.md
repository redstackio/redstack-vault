---
type: command
executor: powershell
data: $D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# powershell-new-scheduledtask-object

## Command

```powershell
$D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
```

## Description

Assembles a complete scheduled task object from previously defined components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Action $A | Action object | Yes |
| -Trigger $T | Trigger object | Yes |
| -Principal $P | Principal object | Yes |
| -Settings $S | Settings object | Yes |

## Examples

### Basic Usage

```powershell
$D = New-ScheduledTask -Action $A -Trigger $T
```

## Expected Output

Returns a ScheduledTask object ready for registration.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
