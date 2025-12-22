---
id: 6b338613-8303-4285-aa37-e4384e5d0763
name: CMD-List-System32-Contents
type: command
executor: cmd
data: dir $_DIRECTORY_PATH
output: null
created_at: '2023-04-06T03:56:30.347913+00:00'
updated_at: '2023-04-10T20:37:40.997286+00:00'
platforms:
  - Windows
tags:
  - recon
  - directory-list
verified: true
validated: true
---

# CMD-List-System32-Contents

## Command

```cmd
dir $_DIRECTORY_PATH
```

## Description

This CMD command lists the contents of a directory, such as System32, showing files, sizes, and dates. Useful for verifying file placements or permissions in post-exploitation scenarios, like confirming privileged writes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_DIRECTORY_PATH` | Path to list (e.g., C:\Windows\System32) | Yes |

## Examples

### Basic Usage

```cmd
dir C:\Windows\System32
```

### Advanced Usage

```cmd
dir C:\Windows\System32 /B
```

## Expected Output

```
 Volume in drive C has no label.
 Directory of C:\Windows\System32

04/10/2023  08:37 PM    <DIR>          .
04/10/2023  08:37 PM    <DIR>          ..
... (list of files)
```

A successful listing shows files without permission errors; look for new entries post-exploit.

## Related

- [[procedures/Windows-Privileged-File-Write-via-UsoDLLLoader]]
