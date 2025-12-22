---
data: gcc $(pkg-config --cflags --libs apr-1) input.c
tags:
  - compilation
  - apr
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.055Z'
id: 49375447-6fd5-4822-8183-301e54586557
verified: false
validated: true
submitted: true
---
# Compile APR Pool Sample

## Command

```bash
gcc $(pkg-config --cflags --libs apr-1) input.c
```

## Description

Compiles a C sample using APR pool allocator to demonstrate buffer overflow without sanitizer detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $(pkg-config --cflags --libs apr-1) | APR compile flags and libs | Yes |
| input.c | Source with pool buffers and strcpy | Yes |

## Examples

### Basic Usage

```bash
gcc $(pkg-config --cflags --libs apr-1) input.c
```

### Advanced Usage

Add -o output for naming: gcc $(pkg-config --cflags --libs apr-1) input.c -o test

## Expected Output

Executable that runs to show garbled strings from overflow.

## Related

- [[commands/compile-apr-with-asan]]
