---
type: command
executor: bash
data: ssh -D 8080 $_USER@$_TARGET_HOST
tags:
  - ssh
  - tunneling
  - proxy
platforms:
  - Linux
  - macOS
  - Unix
verified: true
validated: true
---

# ssh-create-dynamic-port-forwarding

## Command

```bash
ssh -D 8080 $_USER@$_TARGET_HOST
```

## Description

This command establishes a basic dynamic SSH port forwarding tunnel, creating a SOCKS proxy on the local machine's port 8080. It forwards application traffic through the encrypted SSH connection to the target host, enabling network pivoting from the attacker's side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -D 8080 | Binds dynamic SOCKS proxy to local port 8080 (change as needed) | Yes |
| $_USER | Username for SSH authentication on target | Yes |
| $_TARGET_HOST | IP address or hostname of the target SSH server | Yes |

## Examples

### Basic Usage

```bash
ssh -D 8080 attacker@192.168.1.100
```

### Advanced Usage

```bash
ssh -D 8080 -i private_key.pem user@target.example.com
```

## Expected Output

The command prompts for password (if not key-based) and connects, dropping to an interactive shell on the target. No explicit proxy output; success is confirmed by SSH connection establishment and subsequent proxy traffic routing (e.g., via curl --socks5).

## Related

- [[procedures/SSH-Tunneling-for-SOCKS-Proxy]]
- [[commands/ssh-create-background-socks-proxy]]
