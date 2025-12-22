---
id: c1f7da33-3469-4f5e-92dd-83e48985a8d5
name: PowerShell-Get-DLL-Properties
type: command
executor: powershell
data: 'Get-ItemProperty -Path "C:\Windows\System32\windowscoredeviceinfo.dll"'
output: null
created_at: '2023-04-06T03:56:30.347790+00:00'
updated_at: '2023-04-10T20:37:40.997286+00:00'
platforms:
  - Windows
tags:
  - recon
  - file-info
verified: true
validated: true
---

# PowerShell-Get-DLL-Properties

## Command

```powershell
Get-ItemProperty -Path "$_DLL_PATH"
```

## Description

This PowerShell command retrieves detailed properties of a specified DLL file, such as version, size, and attributes. Use it during reconnaissance to assess target DLLs for hijacking vulnerabilities in privilege escalation scenarios like UsoDLLLoader abuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_DLL_PATH` | Full path to the DLL file (e.g., C:\Windows\System32\windowscoredeviceinfo.dll) | Yes |

## Examples

### Basic Usage

```powershell
Get-ItemProperty -Path "C:\Windows\System32\windowscoredeviceinfo.dll"
```

### Advanced Usage

```powershell
Get-ItemProperty -Path "$_DLL_PATH" | Select-Object Name, Length, LastWriteTime
```

## Expected Output

```

    Name                  : windowscoredeviceinfo.dll
    Length                : 123456
    LastWriteTime         : 1/1/2023 12:00:00 PM

```

Properties displayed include file metadata; success if no 'Access Denied' error and details match expected system file.

## Related

- [[procedures/Windows-Privileged-File-Write-via-UsoDLLLoader]]
