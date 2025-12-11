---
data: tree
tags:
  - recon
  - directory
type: command
executor: bash
platforms:
  - Linux
id: c9990353-5fb4-4fca-8963-fa20c3686ee1
created_at: '2025-12-11T03:47:39.989Z'
updated_at: '2025-12-11T03:47:39.989Z'
verified: false
validated: true
submitted: true
---
# tree-display

## Command

```bash
tree
```

## Description

Displays the directory structure of the repository used in the exploit, illustrating the specially crafted path for verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default displays current directory | No |

## Examples

### Basic Usage

```bash
tree
```

## Expected Output

Directory tree showing '--output=/var/opt/gitlab/.ssh/authorized_keys/' with 'id_ed25519.pub' inside.

## Related

- [[procedures/Create-Malicious-Git-Repository-for-File-Overwrite]]
