---
id: cmd-uuid-6
data: git submodule add ../project.wiki wiki
tags:
  - git
  - submodule
type: command
output: |-
  Cloning into 'wiki'...
  done.
  Submodule 'wiki' (../project.wiki) registered for path 'wiki'
  Submodule path 'wiki' added
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.316Z'
verified: false
validated: true
submitted: true
---
---

# git-submodule-add-relative

## Command

```bash
git submodule add ../project.wiki wiki
```

## Description

Adds a repository as a submodule using a relative path, creating .gitmodules.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `../project.wiki` | Relative path to submodule repo | Yes |
| `wiki` | Local path for submodule | Yes |

## Examples

### Basic Usage

```bash
git submodule add ../project.wiki wiki
```

### Advanced Usage

```bash
git submodule add https://example.com/repo.git path
```

## Expected Output

Submodule registered and .gitmodules updated.

## Related

- [[commands/git-add-submodule]]
- [[procedures/Add-Wiki-as-Relative-Git-Submodule]]
