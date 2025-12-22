---
id: 12d87123-127d-4774-8db1-4911587be730
name: git-cat-file-show-blob
type: command
executor: bash
data: git cat-file -p $_BLOB_HASH
output: null
created_at: '2023-04-06T03:55:59.982034+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - git
  - inspect
  - file
verified: true
validated: true
---

# git-cat-file-show-blob

## Command

```bash
git cat-file -p $_BLOB_HASH
```

## Description

Displays the raw contents of a Git blob object (file) from the recovered repository, useful for extracting code or configuration data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BLOB_HASH | SHA-1 hash of the blob object | Yes |
| -p | Pretty-print the blob contents | Yes |

## Examples

### Basic Usage

```bash
git cat-file -p def456ghi789
```

### Advanced Usage

```bash
git cat-file -p $(git hash-object config.py)
```

## Expected Output

dbname=production
password=secret123

## Related

- [[procedures/Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]
