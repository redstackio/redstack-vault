---
data: gdb attach 10251
tags:
  - gdb
  - debugging
type: command
executor: bash
platforms:
  - Linux
id: dbbf56bc-2319-403d-a461-6d9b5d5bafd2
created_at: '2025-12-11T03:47:48.064Z'
updated_at: '2025-12-11T03:47:48.064Z'
verified: false
validated: true
submitted: true
---
# gdb-attach

## Command

```bash
gdb attach 10251
```

## Description

Attaches GDB to a running process by PID for debugging, used here to attach to mirb before triggering the crash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| attach | Attaches to the specified process ID | Yes |
| 10251 | Example PID; replace with actual | Yes |

## Examples

### Basic Usage

```bash
gdb attach 10251
```

## Expected Output

GDB attaches to the process and loads symbols, ready for further commands.

## Related

- [[commands/gdb-continue]]
- [[procedures/Debug-mruby-Crash-with-GDB]]
