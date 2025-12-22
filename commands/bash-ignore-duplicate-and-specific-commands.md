---
id: e123923c-37b7-44b4-9b8e-c55cc6a7d29d
name: bash-ignore-duplicate-and-specific-commands
type: command
executor: bash
data: 'export HISTIGNORE="&:$_PATTERNS"'
output: null
created_at: '2023-04-06T03:56:17.656595+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - evasion
  - history
verified: true
validated: true
---

# bash-ignore-duplicate-and-specific-commands

## Command

```bash
export HISTIGNORE="&:$_PATTERNS"
```

## Description

Configures Bash to ignore duplicate commands ('&') and specific patterns from being added to history, reducing logged noise and hiding common or sensitive commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| export HISTIGNORE | Sets the variable for ignored patterns | Built-in |
| $_PATTERNS | Colon-separated patterns (e.g., ls:ll:cd:exit) | Yes |

## Examples

### Basic Usage

```bash
export HISTIGNORE="&:ls:ll:cd:exit"
```

### Advanced Usage

```bash
export HISTIGNORE="&:ls*:cd*:pwd:exit"
```

Use wildcards for broader matching.

## Expected Output

No output. Test by running ignored commands; they won't appear in `history`.

## Related

- [[procedures/Linux-Command-History-Evasion]]
