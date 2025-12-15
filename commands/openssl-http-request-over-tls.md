---
data: >-
  printf "GET / HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client
  -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com
  -sess_in session_A.pem
tags:
  - http
  - tls
  - request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.094Z'
id: 97af367b-de9b-4016-9e64-afffca122ee3
verified: false
validated: true
submitted: true
---
# printf "GET / HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem

## Command

```bash
printf "GET / HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem
```

## Description

Sends an HTTP request over a resumed TLS connection, using Host header to target virtual host B.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf` | Constructs HTTP request | Yes |
| `Host:` | Targets virtual host B | Yes |
| `openssl s_client` params | As above for resumption | Yes |

## Examples

### Basic Usage

```bash
printf "GET / HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem
```

### Advanced Usage

```bash
printf "GET /protected HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in session_A.pem
```

## Expected Output

HTTP response from host B, e.g., 200 OK with content.

## Related

- [[Related Procedure]]
