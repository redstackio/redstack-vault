---
id: 056f0219-90a4-45e6-ba1b-d083607eeb04
name: get-mpcomputerstatus-check-defender-status
type: command
executor: powershell
data: Get-MpComputerStatus
output: null
created_at: '2023-04-06T03:56:26.616488+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - antivirus
verified: true
validated: true
---

# get-mpcomputerstatus-check-defender-status

## Command

```powershell
Get-MpComputerStatus
```

## Description

Queries the status of Windows Defender Antivirus, including whether real-time protection is enabled, signature version, and scan engine details. Use this during reconnaissance to evaluate the target's defenses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs on local machine | No |

## Examples

### Basic Usage

```powershell
Get-MpComputerStatus
```

### Advanced Usage

Pipe to select specific properties:

```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, SignatureVersion
```

## Expected Output

```
AntivirusEnabled           : True
AntivirusSignatureLastUpdated : 10/1/2023 12:00:00 PM
AntivirusSignatureVersion  : 1.413.1234.0
RealTimeProtectionEnabled  : True
...
```

Success is indicated by detailed status output without errors.

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
