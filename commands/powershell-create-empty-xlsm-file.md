---
type: command
executor: powershell
data: New-Item -ItemType File -Name blank.xlsm -Force
tags:
  - office
  - macro
platforms:
  - Windows
verified: true
validated: true
---

# powershell-create-empty-xlsm-file

## Command

```powershell
New-Item -ItemType File -Name blank.xlsm -Force
```

## Description

This PowerShell command creates an empty Excel macro-enabled workbook file (.xlsm) in the current directory, serving as a template for embedding VBA macros.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ItemType File` | Specifies that a file (not directory) is created | Yes |
| `-Name blank.xlsm` | The name and extension of the file to create | Yes |
| `-Force` | Overwrites if the file already exists | No |

## Examples

### Basic Usage

```powershell
New-Item -ItemType File -Name blank.xlsm -Force
```

### Advanced Usage

```powershell
New-Item -ItemType File -Name "my-macro.xlsm" -Path C:\Temp -Force
```

## Expected Output

Directory: C:\path\to\current

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         4/6/2023   3:56 AM            0 blank.xlsm

The command outputs file details if successful; no output if -Force suppresses it.

## Related

- [[procedures/Generate-Obfuscated-VBA-Macro-Using-Hot-Manchego]]
