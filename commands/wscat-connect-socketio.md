---
data: 'wscat -c ws://target-host:3000/socket.io/?EIO=4&transport=websocket'
tags:
  - websocket
  - socketio
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.827Z'
id: 0fb9ef44-3fb8-4e28-9cd5-239d2367a73d
verified: false
validated: true
submitted: true
---
# wscat-connect-socketio

## Command

```bash
wscat -c ws://target-host:3000/socket.io/?EIO=4&transport=websocket
```

## Description

This command uses wscat to establish a WebSocket connection to a Socket.IO endpoint, simulating a client connection for testing or exploitation purposes in web applications like Hyperledger Cactus.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Connection URL (ws:// or wss://) | Yes |
| `target-host` | Hostname or IP of the target | Yes |
| `3000` | Port number (default for many Node.js apps) | No |
| `EIO=4` | Engine.IO protocol version | No |
| `transport=websocket` | Force WebSocket transport | No |

## Examples

### Basic Usage

```bash
wscat -c ws://example.com:3000/socket.io/?EIO=4&transport=websocket
```

### Advanced Usage

```bash
wscat -c wss://secure-target.com:443/socket.io/?EIO=4&transport=websocket --no-check
```

## Expected Output

Connection established with server response like '40' or '0{"sid":"abc123"}', indicating successful handshake. Interactive mode allows sending messages.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-SocketIO-Handling]]
