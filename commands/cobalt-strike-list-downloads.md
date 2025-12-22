---
type: command
executor: beacon
data: beacon > downloads
tags:
  - cobalt-strike
  - file-management
  - exfiltration
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-list-downloads

## Command

```bash
beacon > downloads
```

## Description

Lists all active file downloads from the target, showing progress and status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters required. | No |

## Examples

### Basic Usage

```bash
beacon > downloads
```

## Expected Output

Table of downloads, e.g.:

[*] ID  Path  Size  Progress
[*] 1   C:\\file.txt  1024  100%

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
