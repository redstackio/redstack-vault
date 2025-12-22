---
type: command
executor: bash
data: BadAssMacros.exe -i <path_to_doc_or_excel_file> -w <doc_or_excel> -p yes -l
output: null
platforms:
  - Windows
tags:
  - office
  - macro
  - analysis
verified: true
validated: true
---

# list-modules-doc-excel-file

## Command

```bash
BadAssMacros.exe -i $_INPUT_FILE -w $_DOC_OR_EXCEL -p yes -l
```

## Description

Lists all VBA modules present in an Office document for analysis or cleanup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_INPUT_FILE` | Path to the .doc or .xls file | Yes |
| `$_DOC_OR_EXCEL` | 'doc' or 'excel' type | Yes |
| `-p yes` | Preserve original file | Built-in |
| `-l` | List modules flag | Built-in |

## Examples

### Basic Usage

```bash
BadAssMacros.exe -i document.doc -w doc -p yes -l
```

## Expected Output

Console output showing modules:
Modules in document.doc:
- ThisDocument
- Module1 (Sub AutoOpen())
- UserForm1

## Related

- [[procedures/Create-Office-Macro-Malware-with-BadAssMacros]]
- [[tools/BadAssMacros]]
