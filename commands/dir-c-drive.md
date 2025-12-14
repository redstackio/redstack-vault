---
id: list-c-drive-files
data: 'dir C:\ /b | findstr program.exe'
tags:
  - file-list
  - verification
type: command
output: program.exe
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.214Z'
verified: false
validated: true
submitted: true
---
# dir-c-drive

## Command

```cmd
dir C:\ /b | findstr program.exe
```

## Description

Lists files in C:\ root and filters for 'program.exe' to verify placement of the hijack file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /b | Bare format (filenames only) | No |
| findstr program.exe | Filter for the target file | Yes |

## Examples

### Basic Usage

```cmd
dir C:\ /b | findstr program.exe
```

### Full List

```cmd
dir C:\
```

## Expected Output

'program.exe' if present; nothing if missing.

## Related

- [[commands/copy-malicious-exe]]
- [[procedures/Prepare-Malicious-Executable-for-Hijacking]]
