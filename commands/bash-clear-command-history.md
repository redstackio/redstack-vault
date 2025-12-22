---
id: 0b079192-62cd-412b-8abd-e1dec1394051
name: bash-clear-command-history
type: command
executor: bash
data: history -c && history -w
output: null
created_at: '2023-04-06T03:56:17.657313+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-clear-command-history

## Command

```bash
history -c && history -w
```

## Description

Clears the in-memory Bash command history and writes the empty history to the disk file, effectively erasing all logged commands for the current user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Clear the history list from memory | Built-in |
| -w | Write the current history to the history file | Built-in |

## Examples

### Basic Usage

```bash
history -c && history -w
```

### Advanced Usage

Run after sensitive operations to wipe traces.

## Expected Output

No output produced. Verify success by running `history`, which should return an empty list, and check that `~/.bash_history` is empty or zero-length.

## Related

- [[procedures/Linux-Command-History-Evasion]]
