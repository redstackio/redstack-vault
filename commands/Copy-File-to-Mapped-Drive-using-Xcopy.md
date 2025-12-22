---
id: bd1ce063-6b86-41a4-aed4-0e6b7a889fd4
name: Copy-File-to-Mapped-Drive-using-Xcopy
type: command
executor: cmd
data: 'xcopy C:\$_FILENAME T:\$_FILENAME'
output: null
created_at: '2023-01-12T22:19:00.383458+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - '[[tags/file-transfer]]'
  - '[[tags/lateral-movement]]'
verified: true
validated: true
---

# Copy-File-to-Mapped-Drive-using-Xcopy

## Command

```cmd
xcopy C:\$_FILENAME T:\$_FILENAME
```

## Description

This command copies a single file from a local path (C:\) to a mapped network drive (T:), typically used after mapping a remote share. xcopy is robust for file transfers and prompts for confirmation if the target path is ambiguous. Ideal for staging files on remote Windows hosts during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| C:\$_FILENAME | Source file path on local machine (e.g., C:\payload.exe) | Yes |
| T:\$_FILENAME | Destination path on mapped drive (e.g., T:\payload.exe) | Yes |

## Examples

### Basic Usage

```cmd
xcopy C:\file.exe T:\file.exe
```

### Advanced Usage (Suppress Prompt)

```cmd
xcopy /Y C:\script.ps1 T:\Users\Public\script.ps1
```

## Expected Output

When successful (after selecting 'F' for file):

```
xcopy c:\file.exe t:\file.exe
Does t:\file.exe specify a file name or directory name on the target
(F = file, D = directory)? F
c:\file.exe
1 File(s) copied
```

If source not found:

```
File not found - $_FILENAME
0 File(s) copied
```

## Related

- [[procedures/Copy-File-to-Remote-Windows-Machine-via-Xcopy]]
- [[commands/Map-Remote-Share-as-Network-Drive]]
- [[Remote File Copy]]
