---
data: cat /etc/hosts
tags:
  - discovery
type: command
executor: bash
platforms:
  - Linux
id: 1fc5f93b-4ad0-4db5-be1a-b4cfb5fde67c
created_at: '2025-12-11T06:10:32.973Z'
updated_at: '2025-12-11T06:10:32.973Z'
verified: false
validated: true
submitted: true
---
# cat-hosts-file

## Command

```bash
cat /etc/hosts
```

## Description

Displays the contents of /etc/hosts file to confirm server identity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/etc/hosts` | Path to hosts file | Yes |

## Examples

### Basic Usage

```bash
cat /etc/hosts
```

## Expected Output

127.0.0.1 localhost
█████ ████.semrush.net ███
████████ ███████

## Related

- [[procedures/Receive-and-Interact-with-Reverse-Shell]]
