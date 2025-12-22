---
id: 98fa8e7b-e772-4e5a-b80c-73f39cbbb5ac
name: git-ls-tree-show-directory
type: command
executor: bash
data: git ls-tree -r $_TREE_HASH
output: null
created_at: '2023-04-06T03:55:59.981877+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - git
  - inspect
  - tree
verified: true
validated: true
---

# git-ls-tree-show-directory

## Command

```bash
git ls-tree -r $_TREE_HASH
```

## Description

Lists the contents of a Git tree object recursively, showing files and subdirectories in the recovered repository for structure analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TREE_HASH | SHA-1 hash of the tree object | Yes |
| -r | Recursive listing | Yes |

## Examples

### Basic Usage

```bash
git ls-tree -r abc123def456
```

### Advanced Usage

```bash
git ls-tree -r --name-only HEAD
```

## Expected Output

100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    README.md
100644 blob 5dae937a49acc7c2668f5bcde2a9fd07fc382fe2    config.py

## Related

- [[procedures/Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]
