---
id: 1383c460-58dc-441b-ab7c-9d43ed0e487c
name: ssh-local-port-forwarding
type: command
executor: bash
data: 'ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP'
output: >-
  No visible output as the process forks to background; verify with 'ps aux |
  grep ssh' or 'ss -tuln | grep :$_ATTACKER_PORT'
created_at: '2019-10-02T01:10:12.259465+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - pivot
  - tunneling
verified: true
validated: true
---

# ssh-local-port-forwarding

## Command

```bash
ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP
```

## Description

This command establishes a local SSH port forward, allowing the attacker to connect to an isolated remote service via an intermediary host. Traffic from the local machine's specified port is tunneled through the SSH connection to the target port on the remote IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Forks the process into the background after authentication | Yes |
| -N | Do not execute a remote command; useful for tunneling only | Yes |
| -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT | Local forward: bind local port to remote host:port via SSH | Yes |
| $_USER@$_TARGET_IP | SSH username and intermediary host IP | Yes |

## Examples

### Basic Usage

```bash
ssh -f -N -L 8001:10.10.10.11:80 root@10.10.10.10
```

### Advanced Usage

```bash
ssh -i /path/to/key -f -N -L 8001:10.10.10.11:80 root@10.10.10.10 -o StrictHostKeyChecking=no
```

## Expected Output

No visible output as the process forks to background; verify with 'ps aux | grep ssh' or 'ss -tuln | grep :$_ATTACKER_PORT' to confirm the tunnel is listening.

## Related

- [[procedures/SSH-Port-Forwarding-with-an-Isolated-Host]]
