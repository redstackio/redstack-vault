---
id: 469aadb0-caa4-4946-b3c1-8f799bf02567
name: bash-print-user-id
type: command
executor: bash
data: id
output: null
created_at: '2023-04-06T03:55:58.577426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - privilege-check
verified: true
validated: true
---

# bash-print-user-id

## Command

```bash
id
```

## Description

This command prints the current user ID (UID), group ID (GID), and effective user/group IDs for the process, providing quick insight into the current user's privileges and context on a Linux system. It is commonly used in post-exploitation to verify if the shell is running as root, a service account like www-data, or another user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs with current user context | No |

## Examples

### Basic Usage

```bash
id
```

### With Username (Alternative)

```bash
id username
```

> Displays UID/GID for a specific user instead of current.

## Expected Output

Successful execution outputs something like:

```
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

This indicates the user 'www-data' with matching group, typical for web server processes. If 'uid=0(root)', full privileges are available.

## Related

- [[procedures/LFI-to-RCE-via-SSH-Log-File-Inclusion]]
