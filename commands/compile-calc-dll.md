---
id: cmd-compile-calc-dll-001
data: x86_64-w64-mingw32-g++ calc.c -o calc.dll -shared
tags:
  - compilation
  - cross-compile
type: command
output: calc.dll generated without compilation errors.
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.945Z'
verified: false
validated: true
submitted: true
---
# compile-calc-dll

## Command

```bash
x86_64-w64-mingw32-g++ calc.c -o calc.dll -shared
```

## Description

Cross-compiles C source calc.c into a Windows shared DLL for malicious OpenSSL Engine, with DllMain executing system("calc").

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `calc.c` | Input C source file | Yes |
| `-o calc.dll` | Output DLL name | Yes |
| `-shared` | Compile as shared library | Yes |

## Examples

### Basic Usage

```bash
x86_64-w64-mingw32-g++ calc.c -o calc.dll -shared
```

### Advanced Usage

Add debug: x86_64-w64-mingw32-g++ -g calc.c -o calc.dll -shared

## Expected Output

calc.dll binary generated.

## Related

- [[tools/x86_64-w64-mingw32-gpp]]
