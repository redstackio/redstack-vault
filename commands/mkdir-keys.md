---
id: cmd-8
data: mkdir -p keys
tags:
  - dir
  - setup
type: command
output: Directory created
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.534Z'
verified: false
validated: true
submitted: true
---
# mkdir-keys

## Command

```bash
mkdir -p keys
```

## Description

Creates a directory for storing extracted keys, with -p to avoid errors if exists.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Create parents, no error | Yes |
| `keys` | Directory name | Yes |

## Examples

### Basic Usage

```bash
mkdir -p keys
```

### Advanced Usage

```bash
mkdir -p /tmp/keys
```

## Expected Output

No output if successful.

## Related

- [[commands/gcloud-storage-cat-private-key]]
