---
type: command
executor: beacon
data: beacon > rm $_PATH
tags:
  - cobalt-strike
  - file-management
  - anti-forensics
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-delete-file-or-folder

## Command

```bash
beacon > rm $_PATH
```

## Description

Deletes a file or folder on the target, aiding in cleanup or disruption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PATH | File or directory path to delete. | Yes |
| -r | Recursive deletion for directories (optional). | No |
| -f | Force deletion without prompt (optional). | No |

## Examples

### Basic Usage

```bash
beacon > rm C:\\temp\\log.txt
```

### Advanced Usage

```bash
beacon > rm -r /var/log
```

## Expected Output

Deletion confirmation, e.g.:

[*] Deleted C:\\temp\\log.txt

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
