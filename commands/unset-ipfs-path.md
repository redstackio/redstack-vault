---
id: e85c36b2-ed05-4395-8f8b-d0f2342d53d1
name: unset-ipfs-path
type: command
executor: bash
data: unset IPFS_PATH
output: No output
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.967Z'
platforms:
  - Linux
tags:
  - cleanup
  - env-var
verified: false
validated: true
submitted: true
---

# unset-ipfs-path

## Command

```bash
unset IPFS_PATH
```

## Description

Removes the IPFS_PATH environment variable after exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IPFS_PATH | Variable to unset | Yes |

## Examples

### Basic Usage

```bash
unset IPFS_PATH
```

## Expected Output

None; variable cleared.

## Related

- [[commands/export-ipfs-path]]
- [[procedures/Cleanup-Exploit-Environment]]
