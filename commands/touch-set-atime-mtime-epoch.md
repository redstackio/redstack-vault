---
id: 39401ec3-1887-4a2a-b87e-5147bdbc462c
name: touch-set-atime-mtime-epoch
type: command
executor: bash
data: touch -a -m -d @$_EPOCH_TIMESTAMP $_FILE_NAME
output: null
created_at: '2023-04-06T03:56:17.808659+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - timestamp-modification
verified: true
validated: true
---

# touch-set-atime-mtime-epoch

## Command

```bash
touch -a -m -d @$_EPOCH_TIMESTAMP $_FILE_NAME
```

## Description

Updates atime and mtime using a Unix epoch timestamp (seconds since 1970). Precise for script-based timestomping where epoch values are calculated dynamically.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Update access time | Built-in |
| -m | Update modification time | Built-in |
| -d | Set time via date string or epoch | Built-in |
| @$_EPOCH_TIMESTAMP | Epoch seconds prefixed with @ (e.g., @1667275140) | Yes |
| $_FILE_NAME | Target file | Yes |

## Examples

### Basic Usage

```bash
touch -a -m -d @1667275140 example
```

### Advanced Usage

```bash
touch -a -m -d @$(( $(date +%s) - 86400 )) example
```

## Expected Output

Silent on success. `stat --format='%Y' example` returns the epoch (e.g., `1667275140`).

## Related

- [[procedures/Linux-Timestomping-Evasion]]
