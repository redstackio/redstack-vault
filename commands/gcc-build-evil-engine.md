---
data: gcc -fPIC -shared -o evil_engine.so evil_engine.c
tags:
  - compilation
  - gcc
type: command
executor: bash
platforms:
  - Linux
  - POSIX
id: 81079dc5-3f57-456f-995f-b92ce58fda7b
created_at: '2025-12-14T17:23:31.198Z'
updated_at: '2025-12-14T17:23:31.198Z'
verified: false
validated: true
submitted: true
---
# gcc-build-evil-engine

## Command

```bash
gcc -fPIC -shared -o evil_engine.so evil_engine.c
```

## Description

Compiles C source into a position-independent shared library for malicious payload in curl RCE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-fPIC` | Generate position-independent code | Yes |
| `-shared` | Create a shared object file | Yes |
| `-o` | Output file name (evil_engine.so) | Yes |
| `evil_engine.c` | Input source file | Yes |

## Examples

### Basic Usage

```bash
gcc -fPIC -shared -o evil_engine.so evil_engine.c
```

### Advanced Usage

Add debug: gcc -fPIC -shared -g -o evil_engine.so evil_engine.c

## Expected Output

No output if successful; creates evil_engine.so file

## Related

- [[procedures/Compile-Malicious-Payload-with-gcc]]
