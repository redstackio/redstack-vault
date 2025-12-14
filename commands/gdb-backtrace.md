---
id: cmd-uuid-8
data: (gdb) bt
tags:
  - debug
  - backtrace
type: command
output: null
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.190Z'
verified: false
validated: true
submitted: true
---
# gdb-backtrace

## Command

```bash
(gdb) bt
```

## Description

Prints the backtrace of the call stack in GDB after a crash.

## Parameters

None.

## Examples

### Basic Usage

```bash
(gdb) bt
```

### Advanced Usage

```bash
(gdb) bt full
```

## Expected Output

Stack trace from raise() to CacheManager::ParseHeaders.

## Related

- [[Related Procedure: Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]
