---
id: cmd-cat-proc-libphp
data: cat /proc/6318/maps | grep libphp | grep rw-p
tags:
  - memory-map
  - php
  - proc
type: command
output: >-
  7f4a8f9f3000-7f4a8fa0a000 rw-p 00471000 08:02 542265
  /usr/lib/apache2/modules/libphp7.2.so
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.269Z'
verified: false
validated: true
submitted: true
---
# cat-proc-maps-grep-libphp-rw-p

## Command

```bash
cat /proc/6318/maps | grep libphp | grep rw-p
```

## Description

Extracts read-write mapped regions of libphp from a process's memory maps (/proc/<pid>/maps) to locate the PHP heap for UAF exploitation planning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /proc/6318/maps | Path to process maps (replace 6318 with PID) | Yes |
| grep libphp | Filter for libphp | Yes |
| grep rw-p | Filter for rw-p permissions | Yes |

## Examples

### Basic Usage

```bash
cat /proc/6318/maps | grep libphp | grep rw-p
```

### Advanced Usage

For different PID: `cat /proc/<pid>/maps | grep libphp | grep rw-p`

## Expected Output

7f4a8f9f3000-7f4a8fa0a000 rw-p 00471000 08:02 542265 /usr/lib/apache2/modules/libphp7.2.so

## Related

- [[commands/cat-proc-maps-grep-rw-s]]
