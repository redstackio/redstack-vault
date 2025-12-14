---
id: cmd-007
data: export CC=clang
tags:
  - environment
  - compiler
type: command
output: Environment variable set
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.063Z'
verified: false
validated: true
submitted: true
---
# export-cc-clang

## Command

```bash
export CC=clang
```

## Description

Sets the C compiler to Clang for the build session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `CC=clang` | Compiler var | Yes |

## Examples

### Basic Usage

```bash
export CC=clang
```

## Expected Output

No output; variable set.

## Related

- [[commands/export-cflags-sanitizers]]
