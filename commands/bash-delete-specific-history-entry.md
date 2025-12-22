---
id: a9eb6de6-a96b-4d96-8e03-e8e9ad55248d
name: bash-delete-specific-history-entry
type: command
executor: bash
data: history -d $_INDEX
output: null
created_at: '2023-04-06T03:56:17.657091+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-delete-specific-history-entry

## Command

```bash
history -d $_INDEX
```

## Description

Deletes a specific entry from the Bash history list by its index number, useful for removing traces of sensitive commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Delete the specified history entry | Built-in |
| $_INDEX | The numeric index of the command to delete (from `history` output) | Yes |

## Examples

### Basic Usage

```bash
history -d 123
```

### Advanced Usage

```bash
history -d 123 && history -w
```

Follow with `-w` to save changes to disk.

## Expected Output

No output. The entry is removed; subsequent `history` shows the updated list with indices shifted.

## Related

- [[procedures/Linux-Command-History-Evasion]]
