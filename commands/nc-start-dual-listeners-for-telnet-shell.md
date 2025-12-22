---
id: c2bc137f-c411-442c-b347-c2b99e4ce5f8
name: nc-start-dual-listeners-for-telnet-shell
type: command
executor: bash
data: |-
  nc -lvp 8080
  nc -lvp 8081
output: null
created_at: '2023-04-06T03:56:24.592489+00:00'
updated_at: '2023-04-10T20:25:31.686351+00:00'
platforms:
  - Linux
  - Unix
tags:
  - c2
  - listener
  - netcat
verified: true
validated: true
---

# nc-start-dual-listeners-for-telnet-shell

## Command

```bash
nc -lvp 8080
nc -lvp 8081
```

## Description

This command starts two Netcat listeners on the attacker's machine for handling a Telnet-based reverse shell. Run each in a separate terminal to capture input and output streams separately.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode for incoming connections | Yes |
| -v | Verbose output to show connection details | Yes |
| -p 8080 | Port for first listener (input stream) | Yes |
| -p 8081 | Port for second listener (output stream) | Yes |

## Examples

### Basic Usage

```bash
nc -lvp 8080
```

### Advanced Usage

Run in two terminals:
```bash
# Terminal 1
nc -lvp 8080
# Terminal 2
nc -lvp 8081
```

## Expected Output

Listening on [0.0.0.0] (family 0, port 8080)
Connection from [victim_ip] 12345 received!

(Interactive shell prompt appears after victim connects.)

## Related

- [[procedures/Telnet-Reverse-Shell]]
- [[commands/telnet-pipe-shell-to-attacker]]
