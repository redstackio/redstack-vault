---
id: cmd-gdb-all-buckets
data: (gdb) p all_buckets
tags:
  - debug
  - apache
  - buckets
type: command
output: (prefork_child_bucket *) 0x7f4a9336b3f0
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.248Z'
verified: false
validated: true
submitted: true
---
# gdb-print-all-buckets

## Command

```gdb
(gdb) p all_buckets
```

## Description

Prints the address of the all_buckets array in Apache mod_prefork for structure matching and inspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p | Print command | Yes |
| all_buckets | The buckets array symbol | Yes |

## Examples

### Basic Usage

```gdb
(gdb) p all_buckets
```

## Expected Output

(prefork_child_bucket *) 0x7f4a9336b3f0

## Related

- [[commands/gdb-print-ap-scoreboard-image]]
