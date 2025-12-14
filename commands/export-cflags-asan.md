---
data: export CFLAGS="-fsanitize=address"
tags:
  - environment
  - asan
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.050Z'
id: 14f20e75-1acf-4839-bc0e-918354d8f8fc
verified: false
validated: true
submitted: true
---
# export-cflags-asan

## Command

```bash
export CFLAGS="-fsanitize=address"
```

## Description

Enables AddressSanitizer for C compilation flags in curl build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CFLAGS | Compilation flags | Yes |

## Examples

### Basic Usage

```bash
export CFLAGS="-fsanitize=address"
```

## Expected Output

No output; verify with echo $CFLAGS.

## Related

- [[commands/export-cxxflags-asan]]
- [[procedures/Clone-and-Build-curl-with-AddressSanitizer]]
