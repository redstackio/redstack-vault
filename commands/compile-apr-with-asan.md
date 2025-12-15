---
data: gcc -g -fsanitize=address $(pkg-config --cflags --libs apr-1) input.c
tags:
  - asan
  - compilation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.050Z'
id: 2c4ea2d6-61d4-4537-a3bf-6b86c32999c5
verified: false
validated: true
submitted: true
---
# Compile APR with ASAN

## Command

```bash
gcc -g -fsanitize=address $(pkg-config --cflags --libs apr-1) input.c
```

## Description

Compiles APR code with debug and ASAN to show undetected overflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -g | Debug info | Yes |
| -fsanitize=address | Enable ASAN | Yes |
| $(pkg-config --cflags --libs apr-1) | APR flags | Yes |
| input.c | Source file | Yes |

## Examples

### Basic Usage

```bash
gcc -g -fsanitize=address $(pkg-config --cflags --libs apr-1) input.c
```

## Expected Output

No ASAN error; garbled output on run.

## Related

- [[commands/compile-malloc-with-asan]]
