---
data: tree
tags:
  - recon
type: command
executor: bash
platforms:
  - Linux
id: bac64957-9367-4160-a745-8e43e389f509
created_at: '2025-12-11T06:10:22.631Z'
updated_at: '2025-12-11T06:10:22.631Z'
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

Displays the directory structure in a tree-like format, used to illustrate the malicious repository setup for the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Default behavior shows current directory | No |

## Examples

### Basic Usage

```bash
tree
```

### Advanced Usage

```bash
tree -L 2
```

## Expected Output

Directory tree showing '--output=/var/opt/gitlab/.ssh/authorized_keys/' with 'id_ed25519.pub' file.

## Related

- [[procedures/Create-Malicious-Repository-Structure]]
