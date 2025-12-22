---
type: command
executor: bash
data: id
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - privilege-check
verified: true
validated: true
---

# Check-User-ID

## Command

```bash
id
```

## Description

Displays the current user's real and effective user ID (UID), group ID (GID), and supplementary group memberships. Useful for verifying LXD group access before privilege escalation attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs with current user context | Yes |

## Examples

### Basic Usage

```bash
id
```

### With Username

```bash
id otheruser
```

## Expected Output

uid=1000(username) gid=1000(username) groups=1000(username),110(lxd),998(wheel)

This shows UID/GID and groups; look for 'lxd' group (e.g., 110).

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
