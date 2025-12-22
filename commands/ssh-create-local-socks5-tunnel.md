---
id: e1683693-f1ed-44a6-8c04-13379677a602
name: ssh-create-local-socks5-tunnel
type: command
executor: bash
data: 'ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@$_VPS_IP'
output: null
created_at: '2023-04-06T03:56:22.549983+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssh
  - tunnel
  - socks5
verified: true
validated: true
---

# ssh-create-local-socks5-tunnel

## Command

```bash
ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@$_VPS_IP
```

## Description

This command creates a background SSH tunnel that forwards local port 1080 to the remote host's localhost:1080, establishing a SOCKS5 proxy endpoint for traffic pivoting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Run in background | Yes |
| -N | No remote command execution | Yes |
| -T | Disable pseudo-terminal | Yes |
| -i /tmp/id_rsa | Path to private SSH key | Yes |
| -L 1080:127.0.0.1:1080 | Local forward: local_port:remote_host:remote_port | Yes |
| root@$_VPS_IP | Remote user@host (VPS IP) | Yes |

## Examples

### Basic Usage

```bash
ssh -fNT -i /tmp/id_rsa -L 1080:127.0.0.1:1080 root@192.168.1.100
```

### Advanced Usage

```bash
ssh -fNT -i ~/.ssh/mykey -L 1080:127.0.0.1:1080 -o ServerAliveInterval=60 root@$_VPS_IP
```

## Expected Output

No output on success (silent background process). Errors: "Permission denied" for bad key, "Connection refused" for unreachable host. Verify with `netstat -tuln | grep 1080` showing LISTEN on localhost:1080.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/OpenSSH]]
