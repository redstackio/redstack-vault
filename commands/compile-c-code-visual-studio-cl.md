---
id: aa5f5f85-7e39-42a7-b797-7f063849941d
name: compile-c-code-visual-studio-cl
type: command
executor: cmd
data: cl.exe /c /GS- $_SOURCE_FILE.c /Fo$_OBJECT_FILE.o
output: null
created_at: '2023-04-06T03:56:16.779348+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - compilation
  - cobalt-strike
  - obfuscation
verified: true
validated: true
---

# compile-c-code-visual-studio-cl

## Command

```cmd
cl.exe /c /GS- $_SOURCE_FILE.c /Fo$_OBJECT_FILE.o
```

## Description

Compiles a C source file into an object file (.o) using Microsoft's Visual Studio cl.exe compiler. This is used to prepare custom code for loading into Cobalt Strike Beacons, focusing on compile-only mode without linking or security checks to produce a loadable artifact.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOURCE_FILE | Name of the input C source file (without .c extension) | Yes |
| $_OBJECT_FILE | Name of the output object file (without .o extension) | Yes |
| /c | Compile without linking | Built-in |
| /GS- | Disable buffer security check | Built-in |
| /Fo | Specify output object file path | Built-in |

## Examples

### Basic Usage

```cmd
cl.exe /c /GS- hello.c /Fohello.o
```

Compiles hello.c into hello.o.

### Advanced Usage

```cmd
cl.exe /c /GS- /I$_INCLUDE_PATH custom_payload.c /Focustom_payload.o
```

Adds include path if needed for headers.

## Expected Output

Microsoft (R) C/C++ Optimizing Compiler Version ... for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

hello.c

(If successful, no errors; hello.o file created with size matching code complexity. Errors would show syntax issues.)

## Related

- [[procedures/Compile-C-Code-for-Cobalt-Strike-Beacon-Object-Files]]
- [[commands/compile-c-code-mingw-x86]]
