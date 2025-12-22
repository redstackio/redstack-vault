---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: inject-fake-vba-into-macrofile-for-office-2013-x64
type: command
executor: cmd
data: EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc
output: null
created_at: '2023-04-06T03:56:23.824843+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
platforms:
  - Windows
tags:
  - vba-injection
  - office-2013
  - evilclippy
verified: true
validated: true
---

# inject-fake-vba-into-macrofile-for-office-2013-x64

## Command

```cmd
EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc
```

## Description

Injects fake VBA code into an Office document targeted for Microsoft Office 2013 x64 architecture, enabling version-specific macro manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s fakecode.vba | Specifies the VBA script file to inject | Yes |
| -t 2013x64 | Targets Office 2013 x64 version | Yes |
| macrofile.doc | Target Office document | Yes |

## Examples

### Basic Usage

```cmd
EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc
```

### Advanced Usage

Use with -g for obfuscation: EvilClippy.exe -s fakecode.vba -t 2013x64 -g macrofile.doc.

## Expected Output

Successful injection; document updated. Expected: Macro visible in VBA editor with injected code (before purging).

## Related

- [[procedures/VBA-Purging-with-EvilClippy]]
- [[tools/EvilClippy]]
