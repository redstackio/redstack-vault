---
id: 689db723-27f2-4022-bfa3-a478ebbc815a
name: touch-set-atime-mtime-yyyymmddhhmm
type: command
executor: bash
data: touch -a -m -t $_TIMESTAMP $_FILE_NAME
output: null
created_at: '2023-04-06T03:56:17.808597+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - timestamp-modification
verified: true
validated: true
---

# touch-set-atime-mtime-yyyymmddhhmm

## Command

```bash
touch -a -m -t $_TIMESTAMP $_FILE_NAME
```

## Description

Sets the access (atime) and modification (mtime) times of a file to a specific date/time in YYYYMMDDhhmm format. Helps in aligning file metadata to evade detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Update access time | Built-in |
| -m | Update modification time | Built-in |
| -t | Set time in YYYYMMDDhhmm (e.g., 202210312359) | Built-in |
| $_TIMESTAMP | The timestamp string (12 characters) | Yes |
| $_FILE_NAME | Target file | Yes |

## Examples

### Basic Usage

```bash
touch -a -m -t 202210312359 example
```

### Advanced Usage

```bash
touch -a -m -t 202301011200 example
```

## Expected Output

No output on success. Use `stat example` to confirm: `Access: 2022-10-31 23:59:00.000000000 +0000`, `Modify: 2022-10-31 23:59:00.000000000 +0000`.

## Related

- [[procedures/Linux-Timestomping-Evasion]]
