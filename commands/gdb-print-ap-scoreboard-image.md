---
id: cmd-gdb-ap-scoreboard
data: (gdb) p *ap_scoreboard_image
tags:
  - debug
  - apache
  - shm
type: command
output: '{ global = 0x7f4a9323e008, parent = 0x7f4a9323e020, servers = 0x55835eddea78 }'
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.273Z'
verified: false
validated: true
submitted: true
---
# gdb-print-ap-scoreboard-image

## Command

```gdb
(gdb) p *ap_scoreboard_image
```

## Description

Prints the ap_scoreboard_image structure in GDB to view pointers to Apache's global, parent, and servers shared memory blocks during debugging of mod_prefork.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p | Print command | Yes |
| *ap_scoreboard_image | Dereference the scoreboard image | Yes |

## Examples

### Basic Usage

```gdb
(gdb) p *ap_scoreboard_image
```

### Advanced Usage

Attach first: `(gdb) attach <pid>` then run the print.

## Expected Output

{ global = 0x7f4a9323e008, parent = 0x7f4a9323e020, servers = 0x55835eddea78 }

## Related

- [[commands/gdb-print-process-score-parent-0]]
