---
id: cmd-id-privs-4
data: '| id'
tags:
  - privileges
  - verification
type: command
output: uid=0(root) gid=0(root) groups=0(root)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:26.968Z'
verified: false
validated: true
submitted: true
---
# id-check-privs

## Command

```bash
id
```

## Description

Displays the current user ID, group ID, and group memberships to verify execution context and privileges, typically used post-RCE to confirm root access.

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
id -u  # Just UID
```

## Expected Output

uid=0(root) gid=0(root) groups=0(root), confirming root privileges.

## Related

- [[commands/bash-reverse-shell]]
