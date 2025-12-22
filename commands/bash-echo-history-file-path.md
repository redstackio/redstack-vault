---
id: e729ffe8-f903-4c86-913e-c4414977a0af
name: bash-echo-history-file-path
type: command
executor: bash
data: echo $HISTFILE
output: null
created_at: '2023-04-06T03:56:17.656253+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-echo-history-file-path

## Command

```bash
echo $HISTFILE
```

## Description

Prints the path to the current Bash history file, allowing inspection or targeting for evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo | Outputs the variable value | Built-in |
| $HISTFILE | Environment variable for history file location | Built-in |

## Examples

### Basic Usage

```bash
echo $HISTFILE
```

### Advanced Usage

If unset, defaults to ~/.bash_history.

## Expected Output

File path, e.g.,
```
/home/user/.bash_history
```

## Related

- [[procedures/Linux-Command-History-Evasion]]
