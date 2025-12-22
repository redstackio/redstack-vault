---
id: 2d724fca-38b0-4cee-aea8-050ac2846537
name: bash-set-history-size
type: command
executor: bash
data: export HISTSIZE=$_SIZE
output: null
created_at: '2023-04-06T03:56:17.656729+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-set-history-size

## Command

```bash
export HISTSIZE=$_SIZE
```

## Description

Sets the maximum number of commands stored in Bash history, limiting the log size and automatically discarding older entries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| export HISTSIZE | Sets the in-memory history limit | Built-in |
| $_SIZE | Number of commands to retain (e.g., 100) | Yes |

## Examples

### Basic Usage

```bash
export HISTSIZE=100
```

### Advanced Usage

Set to 0 for no history: `export HISTSIZE=0`.

## Expected Output

No output. `history` will respect the new limit as commands accumulate.

## Related

- [[procedures/Linux-Command-History-Evasion]]
