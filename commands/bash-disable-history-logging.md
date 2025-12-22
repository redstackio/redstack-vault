---
id: 4dde338c-34bb-4d18-99e0-f9df27006e62
name: bash-disable-history-logging
type: command
executor: bash
data: unset HISTFILE && export HISTSIZE=0
output: null
created_at: '2023-04-06T03:56:17.656487+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-disable-history-logging

## Command

```bash
unset HISTFILE && export HISTSIZE=0
```

## Description

Disables Bash history logging by removing the history file reference and setting the in-memory history size to zero, preventing any commands from being recorded in the current session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| unset HISTFILE | Unsets the variable pointing to the history file | Built-in |
| export HISTSIZE=0 | Sets history size to zero, clearing memory | Built-in |

## Examples

### Basic Usage

```bash
unset HISTFILE && export HISTSIZE=0
```

### Advanced Usage

Add to `~/.bashrc` for session persistence: `echo 'unset HISTFILE; export HISTSIZE=0' >> ~/.bashrc`.

## Expected Output

No output. Verify with `history`, which should show no entries.

## Related

- [[procedures/Linux-Command-History-Evasion]]
