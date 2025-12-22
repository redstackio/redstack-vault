---
id: 251a79be-a2a8-4303-b58f-0dee48b0756f
name: bash-view-history-file
type: command
executor: bash
data: cat ~/.bash_history
output: null
created_at: '2023-04-06T03:56:17.656369+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-view-history-file

## Command

```bash
cat ~/.bash_history
```

## Description

Displays the contents of the persistent Bash history file, showing commands saved across sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cat | Concatenates and displays file contents | Built-in |
| ~/.bash_history | Default history file path | Yes |

## Examples

### Basic Usage

```bash
cat ~/.bash_history
```

### Advanced Usage

```bash
cat ~/.bash_history | less
```

For paginated viewing.

## Expected Output

List of commands, one per line, e.g.,
```
ls -la
whoami
```

## Related

- [[procedures/Linux-Command-History-Evasion]]
