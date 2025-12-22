---
type: command
executor: bash
data: git config --global core.editor && git config --global core.pager
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - verify
verified: true
validated: true
---

# git-config-verify-editor

## Command

```bash
git config --global core.editor && git config --global core.pager
```

## Description

Retrieves the configured editor and pager to verify backdoor injections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | Global scope | Yes |
| `core.editor` | Editor key | Yes |
| `core.pager` | Pager key | Yes |

## Examples

### Basic Usage

```bash
git config --global core.editor
```

## Expected Output

```
nohup ... & vim
```

## Related

- [[procedures/Backdoor-Git-User-Configurations-for-Persistence]]
