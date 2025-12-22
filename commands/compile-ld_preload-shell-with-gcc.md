---
type: command
executor: bash
data: gcc -fPIC -shared -o /tmp/shell.so /tmp/shell.c -nostartfiles
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - compilation
  - gcc
verified: true
validated: true
---

# compile-ld_preload-shell-with-gcc

## Command

```bash
gcc -fPIC -shared -o /tmp/shell.so /tmp/shell.c -nostartfiles
```

## Description

Compiles a C source file (shell.c) into a shared object library (shell.so) suitable for LD_PRELOAD injection. The flags ensure position-independent code and dynamic linking without startup files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-fPIC` | Generate position-independent code for shared libraries | Yes |
| `-shared` | Produce a shared object file | Yes |
| `-o /tmp/shell.so` | Output file path | Yes |
| `/tmp/shell.c` | Input C source file | Yes |
| `-nostartfiles` | Omit standard startup files to avoid interference | Yes |

## Examples

### Basic Usage

```bash
gcc -fPIC -shared -o /tmp/shell.so /tmp/shell.c -nostartfiles
```

### With Different Paths

```bash
gcc -fPIC -shared -o ./malicious.so ./hijack.c -nostartfiles
```

## Expected Output

No output on success; produces /tmp/shell.so. Errors if source missing or gcc fails (e.g., 'gcc: error: shell.c: No such file or directory').

## Related

- [[procedures/linux-privilege-escalation-via-ld_preload-and-nopasswd]]
