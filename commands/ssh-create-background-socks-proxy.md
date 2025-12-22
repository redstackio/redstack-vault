---
type: command
executor: bash
data: ssh -N -f -D 9000 $_USER@$_TARGET_HOST
tags:
  - ssh
  - tunneling
  - background
  - proxy
platforms:
  - Linux
  - macOS
  - Unix
verified: true
validated: true
---

# ssh-create-background-socks-proxy

## Command

```bash
ssh -N -f -D 9000 $_USER@$_TARGET_HOST
```

## Description

This command creates a persistent SOCKS proxy tunnel in the background via SSH, without opening an interactive shell. It allows continuous traffic forwarding for pivoting while keeping the terminal free for other tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -N | Do not execute a remote command (keeps tunnel open) | Yes |
| -f | Run SSH in background after authentication | Yes |
| -D 9000 | Bind dynamic SOCKS proxy to local port 9000 | Yes |
| $_USER | SSH username for target authentication | Yes |
| $_TARGET_HOST | Target SSH server IP or hostname | Yes |

## Examples

### Basic Usage

```bash
ssh -N -f -D 9000 user@10.0.0.50
```

### Advanced Usage

```bash
ssh -N -f -D 9000 -i ~/.ssh/id_rsa user@internal-host
```

## Expected Output

Minimal output; returns to shell prompt after backgrounding. Verify with 'netstat -tuln | grep 9000' showing TCP listener on 9000. PID is output if verbose logging is enabled.

## Related

- [[procedures/SSH-Tunneling-for-SOCKS-Proxy]]
- [[commands/ssh-create-dynamic-port-forwarding]]
