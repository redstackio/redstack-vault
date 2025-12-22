---
id: b8d6efdf-255a-4c82-9d14-dc59abb151f4
name: cp-copy-libc-to-temp-dir
type: command
executor: bash
data: cp /lib/i386-linux-gnu/libc.so.6 $_RPATH_DIR/
output: null
created_at: '2023-04-06T03:56:19.401326+00:00'
updated_at: '2023-04-10T20:34:31.017246+00:00'
platforms:
  - Linux
tags:
  - post-exploitation
  - linux
verified: true
validated: true
---

# cp-copy-libc-to-temp-dir

## Command

```bash
cp /lib/i386-linux-gnu/libc.so.6 $_RPATH_DIR/
```

## Description

Copies the system libc.so.6 to a writable RPATH directory, preparing it as a base for modification in a library hijacking attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RPATH_DIR | Target writable directory (e.g., /var/tmp/flag15) | Yes |

## Examples

### Basic Usage

```bash
cp /lib/i386-linux-gnu/libc.so.6 /var/tmp/flag15/
```

### Advanced Usage

```bash
cp /lib64/libc.so.6 /tmp/malicious/
```

## Expected Output

No output on success; verify with `ls $_RPATH_DIR` showing libc.so.6.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Shared-Library-RPATH-Hijacking]]
- [[commands/ls-list-temp-dir-files]]
