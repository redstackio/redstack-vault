---
id: 973a5c08-a285-4230-b3dc-5a804f7a26da
name: compile-c-code-mingw-x64
type: command
executor: bash
data: x86_64-w64-mingw32-gcc -c $_SOURCE_FILE.c -o $_OBJECT_FILE.o
output: null
created_at: '2023-04-06T03:56:16.779476+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - compilation
  - mingw
  - x64
  - cobalt-strike
verified: true
validated: true
---

# compile-c-code-mingw-x64

## Command

```bash
x86_64-w64-mingw32-gcc -c $_SOURCE_FILE.c -o $_OBJECT_FILE.o
```

## Description

Compiles a C source file into a 64-bit object file (.o) using the MinGW-w64 x86_64 cross-compiler. Used to create artifacts for 64-bit Cobalt Strike Beacons in defense evasion workflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOURCE_FILE | Input C source filename (without .c) | Yes |
| $_OBJECT_FILE | Output object filename (without .o) | Yes |
| -c | Compile to object file only | Built-in |
| -o | Specify output file | Built-in |

## Examples

### Basic Usage

```bash
x86_64-w64-mingw32-gcc -c hello.c -o hello.o
```

Produces 64-bit hello.o.

### Advanced Usage

```bash
x86_64-w64-mingw32-gcc -c -m64 hello.c -o hello.o
```

Ensures 64-bit targeting.

## Expected Output

(Silent success; verify with `file $_OBJECT_FILE.o` showing PE-X86-64. Errors indicate compilation failures.)

## Related

- [[procedures/Compile-C-Code-for-Cobalt-Strike-Beacon-Object-Files]]
- [[commands/compile-c-code-mingw-x86]]
