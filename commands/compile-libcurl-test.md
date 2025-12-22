---
id: cmd-gcc-parserbatch-001
data: gcc parserbatch.c -o parserbatch -lcurl
tags:
  - compile
  - build
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.528Z'
verified: false
validated: true
submitted: true
---
# compile-libcurl-test

## Command

```bash
gcc parserbatch.c -o parserbatch -lcurl
```

## Description

Compiles a C source file testing libcurl's URL parsing for IPv6 zone identifiers, linking against the libcurl library to create an executable for demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `parserbatch.c` | Source file with URL parsing test code | Yes |
| `-o parserbatch` | Output executable name | Yes |
| `-lcurl` | Link libcurl library | Yes |

## Examples

### Basic Usage

```bash
gcc parserbatch.c -o parserbatch -lcurl
```

### Advanced Usage

```bash
gcc -g parserbatch.c -o parserbatch -lcurl  # With debug symbols
```

## Expected Output

No output if successful; compilation errors if libcurl missing or code issues.

## Related

- [[commands/run-libcurl-parsing-test]]
