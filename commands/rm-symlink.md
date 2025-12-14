---
data: rm example_bash_operator.py.log
tags:
  - cleanup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.459Z'
id: e415aecc-c0b0-4c5f-a667-4a770c5eeef3
verified: false
validated: true
submitted: true
---
# rm-symlink

## Command

```bash
rm example_bash_operator.py.log
```

## Description

Removes the symlink after use to clean up and avoid detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `example_bash_operator.py.log` | Symlink file name | Yes |

## Examples

### Basic Usage

```bash
rm example_bash_operator.py.log
```

## Expected Output

No output if successful.

## Related

- [[commands/wait-for-poc-file]]
