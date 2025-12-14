---
id: cmd-nc-http-server
data: nc -nlvp 8080
tags:
  - network
  - listener
  - http-server
type: command
output: >-
  listening on [any] 8080 ... connect to [192.168.1.82] from (UNKNOWN)
  [192.168.1.81] 56194 GET /a HTTP/1.1 ... HTTP/1.1 200 OK scode=196206;
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.549Z'
verified: false
validated: true
submitted: true
---
# Netcat-HTTP-Server

## Command

```bash
nc -nlvp 8080
```

## Description

This command starts netcat in listen mode to create a basic TCP/HTTP server, used here to handle callbacks from the victim's browser and serve the SMS code response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Do not resolve DNS names | Yes |
| `-l` | Listen mode for incoming connections | Yes |
| `-v` | Verbose output | Yes |
| `-p 8080` | Specify port 8080 | Yes |

## Examples

### Basic Usage

```bash
nc -nlvp 8080
```

### Advanced Usage

For specific IP binding:
```bash
nc -nlvp 0.0.0.0 8080
```

## Expected Output

listening on [any] 8080 ...
connect to [192.168.1.82] from (UNKNOWN) [victim-ip] 56194
GET /a HTTP/1.1
Host: 192.168.1.82:8080
...
(Then manually type response: HTTP/1.1 200 OK\r\n\r\nscode=196206; )

## Related

- [[Related Procedure|procedures/Receive-and-Relay-SMS-Verification-Code]]
