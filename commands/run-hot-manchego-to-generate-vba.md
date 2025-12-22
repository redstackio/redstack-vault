---
type: command
executor: cmd
data: .\hot-manchego.exe .\blank.xlsm .\vba.txt
tags:
  - macro-generation
  - obfuscation
platforms:
  - Windows
verified: true
validated: true
---

# run-hot-manchego-to-generate-vba

## Command

```cmd
.\hot-manchego.exe .\blank.xlsm .\vba.txt
```

## Description

This command runs the compiled Hot Manchego executable to generate obfuscated VBA code from the input .xlsm file and save it to vba.txt for later embedding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.\blank.xlsm` | Path to the empty Excel macro-enabled workbook | Yes |
| `.\vba.txt` | Output path for the generated VBA code | Yes |

## Examples

### Basic Usage

```cmd
.\hot-manchego.exe .\blank.xlsm .\vba.txt
```

### Advanced Usage

```cmd
hot-manchego.exe C:\path\to\template.xlsm C:\output\macro.vb
```

## Expected Output

The command runs silently if successful, creating vba.txt with obfuscated VBA code like:

Sub Auto_Open()
    ' Obfuscated payload here
End Sub

Verify by opening vba.txt; no console output unless errors occur.

## Related

- [[procedures/Generate-Obfuscated-VBA-Macro-Using-Hot-Manchego]]
