---
id: cmd-008
data: 'export CFLAGS="-fsanitize=address,undefined -fno-omit-frame-pointer -O1 -g"'
tags:
  - environment
  - sanitizers
type: command
output: Environment variable set
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.060Z'
verified: false
validated: true
submitted: true
---
# export-cflags-sanitizers

## Command

```bash
export CFLAGS="-fsanitize=address,undefined -fno-omit-frame-pointer -O1 -g"
```

## Description

Sets compiler flags for address/undefined sanitizers, debug, and optimization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `CFLAGS` | Flags string | Yes |

## Examples

### Basic Usage

```bash
export CFLAGS="-fsanitize=address -g"
```

## Expected Output

No output.

## Related

- [[commands/export-ldflags-sanitizers]]
