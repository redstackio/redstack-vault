---
data: export LDFLAGS="-fsanitize=address"
tags:
  - environment
  - asan
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.040Z'
id: 0eb0b85b-7f3e-40f1-89c4-59cc0615e232
verified: false
validated: true
submitted: true
---
# export-ldflags-asan

## Command

```bash
export LDFLAGS="-fsanitize=address"
```

## Description

Enables AddressSanitizer for linker flags in curl build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LDFLAGS | Linker flags | Yes |

## Examples

### Basic Usage

```bash
export LDFLAGS="-fsanitize=address"
```

## Expected Output

No output.

## Related

- [[commands/export-cflags-asan]]
- [[procedures/Clone-and-Build-curl-with-AddressSanitizer]]
