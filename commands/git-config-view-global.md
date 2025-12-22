---
type: command
executor: bash
data: git config --global --list
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - config
verified: true
validated: true
---

# git-config-view-global

## Command

```bash
git config --global --list
```

## Description

Displays all global Git configuration settings from ~/.gitconfig, useful for inspecting before modifications in persistence setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | Apply to user-wide config | Yes |
| `--list` | Output key-value pairs | Yes |

## Examples

### Basic Usage

```bash
git config --global --list
```

## Expected Output

```
user.name=John Doe
core.editor=vim
core.pager=less
```

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
