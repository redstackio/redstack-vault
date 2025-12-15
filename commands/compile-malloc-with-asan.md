---
data: gcc -g -fsanitize=address input.c -o a.out
tags:
  - asan
  - malloc
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.042Z'
id: 100d7940-7ebf-4cb3-ac74-7620d5e754d0
verified: false
validated: true
submitted: true
---
# Compile Malloc with ASAN

## Command

```bash
gcc -g -fsanitize=address input.c -o a.out
```

## Description

Compiles malloc-based code with ASAN to verify overflow detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -g | Debug | Yes |
| -fsanitize=address | ASAN | Yes |
| input.c | Malloc buffer source | Yes |
| -o a.out | Output binary | Yes |

## Examples

### Basic Usage

```bash
gcc -g -fsanitize=address input.c -o a.out
```

## Expected Output

ASAN heap-buffer-overflow error with trace.

## Related

- [[commands/compile-apr-with-asan]]
