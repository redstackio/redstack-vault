---
id: cmd-id-user
data: id
tags:
  - identification
  - user
type: command
output: uid=1000(git) gid=1000(git) groups=1000(git)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.553Z'
verified: false
validated: true
submitted: true
---
# id-user

## Command

```bash
id
```

## Description

Prints the current user and group IDs, confirming execution context as 'git' user post-RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Identity command | Yes |

## Examples

### Basic Usage

```bash
id
```

### Advanced Usage

Specific user: `id git`.

## Expected Output

uid=1000(git) gid=1000(git) groups=1000(git).

## Related

- [[commands/nc-reverse-shell]]
