---
id: abf45bca-e398-4f1f-8f6b-c07d3d27c5b2
name: powershell-get-childitem-laps-dll
type: command
executor: powershell
data: 'Get-ChildItem ''C:\Program Files\LAPS\CSE\Admpwd.dll'''
output: null
created_at: '2023-01-12T19:12:06.788111+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - filesystem
verified: true
validated: true
---

# powershell-get-childitem-laps-dll

## Command

```powershell
Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

## Description

This PowerShell command retrieves details about the Admpwd.dll file in the LAPS Client Side Extension directory. The file's presence confirms LAPS installation on the local machine. Use this for scripted enumeration in Windows environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'C:\Program Files\LAPS\CSE\Admpwd.dll' | Full path to the LAPS DLL file | Yes |

## Examples

### Basic Usage

```powershell
Get-ChildItem 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

### Advanced Usage

To check existence without details:
```powershell
Test-Path 'C:\Program Files\LAPS\CSE\Admpwd.dll'
```

## Expected Output

If the file exists:
```
    Directory: C:\Program Files\LAPS\CSE

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2022-05-06  10:20 PM         244898 Admpwd.dll
```

If not found:
```
Get-ChildItem : Cannot find path 'C:\Program Files\LAPS\CSE\Admpwd.dll' because it does not exist.
```

## Related

- [[procedures/Enumerate-LAPS-Artifacts-on-Local-Machine]]
