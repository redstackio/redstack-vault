---
data: 'curl -X GET https://demo.weblate.org/accounts/logout/ -v'
tags:
  - web
  - test
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.652Z'
id: 79b37cbd-9d5e-4404-abd7-5986a3087422
verified: false
validated: true
submitted: true
---
# curl-test-logout

## Command

```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -v
```

## Description

This command tests the accessibility of the logout endpoint via a simple GET request, checking for CSRF protection absence by observing if the request succeeds without tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://demo.weblate.org/accounts/logout/` | Target logout URL | Yes |
| `-v` | Verbose output for headers and response | No |

## Examples

### Basic Usage

```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -v
```

### Advanced Usage

```bash
curl -X GET https://demo.weblate.org/accounts/logout/ --referer https://attacker.com -v
```

## Expected Output

Verbose logs showing HTTP/1.1 302 Found or similar redirect to login, with no CSRF-related errors, confirming vulnerability.

## Related

- [[Related Procedure: Identify-Logout-Endpoint]]
