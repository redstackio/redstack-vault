---
type: command
executor: cmd
data: attrib +h mimikatz.exe
output: null
created_at: '2023-04-06T03:56:27.604771+00:00'
updated_at: '2023-04-10T20:37:30.093036+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - file-hiding
verified: true
validated: true
---

# attrib-set-hidden-attribute-on-mimikatz

## Command

```cmd
attrib +h mimikatz.exe
```

## Description

This command uses the Windows 'attrib' utility to set the hidden attribute on the Mimikatz executable file (mimikatz.exe), making it invisible in standard file explorers and directory listings unless hidden files are explicitly shown. It is useful for evading detection during persistence after placing the binary on a target system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +h | Adds the hidden attribute to the file | Yes |
| mimikatz.exe | The target file name (use full path if not in current directory, e.g., C:\Temp\mimikatz.exe) | Yes |

## Examples

### Basic Usage

```cmd
attrib +h mimikatz.exe
```

Hides the file in the current directory.

### Advanced Usage

```cmd
attrib +h +s C:\Windows\Temp\mimikatz.exe
```

Hides and marks the file as a system file for additional concealment.

### Verification Usage

```cmd
attrib mimikatz.exe
```

Displays current attributes; look for 'A' (archive), 'H' (hidden), etc.

## Expected Output

When successful, the command produces no output or a brief confirmation like:

```
H
```

Indicating the hidden attribute is set. The file will not appear in `dir` listings without the `/a:h` flag.

## Related

- [[procedures/Hide-Mimikatz-Executable-for-Persistence]]
