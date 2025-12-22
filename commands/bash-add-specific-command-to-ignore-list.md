---
id: d4740836-06ca-418f-b0fd-5b57fc944861
name: bash-add-specific-command-to-ignore-list
type: command
executor: bash
data: 'export HISTIGNORE="$HISTIGNORE:$_PATTERN"'
output: null
created_at: '2023-04-06T03:56:17.656832+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-add-specific-command-to-ignore-list

## Command

```bash
export HISTIGNORE="$HISTIGNORE:$_PATTERN"
```

## Description

Appends a new pattern to the HISTIGNORE variable, preventing matching commands from being saved to history.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| export HISTIGNORE | Updates the ignore list | Built-in |
| $_PATTERN | The command pattern to ignore (e.g., ls -l) | Yes |

## Examples

### Basic Usage

```bash
export HISTIGNORE="$HISTIGNORE:ls -l"
```

### Advanced Usage

```bash
export HISTIGNORE="$HISTIGNORE:cat /etc/*"
```

For sensitive file reads.

## Expected Output

No output. Verify by executing the pattern; it won't log.

## Related

- [[procedures/Linux-Command-History-Evasion]]
