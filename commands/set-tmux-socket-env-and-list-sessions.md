---
type: command
executor: bash
data: export TMUX=/tmp/tmux-$_UID/default; tmux ls
output: null
platforms:
  - Linux
tags:
  - discovery
  - tmux
  - session-enumeration
verified: true
validated: true
---

# set-tmux-socket-env-and-list-sessions

## Command

```bash
export TMUX=/tmp/tmux-$_UID/default; tmux ls
```

## Description

This command sets the TMUX environment variable to specify a custom socket and lists all active TMUX sessions associated with it. It's used to enumerate sessions for hijacking without attaching, typically after gaining read access to the socket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/tmux-$_UID/default | Path to the TMUX socket; $_UID is the target user's ID | Yes |
| tmux ls | Lists sessions connected to the specified socket | Yes |

## Examples

### Basic Usage

```bash
export TMUX=/tmp/tmux-1000/default; tmux ls
```

### With Error Handling

```bash
export TMUX=/tmp/tmux-1000/default; tmux ls 2>/dev/null || echo "No sessions found"
```

## Expected Output

mysession: 1 windows (created Mon Apr 10 12:00:00 2023) [80x24 term-1]

## Related

- [[procedures/Linux-TMUX-Session-Hijacking]]
- [[commands/tmux-attach-to-session]]
