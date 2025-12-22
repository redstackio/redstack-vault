---
id: d41f0910-0f17-44da-b7cd-e36498bff1e8
name: tmux-attach-to-session-via-socket
type: command
executor: bash
data: tmux -S $_SOCKET_PATH attach
output: |-
  dj@Cupid:~$ tmux -S /.devs/dev_sess
  root@Cupid:/#
created_at: '2019-11-25T21:35:19.511335+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - tmux
  - session-management
verified: true
validated: true
---

# tmux-attach-to-session-via-socket

## Command

```bash
tmux -S $_SOCKET_PATH attach
```

## Description

This command attaches the current terminal to an existing tmux session using a custom socket path. It is useful in security operations for reconnecting to persistent sessions on remote or compromised systems where the default tmux socket might be restricted or relocated for stealth. The `-S` flag specifies a non-standard socket location, allowing attachment without knowing the session name if only one session exists on that socket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SOCKET_PATH | Full path to the tmux server socket file (e.g., /tmp/tmux-1000/default) | Yes |
| -S | Flag to specify the socket path for the tmux server | Built-in |
| attach | Subcommand to attach to the target session | Built-in |

## Examples

### Basic Usage

Attach to the default session on a custom socket:
```bash
tmux -S /tmp/tmux/sock attach
```

### Advanced Usage

Attach to a specific named session on a custom socket, detaching other clients:
```bash
tmux -S /var/run/tmux attach -t persistent-session -d
```

## Expected Output

Upon successful attachment, the command will switch your terminal to the tmux session, displaying the session prompt without additional output. For example:

```
dj@Cupid:~$ tmux -S /.devs/dev_sess attach
root@Cupid:/# 
```

If no session exists or the socket is invalid, tmux will output an error like "no sessions" or "failed to connect to socket".

## Related

- [[tools/tmux]]
