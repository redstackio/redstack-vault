---
id: 3ed431fc-a202-4d8c-8114-09b9f2c28a65
name: gcc-compile-malicious-dll-x64
type: command
executor: bash
data: x86_64-w64-mingw32-gcc $_SOURCE_C -shared -o $_OUTPUT_DLL
output: null
created_at: '2023-04-06T03:56:29.436687+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
platforms:
  - Linux
tags:
  - dll-hijacking
  - compilation
verified: true
validated: true
---

# gcc-compile-malicious-dll-x64

## Command

```bash
x86_64-w64-mingw32-gcc $_SOURCE_C -shared -o $_OUTPUT_DLL
```

## Description

Compiles a C source file into a 64-bit Windows DLL using MinGW cross-compiler, for use in DLL hijacking attacks against Windows services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOURCE_C | Path to C source file (e.g., windows_dll.c) | Yes |
| $_OUTPUT_DLL | Output DLL name (e.g., malicious.dll) | Yes |
| -shared | Builds shared library (DLL) | Built-in |

## Examples

### Basic Usage

```bash
x86_64-w64-mingw32-gcc windows_dll.c -shared -o malicious.dll
```

## Expected Output

No output on success; generates malicious.dll file ready for deployment.

## Related

- [[codes/Malicious-DLL-for-Service-Hijack]]
- [[procedures/Windows-Local-Service-Permissions-Escalation]]
