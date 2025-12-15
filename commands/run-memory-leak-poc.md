---
data: ./memory_leak_poc
tags:
  - execution
  - dos
type: command
output: >-
  Outputs iteration progress and memory usage, e.g., 'Starting memory leak
  test... Iteration 0: Memory usage: 1776 KB' up to 'Memory usage: 32588 KB'
  after completion
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.292Z'
id: 8b755c05-748f-4356-bec4-a67070f17f18
verified: false
validated: true
submitted: true
---
# run-memory-leak-poc

## Command

```bash
./memory_leak_poc
```

## Description

Executes the PoC binary to run a loop calling `bytes_to_hexstring` 1,000,000 times without freeing memory, printing usage via getrusage every 100,000 iterations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./memory_leak_poc` | Path to compiled executable | Yes |

## Examples

### Basic Usage

```bash
./memory_leak_poc
```

### Advanced Usage

```bash
./memory_leak_poc > output.log 2>&1
```

## Expected Output

Console logs of iterations and KB memory usage increasing progressively.

## Related

- [[Related Procedure: Execute-Memory-Leak-PoC]]
