---
type: command
executor: beacon
data: beacon > cancel $_FILE_ID
tags:
  - cobalt-strike
  - file-management
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-cancel-download

## Command

```bash
beacon > cancel $_FILE_ID
```

## Description

Cancels an ongoing file download by its ID to stop exfiltration if needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_ID | Download ID from 'downloads' command (e.g., 1). | Yes |

## Examples

### Basic Usage

```bash
beacon > cancel 1
```

## Expected Output

Cancellation confirmation, e.g.:

[*] Download 1 canceled

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
