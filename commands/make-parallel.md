---
data: make -j$(nproc)
tags:
  - build
  - compile
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.033Z'
id: a45446c9-2e96-4cc6-a1d7-07db793b3c87
verified: false
validated: true
submitted: true
---
# make-parallel

## Command

```bash
make -j$(nproc)
```

## Description

Compiles curl using all available CPU cores for faster build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -j | Number of jobs | Yes |
| $(nproc) | CPU count | Yes |

## Examples

### Basic Usage

```bash
make -j$(nproc)
```

## Expected Output

Compilation progress, ends with built binaries.

## Related

- [[commands/configure-curl]]
- [[procedures/Clone-and-Build-curl-with-AddressSanitizer]]
