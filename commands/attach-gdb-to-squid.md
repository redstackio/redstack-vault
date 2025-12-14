---
id: cmd-uuid-7
data: gdb -q -p $(pgrep squid | tail -n 1)
tags:
  - debug
  - attach
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.194Z'
verified: false
validated: true
submitted: true
---
# attach-gdb-to-squid

## Command

```bash
gdb -q -p $(pgrep squid | tail -n 1)
```

## Description

Attaches GDB quietly to the Squid child process for debugging crashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -q | Quiet mode | Yes |
| -p | Attach to PID | Yes |

## Examples

### Basic Usage

```bash
gdb -q -p $(pgrep squid | tail -n 1)
```

### Advanced Usage

```bash
gdb -q -p 1234 -ex "set pagination off"
```

## Expected Output

GDB prompt attached to process.

## Related

- [[Related Procedure: Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]
