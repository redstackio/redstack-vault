---
type: command
executor: bash
data: /opt/chisel/chisel server -p 8008 --reverse
tags:
  - server
  - tunneling
  - chisel
platforms:
  - Linux
verified: true
validated: true
---

# chisel-server-reverse-mode

## Command

```bash
/opt/chisel/chisel server -p 8008 --reverse
```

## Description

Starts the Chisel server in reverse mode, listening on the specified port for client connections from behind firewalls. This enables reverse port forwarding where clients push tunnels to the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `server` | Mode to run as server | Yes |
| `-p 8008` | Port to bind the server to | Yes |
| `--reverse` | Enable reverse tunneling support | Yes |
| `/opt/chisel/chisel` | Path to chisel binary | Yes (adjust as needed) |

## Examples

### Basic Usage

```bash
chisel server -p 8008 --reverse
```

### Advanced Usage

Add `--auth username:password` for authentication: `chisel server -p 8008 --reverse --auth user:pass`.

## Expected Output

"Server started listening on 0.0.0.0:8008" followed by client connection logs when tunnels are established.

## Related

- [[procedures/chisel-port-forwarding-and-socks-proxy-network-pivoting]]
- [[tools/Chisel]]
