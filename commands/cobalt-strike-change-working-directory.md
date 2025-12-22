---
type: command
executor: beacon
data: beacon > cd $_DIRECTORY
tags:
  - cobalt-strike
  - file-management
platforms:
  - Windows
  - Linux
verified: true
validated: true
---

# cobalt-strike-change-working-directory

## Command

```bash
beacon > cd $_DIRECTORY
```

## Description

Changes the current working directory in the Beacon session to streamline file operations without full paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DIRECTORY | Path to the new working directory (e.g., C:\\Temp or /home/user). | Yes |

## Examples

### Basic Usage

```bash
beacon > cd C:\\Windows\\System32
```

### Advanced Usage

```bash
beacon > cd ..
```

## Expected Output

Confirmation of directory change, e.g.:

[*] Changed working directory to C:\\Windows\\System32

## Related

- [[procedures/Cobalt-Strike-File-Management]]
- [[tools/Cobalt-Strike]]
