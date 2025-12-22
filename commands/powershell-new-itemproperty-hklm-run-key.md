---
type: command
executor: powershell
data: >-
  New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
  -Name '$_VALUE_NAME' -Value '$_VALUE_DATA' -PropertyType String
platforms:
  - Windows
tags:
  - persistence
  - registry
verified: true
validated: true
---

# powershell-new-itemproperty-hklm-run-key

## Command

```powershell
New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name '$_VALUE_NAME' -Value '$_VALUE_DATA' -PropertyType String
```

## Description

This PowerShell command adds a new string value to the HKLM Run key for startup persistence, specifying a program to execute on boot.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Path | Registry path (fixed to HKLM Run key) | Yes |
| -Name, $_VALUE_NAME | Name of the registry value (e.g., Backdoor) | Yes |
| -Value, $_VALUE_DATA | Path to the executable (e.g., C:\Windows\Temp\backdoor.exe) | Yes |
| -PropertyType | Type of value (String/REG_SZ) | Yes |

## Examples

### Basic Usage

```powershell
New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'Backdoor' -Value 'C:\Windows\Temp\backdoor.exe' -PropertyType String
```

### Advanced Usage

```powershell
New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'UpdateService' -Value 'C:\ProgramData\updatesvc.exe' -PropertyType String -Force
```

## Expected Output

PS C:\> New-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name 'Backdoor' -Value 'C:\Windows\Temp\backdoor.exe' -PropertyType String

Name                           Value
----                           -----
Backdoor                       C:\Windows\Temp\backdoor.exe

(On error: New-ItemProperty : Access to the registry key 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' is denied.)

## Related

- [[procedures/Windows-Registry-HKLM-Run-Key-Persistence]]
