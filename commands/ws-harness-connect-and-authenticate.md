---
type: command
executor: bash
data: python ws-harness.py -u "$_WEBSOCKET_URL" -m $_MESSAGE_FILE
output: null
platforms:
  - Linux
  - macOS
tags:
  - web-sockets
  - authentication
verified: true
validated: true
---

# ws-harness-connect-and-authenticate

## Command

```bash
python ws-harness.py -u "$_WEBSOCKET_URL" -m $_MESSAGE_FILE
```

## Description

This command uses the ws-harness.py script to establish a WebSocket connection to a target authentication endpoint and send a custom message payload from a file. It is used to test and exploit WebSocket-based authentication mechanisms in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_WEBSOCKET_URL | The full WebSocket URL for the authentication endpoint (e.g., ws://dvws.local:8080/authenticate-user) | Yes |
| $_MESSAGE_FILE | Path to the file containing the JSON authentication payload (e.g., ./message.txt) | Yes |
| -u | Specifies the WebSocket URL | Built-in |
| -m | Specifies the message file path | Built-in |

## Examples

### Basic Usage

```bash
python ws-harness.py -u "ws://dvws.local:8080/authenticate-user" -m ./message.txt
```

### Advanced Usage

```bash
python ws-harness.py -u "wss://secure-target.com/ws/auth" -m ./fuzz-message.txt
```

## Expected Output

Successful connection and payload transmission might produce output like:

Connected to ws://dvws.local:8080/authenticate-user
Message sent: {"auth_user":"dGVzda==", "auth_pass":"password"}
Response: {"status": "authenticated", "token": "abc123"}

If authentication fails: {"status": "failed", "error": "Invalid credentials"}

## Related

- [[procedures/Web-Sockets-Authentication-Exploitation]]
- [[tools/ws-harness]]
