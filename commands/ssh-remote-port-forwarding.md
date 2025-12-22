---
id: cf3e88ac-955b-43c5-a061-8f464c850ae7
name: ssh-remote-port-forwarding
type: command
executor: bash
data: 'ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP'
output: >-
  No visible output as the process forks to background; verify with 'ps aux |
  grep ssh' or remote logs
created_at: '2019-10-02T01:10:12.258287+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - pivot
  - tunneling
  - reverse
verified: true
validated: true
---

# ssh-remote-port-forwarding

## Command

```bash
ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP
```

## Description

This command sets up a remote SSH port forward, binding a port on the intermediary host to tunnel traffic back to the attacker's specified local port and IP. It enables receiving connections from isolated networks through the intermediary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -f | Forks the process into the background after authentication | Yes |
| -N | Do not execute a remote command; useful for tunneling only | Yes |
| -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT | Remote forward: bind remote port to attacker host:port | Yes |
| $_USER@$_TARGET_IP | SSH username and intermediary host IP | Yes |

## Examples

### Basic Usage

```bash
ssh -f -N -R 4444:127.0.0.1:4444 root@10.10.10.10
```

### Advanced Usage

```bash
ssh -i /path/to/key -f -N -R 4444:192.168.1.100:4444 root@10.10.10.10 -o GatewayPorts=yes
```

## Expected Output

No visible output as the process forks to background; verify with 'ps aux | grep ssh' on the attacker or check SSH logs on the intermediary for the binding.

## Related

- [[procedures/SSH-Port-Forwarding-with-an-Isolated-Host]]
