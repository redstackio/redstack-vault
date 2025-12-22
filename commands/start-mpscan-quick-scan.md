---
id: 05b2a667-2f6a-466a-948f-80c4d3006bad
name: start-mpscan-quick-scan
type: command
executor: powershell
data: Start-MpScan -ScanType QuickScan
output: null
created_at: '2023-04-06T03:56:26.616303+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - verification
  - scan
verified: true
validated: true
---

# start-mpscan-quick-scan

## Command

```powershell
Start-MpScan -ScanType QuickScan
```

## Description

Initiates a quick scan of common threat locations to verify impairments or check for detections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ScanType | Type of scan (QuickScan, FullScan, etc.) | Yes |
| QuickScan | Scans user profile and common areas | Yes |

## Examples

### Basic Usage

```powershell
Start-MpScan -ScanType QuickScan
```

## Expected Output

```
Scan started successfully.
Scan ID: {guid}
```
Progress updates follow; completes with threat summary if any.

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
