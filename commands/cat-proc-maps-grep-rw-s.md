---
id: cmd-cat-proc-rw-s
data: cat /proc/6318/maps | grep rw-s
tags:
  - memory-map
  - shm
  - proc
type: command
output: '7f4a9323e000-7f4a93252000 rw-s 00000000 00:05 57052 /dev/zero (deleted)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.265Z'
verified: false
validated: true
submitted: true
---
# cat-proc-maps-grep-rw-s

## Command

```bash
cat /proc/6318/maps | grep rw-s
```

## Description

Identifies shared read-write memory regions (SHM) from process memory maps for targeting in Apache exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /proc/6318/maps | Path to process maps | Yes |
| grep rw-s | Filter for rw-s (shared) permissions | Yes |

## Examples

### Basic Usage

```bash
cat /proc/6318/maps | grep rw-s
```

## Expected Output

7f4a9323e000-7f4a93252000 rw-s 00000000 00:05 57052 /dev/zero (deleted)

## Related

- [[commands/cat-proc-maps-grep-libphp-rw-p]]
