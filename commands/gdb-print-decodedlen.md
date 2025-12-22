---
id: cmd-uuid-9
data: (gdb) p decodedLen
tags:
  - debug
  - variable
type: command
output: null
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.187Z'
verified: false
validated: true
submitted: true
---
# gdb-print-decodedlen

## Command

```bash
(gdb) p decodedLen
```

## Description

Prints the value of the decodedLen variable in GDB to confirm overflow size.

## Parameters

None.

## Examples

### Basic Usage

```bash
(gdb) p decodedLen
```

### Advanced Usage

```bash
(gdb) print decodedLen
```

## Expected Output

$21 = 43011.

## Related

- [[Related Procedure: Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]
