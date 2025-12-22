---
type: command
executor: beacon
data: beacon > ls $_PATH
tags:
  - cobalt-strike
  - file-management
  - reconnaissance
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-list-directory-contents

## Command

```bash
beacon > ls $_PATH
```

## Description

Lists files and subdirectories in the specified path on the compromised host via Cobalt Strike Beacon. Useful for reconnaissance of the file system during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH | Target directory path (e.g., C:\\Windows or /etc). Defaults to current working directory if omitted. | No |
| -r | Recursive listing flag (optional). | No |

## Examples

### Basic Usage

```bash
beacon > ls C:\\Users
```

### Advanced Usage

```bash
beacon > ls -r /var/log
```

## Expected Output

Directory listing with file names, sizes, and modification times, e.g.:

[*] Listing C:\\Users
[*] 2023-10-01 12:00   1024  Administrator
[*] 2023-10-01 12:00   2048  Public

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
