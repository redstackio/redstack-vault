---
id: cmd-gdb-parent-0
data: '(gdb) p ap_scoreboard_image->parent[0]'
tags:
  - debug
  - apache
  - process-score
type: command
output: >-
  { pid = 19447, generation = 0, quiescing = 0 '\000', not_accepting = 0 '\000',
  connections = 0, write_completion = 0, lingering_close = 0, keep_alive = 0,
  suspended = 0, bucket = 0 }
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.271Z'
verified: false
validated: true
submitted: true
---
# gdb-print-process-score-parent-0

## Command

```gdb
(gdb) p ap_scoreboard_image->parent[0]
```

## Description

Prints the first process_score structure in Apache's parent array from shared memory, including PID, generation, and bucket index, for inspecting worker associations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| p | Print command | Yes |
| ap_scoreboard_image->parent[0] | Access first parent entry | Yes |

## Examples

### Basic Usage

```gdb
(gdb) p ap_scoreboard_image->parent[0]
```

## Expected Output

{ pid = 19447, generation = 0, quiescing = 0 '\000', not_accepting = 0 '\000', connections = 0, write_completion = 0, lingering_close = 0, keep_alive = 0, suspended = 0, bucket = 0 }

## Related

- [[commands/gdb-print-ap-scoreboard-image]]
