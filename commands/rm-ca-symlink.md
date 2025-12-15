---
data: rm -f ca.crt
tags:
  - remove
  - symlink
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.032Z'
id: e8aeb91b-3ed2-4f9a-acb0-2c47e4bcb356
verified: false
validated: true
submitted: true
---
# rm-ca-symlink

## Command

```bash
rm -f ca.crt
```

## Description

Removes the existing ca.crt symlink to prepare for the fake CA link in the race condition.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Force removal without prompt | Yes |

## Examples

### Basic Usage

```bash
rm -f ca.crt
```

### Advanced Usage

```bash
rm -rf ca.crt
```

## Expected Output

File removed if exists; no output.

## Related

- [[commands/ln-symlink-fake-ca]]
