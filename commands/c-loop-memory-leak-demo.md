---
data: >-
  for (int i = 0; i < 10000; i++) { uint8_t data[10] = {0x00, 0x01, 0x02, 0x03,
  0x04, 0x05, 0x06, 0x07, 0x08, 0x09}; char* hex_str = bytes_to_hexstring(data,
  10); // Do something with hex_str but forget to free it }
tags:
  - code-snippet
  - memory-leak
type: command
output: >-
  Allocates memory each iteration without release, leading to leak; no direct
  output but observable via memory monitors
executor: c
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.290Z'
id: 774f6ecb-3431-4344-b9a0-e29e7700338a
verified: false
validated: true
submitted: true
---
# c-loop-memory-leak-demo

## Command

```c
for (int i = 0; i < 10000; i++) { uint8_t data[10] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09}; char* hex_str = bytes_to_hexstring(data, 10); // Do something with hex_str but forget to free it }
```

## Description

C code snippet simulating repeated calls to the vulnerable function without freeing the returned string, illustrating the leak in application code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Loop counter from 0 to 9999 | Yes |
| `data` | Sample byte array of length 10 | Yes |
| `bytes_to_hexstring(data, 10)` | Function call with data and length | Yes |

## Examples

### Basic Usage

```c
for (int i = 0; i < 10000; i++) { ... }
```

### Advanced Usage

Embed in main() and compile with larger iterations for bigger leak.

## Expected Output

No console output; memory leak observable via tools like top.

## Related

- [[Related Procedure: Execute-Memory-Leak-PoC]]
