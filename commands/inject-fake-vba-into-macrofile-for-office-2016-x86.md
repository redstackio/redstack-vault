---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
name: inject-fake-vba-into-macrofile-for-office-2016-x86
type: command
executor: cmd
data: EvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc
output: null
created_at: '2023-04-06T03:56:23.824734+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
platforms:
  - Windows
tags:
  - vba-injection
  - office-2016
  - evilclippy
verified: true
validated: true
---

# inject-fake-vba-into-macrofile-for-office-2016-x86

## Command

```cmd
EvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc
```

## Description

Injects fake VBA code into an Office document targeted for Microsoft Office 2016 x86 architecture, supporting compatibility with 32-bit installations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s fakecode.vba | Specifies the VBA script file to inject | Yes |
| -t 2016x86 | Targets Office 2016 x86 version | Yes |
| macrofile.doc | Target Office document | Yes |

## Examples

### Basic Usage

```cmd
EvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc
```

### Advanced Usage

Combine with -r: EvilClippy.exe -s fakecode.vba -t 2016x86 -r macrofile.doc.

## Expected Output

Injection completes; macrofile.doc modified. Verify by inspecting VBA project in Office.

## Related

- [[procedures/VBA-Purging-with-EvilClippy]]
- [[tools/EvilClippy]]
