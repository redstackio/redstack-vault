---
type: tool
verified: true
created_at: '2023-06-01T00:00:00Z'
updated_at: '2023-06-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - administrator
url: >-
  https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page
commands:
  - '[[commands/schtasks-create-repeating-minute-task]]'
validated: true
---

# windows-scheduled-tasks

**Status**: ✓ Verified

## Overview

Windows Scheduled Tasks is a built-in feature for automating the execution of programs, scripts, or commands at specified times, dates, or intervals. It includes the schtasks.exe command-line utility and PowerShell cmdlets in the ScheduledTasks module. In offensive security, it is commonly abused for persistence mechanisms, allowing attackers to ensure malicious code runs repeatedly even after reboots or logoffs.

## Description

The Scheduled Tasks infrastructure enables the creation, modification, deletion, and management of tasks via GUI (Task Scheduler), CLI (schtasks), or scripting (PowerShell). Key capabilities include triggering tasks on events, time-based execution, and running under specific user contexts like SYSTEM. Attackers leverage this for backdoor installation, data exfiltration scheduling, or maintaining access. Detection focuses on anomalous task creation from non-admin users or unusual payloads.

## Features

- Time-based, event-based, or login-triggered scheduling
- Support for multiple actions (e.g., execute program, send email, display message)
- Principal configuration for user/group execution contexts
- Export/import tasks as XML for portability
- PowerShell cmdlets for advanced automation (e.g., New-ScheduledTask, Register-ScheduledTask)
- schtasks for quick CLI operations like create, query, delete

## Installation

### Requirements

- Windows Vista or later (full features from Windows 7/Server 2008 R2)
- Administrative privileges for most operations

### Install Commands

Pre-installed on all modern Windows versions. No additional installation required.

For PowerShell module (built-in):
```powershell
Import-Module ScheduledTasks
```

## Basic Usage

View help for schtasks:
```command_prompt
schtasks /?
```

List all tasks in PowerShell:
```powershell
Get-ScheduledTask
```

### Common Options

| Option | Description |
|--------|-------------|
| /create | Create a new scheduled task |
| /query | Display scheduled tasks |
| /delete | Delete a scheduled task |
| /run | Run a task immediately |
| -New-ScheduledTask | PowerShell: Create a task object |
| -Register-ScheduledTask | PowerShell: Register a task |

## Examples

### Example 1: Basic Usage

Query all tasks:
```command_prompt
schtasks /query
```

### Example 2: Advanced Usage

Create a task using PowerShell:
```powershell
$action = New-ScheduledTaskAction -Execute "notepad.exe"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -TaskName "TestTask" -Action $action -Trigger $trigger
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Scheduled Task]] Scheduled Task/Job: Scheduled Task

### Tactics

- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Event ID 4698 in Windows Security logs (task creation)
- Monitor schtasks.exe process spawning cmd.exe or PowerShell
- Anomalous tasks with suspicious paths (e.g., %TEMP%\malware.bat) or non-standard names
- PowerShell execution logs showing New-ScheduledTask or Register-ScheduledTask
- File system changes in C:\Windows\System32\Tasks

## Related Procedures

- [[procedures/Create-Windows-Scheduled-Task-for-Persistence]]

## Related Tools

- [[tools/Powershell]]
- [[tools/taskschd-mmc]]

## References

- [Microsoft Docs: schtasks](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks)
- [Microsoft Docs: ScheduledTasks PowerShell Module](https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/)
