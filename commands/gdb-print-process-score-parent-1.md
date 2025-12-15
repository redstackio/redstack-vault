---
id: cmd-gdb-parent-1
data: '(gdb) p ap_scoreboard_image->parent[1]'
tags:
  - debug
  - apache
  - process-score
type: command
output: (process_score *) 0x7f4a9323e044
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.244Z'
verified: false
validated: true
submitted: true
---
# gdb-print-process-score-parent-1

## Command

```gdb
(gdb) p ap_scoreboard_image->parent[1]
```

## Description

Prints the second process_score structure address in Apache's parent array to understand spacing for spraying modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p | Print command | Yes |
| ap_scoreboard_image->parent[1] | Access second parent entry | Yes |

## Examples

### Basic Usage

```gdb
(gdb) p ap_scoreboard_image->parent[1]
```

## Expected Output

(process_score *) 0x7f4a9323e044

## Related

- [[commands/gdb-print-process-score-parent-0]]
