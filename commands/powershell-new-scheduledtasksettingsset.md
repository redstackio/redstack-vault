---
type: command
executor: powershell
data: $S = New-ScheduledTaskSettingsSet
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# powershell-new-scheduledtasksettingsset

## Command

```powershell
$S = New-ScheduledTaskSettingsSet
```

## Description

Creates default settings for the scheduled task, such as allowing demand start and hidden execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Uses defaults | Yes |

## Examples

### Basic Usage

```powershell
$S = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries $true
```

## Expected Output

Returns a TaskSettings object with default configurations.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
