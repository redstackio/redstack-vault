---
id: cmd-016
data: echo $?
tags:
  - verify
  - status
type: command
output: 0 for success
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.015Z'
verified: false
validated: true
submitted: true
---
# echo-build-status

## Command

```bash
echo $?
```

## Description

Prints the exit status of the previous command (e.g., make).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$?` | Exit code | Yes |

## Examples

### Basic Usage

```bash
echo $?
```

## Expected Output

0

## Related

- [[commands/make-parallel-build]]
