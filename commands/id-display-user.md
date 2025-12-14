---
id: cmd-uuid-2
data: id
tags:
  - recon
  - user-enum
type: command
output: uid=500(git) gid=500(git) groups=500(git)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.925Z'
verified: false
validated: true
submitted: true
---
# id-display-user

## Command

```bash
id
```

## Description

Displays the current user ID, group ID, and groups, used in reverse shell to confirm execution context as 'git' user in GitLab RCE.

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

uid=500(git) gid=500(git) groups=500(git)

## Related

- [[commands/hostname-show-aliases]]
- [[procedures/Verify-RCE-Impact-with-File-Write-or-Reverse-Shell]]
