---
id: 9a60fabe-931c-453d-bb56-a83e43b9ea98
name: git-cat-file-show-commit
type: command
executor: bash
data: git cat-file -p $_COMMIT_HASH
output: null
created_at: '2023-04-06T03:55:59.982065+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - git
  - inspect
  - commit
verified: true
validated: true
---

# git-cat-file-show-commit

## Command

```bash
git cat-file -p $_COMMIT_HASH
```

## Description

Displays the contents of a Git commit object, including author, committer, timestamp, and message, useful for inspecting recovered repository metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COMMIT_HASH | SHA-1 hash of the commit object | Yes |
| -p | Pretty-print the object contents | Yes |

## Examples

### Basic Usage

```bash
git cat-file -p a1b2c3d4e5f6
```

### Advanced Usage

```bash
git cat-file -p HEAD
```

## Expected Output

author Michael <michael@easyctf.com> 1489389105 +0000
committer Michael <michael@easyctf.com> 1489389105 +0000

Initial commit

## Related

- [[procedures/Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]
