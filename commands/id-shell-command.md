---
data: id
tags:
  - shell
  - discovery
type: command
output: uid=1000(prod) gid=1000(prod) groups=1000(prod)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.912Z'
id: 452146dc-1722-4e1a-bef2-848069f4a72b
verified: false
validated: true
submitted: true
---
# id-shell-command

## Command

```bash
id
```

## Description

Displays the current user ID, group ID, and groups for the shell session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
id
```

### Advanced Usage

```bash
id -u
```

## Expected Output

uid=1000(prod) gid=1000(prod) groups=1000(prod)

## Related

- [[Related Procedure: Verify-Access-via-Reverse-Shell]]
