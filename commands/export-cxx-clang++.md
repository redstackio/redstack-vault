---
data: export CXX=clang++
tags:
  - environment
  - compiler
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.053Z'
id: 0b760ec3-5df5-4dd3-8694-b5444ea29256
verified: false
validated: true
submitted: true
---
# export-cxx-clang++

## Command

```bash
export CXX=clang++
```

## Description

Sets the C++ compiler to Clang++ for ASan in curl build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CXX | C++ compiler path | Yes |

## Examples

### Basic Usage

```bash
export CXX=clang++
```

## Expected Output

No output; verify with echo $CXX.

## Related

- [[commands/export-cc-clang]]
- [[procedures/Clone-and-Build-curl-with-AddressSanitizer]]
