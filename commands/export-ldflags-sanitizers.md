---
id: cmd-009
data: 'export LDFLAGS="-fsanitize=address,undefined"'
tags:
  - environment
  - linker
type: command
output: Environment variable set
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.058Z'
verified: false
validated: true
submitted: true
---
# export-ldflags-sanitizers

## Command

```bash
export LDFLAGS="-fsanitize=address,undefined"
```

## Description

Sets linker flags for sanitizers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `LDFLAGS` | Linker flags | Yes |

## Examples

### Basic Usage

```bash
export LDFLAGS="-fsanitize=address"
```

## Expected Output

No output.

## Related

- [[commands/configure-curl-build]]
