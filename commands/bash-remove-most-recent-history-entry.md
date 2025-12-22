---
id: 99b71f15-6f46-439b-a24c-07c578246d96
name: bash-remove-most-recent-history-entry
type: command
executor: bash
data: history -d -2 && history -d -1
output: null
created_at: '2023-04-06T03:56:17.657222+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-remove-most-recent-history-entry

## Command

```bash
history -d -2 && history -d -1
```

## Description

Deletes the two most recent history entries: the target command and this deletion command itself, preventing self-logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d -2 | Delete the second-to-last entry | Built-in |
| -d -1 | Delete the last entry (this command) | Built-in |

## Examples

### Basic Usage

```bash
history -d -2 && history -d -1
```

### Advanced Usage

Follow with `history -w` to persist to disk.

## Expected Output

No output. The recent entries are removed; `history` shows the updated list.

## Related

- [[procedures/Linux-Command-History-Evasion]]
