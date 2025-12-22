---
id: cmd-gcc-parserbatch
data: gcc parserbatch.c -o parserbatch -lcurl
tags:
  - compile
  - libcurl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.060Z'
verified: false
validated: true
submitted: true
---
# compile-parserbatch-test

## Command

```bash
gcc parserbatch.c -o parserbatch -lcurl
```

## Description

Compiles a C source file testing libcurl's URL parsing for IPv6 zone IDs, linking against the libcurl library to demonstrate the omission flaw.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `parserbatch.c` | Source file with CURLU API test code | Yes |
| `-o parserbatch` | Output executable name | Yes |
| `-lcurl` | Link libcurl library | Yes |

## Examples

### Basic Usage

```bash
gcc parserbatch.c -o parserbatch -lcurl
```

### Advanced Usage

```bash
gcc -Wall parserbatch.c -o parserbatch -lcurl
```

> Adds warnings for debugging.

## Expected Output

No output if successful; compilation completes without errors.

## Related

- [[commands/run-parserbatch-test]]
