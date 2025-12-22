---
id: cmd-stat-passwd
name: stat-file-passwd
type: command
executor: bash
data: stat /tmp/passwd
output: >-
  Details like 1677722028528016 -rwxrwxrwx 1 James wheel 7 Aug 12 09:39:16 2016
  ... 4096 80 /tmp/passwd
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.213Z'
platforms:
  - Linux
tags:
  - testing
  - file-info
verified: false
validated: true
submitted: true
---

# stat-file-passwd

## Command

```bash
stat /tmp/passwd
```

## Description

Displays detailed file status (permissions, timestamps, etc.) of /tmp/passwd to verify changes after permission modifications in symlink testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Target file (/tmp/passwd) | Yes |

## Examples

### Basic Usage

```bash
stat /tmp/passwd
```

### Advanced Usage

```bash
stat /tmp/another_file
```

## Expected Output

File details including permissions, owner, size, and timestamps, e.g., -rwxrwxrwx 1 user group 7 bytes.

## Related

- [[commands/set-permissions-777-passwd]]
