---
data: umask 0
tags:
  - permissions
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.494Z'
id: cb05c337-d22f-4bfb-8d53-6a1c38c931a7
verified: false
validated: true
submitted: true
---
# umask-0

## Command

```bash
umask 0
```

## Description

Sets the file creation mask (umask) to 0 in the current shell, allowing new files and directories to have full permissions (world-readable, writable, executable). Used in PoC to simulate Airflow daemon mode's insecure default.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0` | Umask value (no bits masked, full permissions) | Yes |

## Examples

### Basic Usage

```bash
umask 0
```

### Verify Change

```bash
touch testfile
ls -l testfile  # Shows 666 permissions
```

## Expected Output

No output; changes shell's umask. Verify with `umask` command showing 0000.

## Related

- [[commands/cd-to-scheduler-logs]]
