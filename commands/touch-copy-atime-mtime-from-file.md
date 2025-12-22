---
id: 432f2b74-8bd6-4fb3-b90b-90c93376468a
name: touch-copy-atime-mtime-from-file
type: command
executor: bash
data: touch -a -m -r $_REFERENCE_FILE $_TARGET_FILE
output: null
created_at: '2023-04-06T03:56:17.808716+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - timestamp-copy
verified: true
validated: true
---

# touch-copy-atime-mtime-from-file

## Command

```bash
touch -a -m -r $_REFERENCE_FILE $_TARGET_FILE
```

## Description

Copies atime and mtime from a reference file to the target, making the target appear as old or recent as the reference for blending with legitimate files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Update access time | Built-in |
| -m | Update modification time | Built-in |
| -r | Reference file for timestamps | Built-in |
| $_REFERENCE_FILE | Source file (e.g., /bin/ls) | Yes |
| $_TARGET_FILE | Destination file | Yes |

## Examples

### Basic Usage

```bash
touch -a -m -r /bin/ls example
```

### Advanced Usage

```bash
touch -a -m -r legitimate.log malicious.payload
```

## Expected Output

No output. `ls -l` on both files shows matching timestamps (e.g., same date for both).

## Related

- [[procedures/Linux-Timestomping-Evasion]]
