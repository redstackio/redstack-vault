---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: purge-vba-source-with-r-flag
type: command
executor: cmd
data: EvilClippy.exe -r macrofile.doc
output: null
created_at: '2023-04-06T03:56:23.824979+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
platforms:
  - Windows
tags:
  - vba-purging
  - obfuscation
  - evilclippy
verified: true
validated: true
---

# purge-vba-source-with-r-flag

## Command

```cmd
EvilClippy.exe -r macrofile.doc
```

## Description

Removes the VBA source code from the Office document, leaving only the compiled p-code to evade detection and confuse analysis tools like pcode.dmp.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Flag to remove VBA source code | Yes |
| macrofile.doc | Target Office document file | Yes |

## Examples

### Basic Usage

```cmd
EvilClippy.exe -r macrofile.doc
```

### Advanced Usage

Combine with other flags, e.g., EvilClippy.exe -s script.vba -r target.doc.

## Expected Output

Process completes silently or with a success message. The document's VBA project now contains only compiled code, verifiable by opening in Office VBA editor (source unviewable).

## Related

- [[procedures/VBA-Purging-with-EvilClippy]]
- [[tools/EvilClippy]]
