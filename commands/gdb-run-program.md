---
data: r
tags:
  - gdb
  - run
  - execute
type: command
output: null
executor: gdb
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.666Z'
id: 69d80943-5960-4fae-923e-1cf6f450b678
verified: false
validated: true
submitted: true
---
# gdb-run-program

## Command

```gdb
r
```

## Description

Runs the loaded program within GDB to execute the multi-threaded curl example and trigger the DNS timeout race condition.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| r | Alias for 'run' command | Yes |

## Examples

### Basic Usage

```gdb
r
```

### Advanced Usage

```gdb
r arg1 arg2
```

## Expected Output

Program executes, creates threads for URL fetches, hits DNS timeout, triggers SIGSEGV: Thread 1 "multithread" received signal SIGSEGV, Segmentation fault. 0x00007ffff7f42b32 in Curl_failf () from ./lib/.libs/libcurl.so.4

## Related

- [[commands/gdb-launch-multithread]]
- [[commands/gdb-backtrace]]
