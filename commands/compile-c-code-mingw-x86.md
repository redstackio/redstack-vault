---
id: 708f022e-7b13-438d-9b34-2f6b9e6dc713
name: compile-c-code-mingw-x86
type: command
executor: bash
data: i686-w64-mingw32-gcc -c $_SOURCE_FILE.c -o $_OBJECT_FILE.o
output: null
created_at: '2023-04-06T03:56:16.779401+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - compilation
  - mingw
  - x86
  - cobalt-strike
verified: true
validated: true
---

# compile-c-code-mingw-x86

## Command

```bash
i686-w64-mingw32-gcc -c $_SOURCE_FILE.c -o $_OBJECT_FILE.o
```

## Description

Compiles a C source file into a 32-bit object file (.o) using the MinGW-w64 i686 cross-compiler. Ideal for preparing x86-compatible code for Cobalt Strike Beacon object loading in evasion scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOURCE_FILE | Input C source filename (without .c) | Yes |
| $_OBJECT_FILE | Output object filename (without .o) | Yes |
| -c | Compile to object file only (no linking) | Built-in |
| -o | Specify output file | Built-in |

## Examples

### Basic Usage

```bash
i686-w64-mingw32-gcc -c hello.c -o hello.o
```

Generates 32-bit hello.o from hello.c.

### Advanced Usage

```bash
i686-w64-mingw32-gcc -c -m32 hello.c -o hello.o
```

Explicitly enforces 32-bit mode.

## Expected Output

(No output if successful; check with `ls -la` for hello.o creation. Errors: `hello.c:1: error: ...` for syntax issues.)

## Related

- [[procedures/Compile-C-Code-for-Cobalt-Strike-Beacon-Object-Files]]
- [[commands/compile-c-code-mingw-x64]]
