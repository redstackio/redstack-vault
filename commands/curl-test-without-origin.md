---
data: >-
  curl -X POST https://api.tiktok.com/webcast/endpoint -H "Cookie:
  session=valid_session" -d "data=test_payload"
tags:
  - bypass
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.591Z'
id: c768dc6a-19a0-45b3-bace-715a146356b1
verified: false
validated: true
submitted: true
---
# curl-test-without-origin

## Command

```bash
curl -X POST https://api.tiktok.com/webcast/endpoint -H "Cookie: session=valid_session" -d "data=test_payload"
```

## Description

Tests TikTok Webcast API by sending a request without Origin header to check for CSRF bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Cookie: ..."` | Authentication | Yes |
| `-d "data=..."` | Payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.tiktok.com/webcast/endpoint -H "Cookie: session=valid_session" -d "data=test_payload"
```

### Advanced Usage

```bash
curl -X POST https://api.tiktok.com/webcast/endpoint -H "Cookie: session=valid_session" -d '{"test":"bypass"}'
```

## Expected Output

Successful response (e.g., 200 OK) without CSRF rejection.

## Related

- [[commands/curl-test-with-origin]]
