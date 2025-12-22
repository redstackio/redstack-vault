---
id: 2eda8719-e163-4c6e-9a16-c8ca4e0d71c8
name: bash-display-command-history
type: command
executor: bash
data: history
output: null
created_at: '2023-04-06T03:56:17.656134+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-display-command-history

## Command

```bash
history
```

## Description

Displays the current in-session Bash command history with line numbers for reference and potential deletion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| history | Built-in command to show history | Built-in |

## Examples

### Basic Usage

```bash
history
```

### Advanced Usage

```bash
history 10
```

Show last 10 entries.

## Expected Output

Numbered list, e.g.,
```
   1  ls -la
   2  whoami
```

## Related

- [[procedures/Linux-Command-History-Evasion]]
