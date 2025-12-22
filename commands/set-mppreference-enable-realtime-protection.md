---
id: de4d3958-e028-48a1-a254-64f095232abc
name: set-mppreference-enable-realtime-protection
type: command
executor: powershell
data: |-
  Set-MpPreference -DisableRealtimeMonitoring $false
  Set-MpPreference -DisableScriptScanning $false
  Get-MpComputerStatus
output: null
created_at: '2023-04-06T03:56:26.616249+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - restoration
  - opsec
verified: true
validated: true
---

# set-mppreference-enable-realtime-protection

## Command

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -DisableScriptScanning $false
Get-MpComputerStatus
```

## Description

Re-enables real-time protection and script scanning after testing to maintain operational security.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DisableRealtimeMonitoring | Set to $false to enable | Yes |
| $false | Boolean to re-enable | Yes |
| -DisableScriptScanning | Set to $false to enable AMSI | Yes |

## Examples

### Basic Usage

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
```

### Advanced Usage

With verification:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false; Get-MpComputerStatus
```

## Expected Output

No output for Set-MpPreference. Status:

```
RealTimeProtectionEnabled : True
```

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
