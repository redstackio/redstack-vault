---
id: 558f921b-ceca-4296-b599-725ee4b26cfe
type: command
executor: powershell
data: Set-MpPreference -DisableRealtimeMonitoring $true
output: null
created_at: '2020-01-28T21:19:38.378793+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defender
  - disable-av
  - defense-evasion
verified: true
validated: true
---

# set-mp-preference-disable-realtime-monitoring

## Command

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

## Description

This PowerShell command disables real-time monitoring in Windows Defender, preventing it from scanning files, processes, and network activity in real-time. It is typically used after gaining administrator access to evade antivirus detection during post-exploitation activities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DisableRealtimeMonitoring | Sets real-time protection to disabled (accepts $true or $false) | Yes |
| $true | Boolean value to enable/disable the feature | Yes |

## Examples

### Basic Usage

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

### Verification

```powershell
Get-MpPreference | Select-Object DisableRealtimeMonitoring
```

## Expected Output

No direct output on success. The verification command returns:

DisableRealtimeMonitoring : True

## Related

- [[Related Procedure: disable-windows-defender]]
