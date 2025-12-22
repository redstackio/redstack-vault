---
data: >-
  curl -X POST https://api.tiktok.com/webcast/endpoint -H "Origin:
  https://www.tiktok.com" -H "Cookie: session=valid_session" -d
  "data=test_payload"
tags:
  - test
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.593Z'
id: 5a6866f4-4fbf-4ad3-a28d-0ac81caf5d3a
verified: false
validated: true
submitted: true
---
# curl-test-with-origin

## Command

```bash
curl -X POST https://api.tiktok.com/webcast/endpoint -H "Origin: https://www.tiktok.com" -H "Cookie: session=valid_session" -d "data=test_payload"
```

## Description

Sends a POST request to TikTok Webcast API with Origin header to test standard CSRF validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Origin: ..."` | Sets Origin header | Yes |
| `-H "Cookie: ..."` | Authentication cookie | Yes |
| `-d "data=..."` | Request payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.tiktok.com/webcast/endpoint -H "Origin: https://www.tiktok.com" -H "Cookie: session=valid_session" -d "data=test_payload"
```

### Advanced Usage

```bash
curl -X POST https://api.tiktok.com/webcast/endpoint -H "Origin: https://www.tiktok.com" -H "Cookie: session=valid_session" -H "Content-Type: application/json" -d '{"key":"value"}'
```

## Expected Output

HTTP 200 OK with JSON response indicating successful processing.

## Related

- [[commands/curl-test-without-origin]]
