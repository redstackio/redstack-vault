---
data: strace -p <server_pid> -e trace=network -o strace.log
tags:
  - strace
  - tracing
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.397Z'
id: 12b7c4d0-2c9c-4f61-9547-d665b3fd2844
verified: false
validated: true
submitted: true
---
# strace-trace-server

## Command

```bash
strace -p <server_pid> -e trace=network -o strace.log
```

## Description

Attaches strace to a running server process to trace network-related system calls, useful for debugging anomalies during load testing without server restarts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p <server_pid>` | PID of the target server process | Yes |
| `-e trace=network` | Limit to network syscalls (accept, send, recv) | No (default all) |
| `-o strace.log` | Output file for traces | Yes |

## Examples

### Basic Usage

```bash
strace -p 1234 -e trace=network -o server_trace.log
```

### Advanced Usage

```bash
strace -p 1234 -e trace=network,read,write -f -o full_trace.log
```

(Includes forking with -f for multi-threaded servers.)

## Expected Output

Log file with entries like "[pid 1234] accept(3, ..., ) = 4\n[pid 1234] sendto(4, \"HTTP/1.1 200 OK...\", 1024, 0, NULL, 0) = 1024", showing normal operations.

## Related

- [[procedures/Trace-Server-System-Calls-with-strace]]
