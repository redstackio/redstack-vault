---
id: 892e4d3d-e2ef-4335-b9c3-484d8923d908
name: powershell-get-childitem-laps-admpwd-dll
type: command
executor: powershell
data: 'Get-ChildItem ''C:\Program Files\LAPS\CSE\Admpwd.dll'''
output: null
created_at: '2023-04-06T03:56:04.492648+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - laps
  - active-directory
verified: true
validated: true
---

# powershell-get-childitem-laps-admpwd-dll

## Command

```powershell
Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

## Description

This command checks for the existence of the Admpwd.dll file, part of the LAPS Client Side Extension, in the default installation path on a Windows domain-joined machine. Use it as the first step to detect LAPS deployment locally.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'C:\\Program Files\\LAPS\\CSE\\Admpwd.dll'` | Path to the Admpwd.dll file | Yes |

## Examples

### Basic Usage

```powershell
Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

### Remote Check (via Invoke-Command)

```powershell
Invoke-Command -ComputerName REMOTE-MACHINE -ScriptBlock { Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll' }
```

## Expected Output

If the file exists:

    Directory: C:\Program Files\LAPS\CSE

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         1/1/2020   12:00 PM       123456 Admpwd.dll

If not found, no output or error: 'Cannot find path...'

## Related

- [[procedures/Check-LAPS-Installation-and-Retrieve-Password]]
- [[commands/powershell-get-filehash-laps-admpwd-dll]]
