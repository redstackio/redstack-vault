---
id: 725d499e-30f5-4584-92fa-65ebb36f4ca3
name: gcc-compile-c-source-to-binary
type: command
executor: bash
data: gcc -o $_OUTPUT_BINARY $_SOURCE_FILE
output: null
created_at: '2019-09-17T20:10:55.530193+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - Build
  - Compilation
verified: true
validated: true
---

# gcc-compile-c-source-to-binary

## Command

```bash
gcc -o $_OUTPUT_BINARY $_SOURCE_FILE
```

## Description

This command compiles a C source file into an executable binary using GCC. It's a fundamental step in building custom security tools, exploits, or payloads from source code, allowing for environment-specific customization to evade detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_OUTPUT_BINARY` | Name of the output executable file (e.g., suid) | Yes |
| `$_SOURCE_FILE` | Path to the input C source file (e.g., suid.c) | Yes |
| `-o` | Flag to specify output file | Built-in |

## Examples

### Basic Usage

Compile suid.c to suid binary:

```bash
gcc -o suid suid.c
gcc-compile-c-source-to-binary
```

### Advanced Usage

Compile with warnings and optimization:

```bash
gcc -Wall -O2 -o exploit exploit.c
gcc-compile-c-source-to-binary
```

## Expected Output

Successful compilation produces no output or warnings if clean; the binary file is created in the current directory. Verify with:

```
root@hackers:~# gcc -o suid suid.c
root@hackers:~# ls -l suid
-rwxr-xr-x 1 root root 8744 Sep 17 20:10 suid
root@hackers:~# ./suid
# 
```

If errors occur, GCC outputs diagnostic messages like syntax errors or missing headers.

## Related

- [[Related Procedure: Build Custom SUID Exploit]]
- [[tools/GCC]] (parent tool)
