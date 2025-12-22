---
type: command
executor: beacon
data: beacon > cp $_SOURCE $_DESTINATION
tags:
  - cobalt-strike
  - file-management
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-copy-file

## Command

```bash
beacon > cp $_SOURCE $_DESTINATION
```

## Description

Copies a file or directory from source to destination on the target host, useful for backing up or staging files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOURCE | Source file or directory path. | Yes |
| $_DESTINATION | Destination path. | Yes |
| -r | Recursive copy for directories (optional). | No |

## Examples

### Basic Usage

```bash
beacon > cp C:\\secrets.txt C:\\Temp\\backup.txt
```

### Advanced Usage

```bash
beacon > cp -r /etc /tmp/backup
```

## Expected Output

Success confirmation, e.g.:

[*] Copied 1 file(s)

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
