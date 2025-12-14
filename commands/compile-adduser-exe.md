---
data: i686-w64-mingw32-gcc adduser.c -o adduser.exe
tags:
  - compilation
  - payload
type: command
output: |-
  adduser.c: In function 'main':
  adduser.c:5: warning: implicit declaration of function 'system'
  Compilation successful; adduser.exe generated.
executor: bash
platforms:
  - Linux
  - Windows
id: 74fb6c20-48b3-43f7-9866-137e093d3f1b
created_at: '2025-12-14T17:26:17.547Z'
updated_at: '2025-12-14T17:26:17.547Z'
verified: false
validated: true
submitted: true
---
# compile-adduser-exe

## Command

```bash
i686-w64-mingw32-gcc adduser.c -o adduser.exe
```

## Description

Compiles a C source file into a 32-bit Windows executable using MinGW cross-compiler, creating a payload that adds a local admin user when run.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| adduser.c | Source C file with net commands in system() calls | Yes |
| -o adduser.exe | Output flag and executable name | Yes |

## Examples

### Basic Usage

```bash
i686-w64-mingw32-gcc adduser.c -o adduser.exe
```

### Advanced Usage

```bash
i686-w64-mingw32-gcc -static adduser.c -o adduser.exe
```
(Static linking for portability)

## Expected Output

Successful compilation with warnings about implicit declarations; adduser.exe binary produced.

## Related

- [[procedures/Compile-and-Place-Malicious-Executable-for-Path-Hijacking]]
