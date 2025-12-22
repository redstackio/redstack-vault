---
id: 59f01ad1-cea3-4d29-9bbb-4446f6131351
name: windows-cmd-search-unattend-files
type: command
executor: cmd
data: >-
  dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt
  2>nul
output: null
created_at: '2023-04-06T03:56:29.080438+00:00'
updated_at: '2023-04-10T20:37:39.339735+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - file-search
verified: true
validated: true
---

# windows-cmd-search-unattend-files

## Command

```cmd
dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul
```

## Description

This command performs a recursive directory search on the Windows file system for common answer files used in automated installations, which may contain credentials. It starts from the current directory (ideally C:\) and suppresses error messages for permission-denied paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /s | Recurse into subdirectories | Built-in |
| *pattern* | Wildcard file patterns for sysprep and unattend files | Built-in |
| 2>nul | Suppress stderr output | Built-in |

No user-supplied parameters; the patterns are fixed for relevance.

## Examples

### Basic Usage

```cmd
dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul
```

Run from C:\ to search the entire system.

### Advanced Usage

Pipe to findstr for keyword filtering:

```cmd
dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul | findstr /i "unattend"
```

## Expected Output

A list of matching file paths, for example:

```
 Directory of C:\Windows\Panther

04/06/2023  10:00 AM               1,234 unattend.xml

 Directory of C:\Windows\system32\sysprep

04/06/2023  09:00 AM                 567 sysprep.xml
```

## Related

- [[procedures/windows-unattend-password-extraction]]
- [[commands/powershell-decode-base64-password]]
