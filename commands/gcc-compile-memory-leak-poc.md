---
data: gcc memory_leak_poc.c -o memory_leak_poc
tags:
  - compilation
  - poc
type: command
output: 'Compiles without errors, producing executable ''memory_leak_poc'''
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.295Z'
id: 2a697faa-192c-432a-af77-98ac004b155c
verified: false
validated: true
submitted: true
---
# gcc-compile-memory-leak-poc

## Command

```bash
gcc memory_leak_poc.c -o memory_leak_poc
```

## Description

Compiles the C source file containing the vulnerable `bytes_to_hexstring` function and a test loop into an executable binary for demonstrating the memory leak.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `memory_leak_poc.c` | Source file with vulnerable code | Yes |
| `-o memory_leak_poc` | Output executable name | Yes |

## Examples

### Basic Usage

```bash
gcc memory_leak_poc.c -o memory_leak_poc
```

### Advanced Usage

```bash
gcc -Wall -g memory_leak_poc.c -o memory_leak_poc
```

## Expected Output

No errors; generates 'memory_leak_poc' executable file.

## Related

- [[Related Procedure: Compile-Memory-Leak-PoC]]
