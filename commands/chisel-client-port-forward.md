---
type: command
executor: cmd
data: >-
  .\chisel.exe client $_SERVER_IP:8008
  R:$_REMOTE_PORT1:$_LOCALHOST1:$_LOCAL_PORT1
  R:$_REMOTE_PORT2:$_LOCALHOST2:$_LOCAL_PORT2
tags:
  - client
  - port-forward
  - chisel
platforms:
  - Windows
verified: true
validated: true
---

# chisel-client-port-forward

## Command

```cmd
.\chisel.exe client $_SERVER_IP:8008 R:$_REMOTE_PORT1:$_LOCALHOST1:$_LOCAL_PORT1 R:$_REMOTE_PORT2:$_LOCALHOST2:$_LOCAL_PORT2
```

## Description

Connects the Chisel client to the server and sets up reverse port forwards for specified remote ports to local destinations on the server side, useful for accessing internal services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `client` | Mode to run as client | Yes |
| `$_SERVER_IP:8008` | Server address and port | Yes |
| `R:$_REMOTE_PORT1:$_LOCALHOST1:$_LOCAL_PORT1` | Reverse forward: remote port to local host:port | Yes |
| `R:$_REMOTE_PORT2:$_LOCALHOST2:$_LOCAL_PORT2` | Additional reverse forward | No |
| `.\chisel.exe` | Path to Windows binary | Yes |

## Examples

### Basic Usage

```cmd
.\chisel.exe client 192.168.1.100:8008 R:88:127.0.0.1:88
```

### Advanced Usage

Forward multiple ports: `.\chisel.exe client 192.168.1.100:8008 R:88:127.0.0.1:88 R:389:localhost:389`.

## Expected Output

Connection success: "88: connected to 127.0.0.1:88" and tunnel status updates.

## Related

- [[procedures/chisel-port-forwarding-and-socks-proxy-network-pivoting]]
- [[tools/Chisel]]
