---
id: dd58cf3b-85b8-45e8-a298-af7b0507ae1b
name: git-rev-parse-parent-commit
type: command
executor: bash
data: git rev-parse $_COMMIT_HASH^1
output: null
created_at: '2023-04-06T03:55:59.981998+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - git
  - inspect
  - history
verified: true
validated: true
---

# git-rev-parse-parent-commit

## Command

```bash
git rev-parse $_COMMIT_HASH^1
```

## Description

Resolves the parent commit hash of a given commit in the recovered Git repository, enabling traversal of the commit history.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COMMIT_HASH | SHA-1 hash of the commit | Yes |
| ^1 | Reference to the first parent | Yes |

## Examples

### Basic Usage

```bash
git rev-parse abc123^1
```

### Advanced Usage

```bash
git rev-parse HEAD~1
```

## Expected Output

15ca375e54f056a576905b41a417b413c57df6eb

## Related

- [[procedures/Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]
