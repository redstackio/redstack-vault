---
id: fea4c39e-e595-41ce-938f-44f0cc16b6b8
name: start-mpscan-full-scan
type: command
executor: powershell
data: Start-MpScan -ScanType FullScan
output: null
created_at: '2023-04-06T03:56:26.616365+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - verification
  - scan
verified: true
validated: true
---

# start-mpscan-full-scan

## Command

```powershell
Start-MpScan -ScanType FullScan
```

## Description

Starts a full system scan to validate evasion techniques or simulate normal operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ScanType | Specifies full system scan | Yes |
| FullScan | Scans all drives and files | Yes |

## Examples

### Basic Usage

```powershell
Start-MpScan -ScanType FullScan
```

## Expected Output

```
Full scan initiated.
Estimated time: X minutes
```
Ends with: "Scan completed successfully. No threats found."

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
