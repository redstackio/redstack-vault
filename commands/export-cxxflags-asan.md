---
data: export CXXFLAGS="-fsanitize=address"
tags:
  - environment
  - asan
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.045Z'
id: aa363e44-4da7-45c7-b5c1-f5f2cb5c58aa
verified: false
validated: true
submitted: true
---
# export-cxxflags-asan

## Command

```bash
export CXXFLAGS="-fsanitize=address"
```

## Description

Enables AddressSanitizer for C++ compilation in curl build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CXXFLAGS | C++ flags | Yes |

## Examples

### Basic Usage

```bash
export CXXFLAGS="-fsanitize=address"
```

## Expected Output

No output.

## Related

- [[commands/export-cflags-asan]]
- [[procedures/Clone-and-Build-curl-with-AddressSanitizer]]
