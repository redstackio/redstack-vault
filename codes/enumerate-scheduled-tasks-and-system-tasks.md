---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - enumeration
  - scheduled-tasks
validated: true
---

# enumerate-scheduled-tasks-and-system-tasks

## Code

```powershell
schtasks /query /fo LIST 2>nul | findstr TaskName
schtasks /query /fo LIST /v > schtasks.txt; cat schtask.txt | grep "SYSTEM\|Task To Run" | grep -B 1 SYSTEM
Get-ScheduledTask | where {$_.TaskPath -notlike "\\Microsoft*"} | ft TaskName,TaskPath,State
```

## Description

Enumerates scheduled tasks, focusing on SYSTEM-run ones using schtasks and PowerShell, to find modifiable tasks for T1053 execution or persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; note Unix tools (grep/cat) may require Git Bash or adjustment to Select-String | N/A |

## Usage

Run in a shell supporting the commands; the file export allows filtering for SYSTEM tasks. Modify found tasks if permissions allow for escalation.

## Detection

- Task Scheduler logs (Event ID 4698 for task creation/modification).
- File creation of schtasks.txt monitored via filesystem auditing.
- PowerShell Get-ScheduledTask in module logs.

## Related

- [[procedures/windows-processes-and-tasks-enumeration-for-privilege-escalation]]
