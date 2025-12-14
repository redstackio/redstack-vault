---
id: cmd-uuid-7
data: git add wiki
tags:
  - git
  - stage
type: command
output: ''
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.314Z'
verified: false
validated: true
submitted: true
---
---

# git-add-submodule

## Command

```bash
git add wiki
```

## Description

Stages the submodule directory and .gitmodules for commit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `wiki` | Submodule path | Yes |

## Examples

### Basic Usage

```bash
git add wiki
```

### Advanced Usage

```bash
git add .gitmodules
```

## Expected Output

Submodule staged.

## Related

- [[commands/git-commit-message]]
- [[procedures/Add-Wiki-as-Relative-Git-Submodule]]
