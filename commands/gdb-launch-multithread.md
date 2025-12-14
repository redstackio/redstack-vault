---
data: 'LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb ./multithread'
tags:
  - debug
  - gdb
  - library-path
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.671Z'
id: 7dfc3728-8901-4b02-897b-3ca563dd4313
verified: false
validated: true
submitted: true
---
# gdb-launch-multithread

## Command

```bash
LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb ./multithread
```

## Description

Launches the multi-threaded curl example under GDB with a prepended library path to load the custom vulnerable libcurl.so.4, enabling crash reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LD_LIBRARY_PATH | Prepends ./lib/.libs to search path for custom libcurl | Yes |
| gdb | GNU Debugger invocation | Yes |
| ./multithread | Path to compiled executable | Yes |

## Examples

### Basic Usage

```bash
LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb ./multithread
```

### Advanced Usage

```bash
LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb --args ./multithread url1 url2
```

## Expected Output

GDB starts, loads symbols (may note no debugging symbols), allows running the program. Prompt: (gdb) 

## Related

- [[commands/gdb-run-program]]
- [[procedures/Reproduce-Crash-with-GDB]]
