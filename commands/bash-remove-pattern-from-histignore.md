---
id: d4138cf0-b944-4cd3-b45c-f831fc39aef7
name: bash-remove-pattern-from-histignore
type: command
executor: bash
data: 'HISTIGNORE=${HISTIGNORE%%:$_PATTERN*} && export HISTIGNORE'
output: null
created_at: '2023-04-06T03:56:17.656886+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-remove-pattern-from-histignore

## Command

```bash
HISTIGNORE=${HISTIGNORE%%:$_PATTERN*} && export HISTIGNORE
```

## Description

Removes a specific pattern from the HISTIGNORE list to allow logging of previously ignored commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ${HISTIGNORE%%:$_PATTERN*} | String manipulation to strip the pattern | Built-in |
| $_PATTERN | The pattern to remove (e.g., ls -l) | Yes |
| export | Makes the updated variable available | Built-in |

## Examples

### Basic Usage

```bash
HISTIGNORE=${HISTIGNORE%%:"ls -l"*} && export HISTIGNORE
```

### Advanced Usage

Echo first: `echo $HISTIGNORE` to check before removal.

## Expected Output

No direct output from the command; use `echo $HISTIGNORE` to see updated list without the pattern.

## Related

- [[procedures/Linux-Command-History-Evasion]]
