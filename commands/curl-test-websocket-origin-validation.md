---
type: command
executor: bash
data: >-
  curl --include --no-buffer --header "Connection: Upgrade" --header "Upgrade:
  websocket" --header "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==" --header
  "Sec-WebSocket-Version: 13" --header "Sec-WebSocket-Protocol: chat" --header
  "Origin: http://evil.attacker.com" http://localhost:8080/
tags:
  - websocket
  - recon
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# curl-test-websocket-origin-validation

## Command

```bash
curl --include --no-buffer --header "Connection: Upgrade" --header "Upgrade: websocket" --header "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==" --header "Sec-WebSocket-Version: 13" --header "Sec-WebSocket-Protocol: chat" --header "Origin: http://evil.attacker.com" http://localhost:8080/
```

## Description

This command performs a WebSocket handshake upgrade request to test if the server validates the Origin header and Sec-WebSocket-Protocol. It simulates a cross-site request to identify CSWSH vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--include` or `-i` | Include response headers in output | Yes |
| `--no-buffer` or `-N` | Disable buffering for real-time output | Yes |
| `--header` or `-H` | Add custom headers (Connection, Upgrade, Sec-WebSocket-Key, etc.) | Yes |
| `http://localhost:8080/` | Target WebSocket endpoint URL (replace with actual) | Yes |
| `Origin: http://evil.attacker.com` | Fake cross-origin Origin to test validation | Yes |
| `Sec-WebSocket-Protocol: chat` | Test subprotocol (adjust to target's if known) | No |

## Examples

### Basic Usage

```bash
curl --include --no-buffer --header "Connection: Upgrade" --header "Upgrade: websocket" --header "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==" --header "Sec-WebSocket-Version: 13" --header "Origin: http://evil.attacker.com" http://target.com/ws
```

### Advanced Usage

Add Sec-WebSocket-Protocol for subprotocol test:

```bash
curl --include --no-buffer --header "Connection: Upgrade" --header "Upgrade: websocket" --header "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==" --header "Sec-WebSocket-Version: 13" --header "Sec-WebSocket-Protocol: custom" --header "Origin: http://evil.attacker.com" http://target.com/ws
```

## Expected Output

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: chat
Date: Wed, 06 Apr 2023 03:56:41 GMT
```

Success: 101 status indicates accepted handshake despite cross-origin Origin. Failure (e.g., 400 Bad Request) means validation is in place.

## Related

- [[procedures/Perform-Cross-Site-WebSocket-Hijacking]]
