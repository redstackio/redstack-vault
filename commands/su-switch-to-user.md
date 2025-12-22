---
type: command
executor: bash
data: su - user
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - post-exploitation
  - privilege-escalation
verified: true
validated: true
---

# su-switch-to-user

## Command

```bash
su - user
```

## Description

This command switches the current user context to the specified 'user' using 'su', loading the target user's environment. It prompts for the user's password and is used in interactive shells to pivot access, such as from a compromised low-privilege account to a higher one.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| - | Load the target user's login environment (home dir, PATH, etc.) | Yes |
| user | The username to switch to (e.g., root, www-data) | Yes |

## Examples

### Basic Usage

```bash
su - root
```

### Advanced Usage

Switch without loading full environment (faster but less complete):

```bash
su root
```

## Expected Output

Password prompt: 'Password: ' (enter target user's password). On success: New prompt like 'root@hostname:~#'. On failure: 'su: Authentication failure'. The environment variables (e.g., $HOME, $USER) update to the target user's.

## Related

- [[procedures/Spawn-TTY-Shell-for-Interactive-Reverse-Shell]]
