---
data: gcc -g -fsanitize=address $(pkg-config --cflags --libs apr-1) input.c
tags:
  - asan
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.036Z'
id: b9e05435-3766-4a8f-b90e-d77d8fbcf64f
verified: false
validated: true
submitted: true
---
# Compile APR Debug ASAN

## Command

```bash
gcc -g -fsanitize=address $(pkg-config --cflags --libs apr-1) input.c
```

## Description

Compiles APR with debug mode and ASAN after --enable-pool-debug=yes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -g | Debug | Yes |
| -fsanitize=address | ASAN | Yes |
| $(pkg-config --cflags --libs apr-1) | APR | Yes |
| input.c | Source | Yes |

## Examples

### Basic Usage

```bash
gcc -g -fsanitize=address $(pkg-config --cflags --libs apr-1) input.c
```

## Expected Output

ASAN detects overflow.

## Related

- [[commands/compile-apr-with-asan]]
