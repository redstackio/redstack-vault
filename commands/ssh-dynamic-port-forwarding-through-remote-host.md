---
type: command
executor: bash
data: ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
output: null
platforms:
  - Linux
  - Windows
tags:
  - ssh
  - tunnel
  - proxy
verified: true
validated: true
---

# SSH Dynamic Port Forwarding Through a Remote Host

## Command

```bash
ssh -f -N -D $_PORT $_USERNAME@$_TARGET_IP
```

## Description

This command sets up a dynamic SOCKS proxy by forwarding local port traffic through an SSH connection to a remote host, allowing SOCKS-compatible applications to tunnel via the target for pivoting or bypassing restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Local port number for the SOCKS proxy (e.g., 1080 or 9050) | Yes |
| $_USERNAME | Username for SSH authentication | Yes |
| $_TARGET_IP | IP address or hostname of the SSH server | Yes |
| -f | Forks the process into the background after authentication | Built-in |
| -N | Do not execute a remote command | Built-in |
| -D | Enables dynamic (SOCKS) port forwarding | Built-in |

## Examples

### Basic Usage

```bash
ssh -f -N -D 1080 user@192.168.1.100
```

Creates a SOCKS proxy on local port 1080.

### Advanced Usage

```bash
ssh -i /path/to/key -f -N -D 9050 user@target.example.com
```

Uses a private key for authentication and port 9050 for Proxychains compatibility.

## Expected Output

No output if successful; the process backgrounds silently. Use `ps aux | grep ssh` to verify the process is running. Errors include authentication failures or port conflicts.

## Related

- [[procedures/dynamic-port-forwarding-with-ssh-socks-proxy]]
- [[tools/openssh]]
