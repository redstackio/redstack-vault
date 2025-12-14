---
data: >-
  curl -X POST 'https://target.weblate.org/accounts/reset/' -H 'X-CSRFToken:
  your_csrf_token' -d
  'csrfmiddlewaretoken=your_csrf_token&email=user1%2Bhackerone%40example.com'
tags:
  - web
  - password-reset
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.290Z'
id: 6ebcfbf8-dccd-4583-9bee-88c5793f3021
verified: false
validated: true
submitted: true
---
# curl-reset-password-weblate

## Command

```bash
curl -X POST 'https://target.weblate.org/accounts/reset/' \
  -H 'X-CSRFToken: your_csrf_token' \
  -d 'csrfmiddlewaretoken=your_csrf_token&email=user1%2Bhackerone%40example.com'
```

## Description

Initiates a password reset in Weblate by submitting the controlled email, sending the reset link to it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d` | Email in form data | Yes |
| CSRF token | For form submission | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://weblate.example.com/accounts/reset/' -H 'X-CSRFToken: token' -d 'csrfmiddlewaretoken=token&email=controlled@example.com'
```

### Advanced Usage

With cookie if session active:

```bash
curl -X POST 'https://weblate.example.com/accounts/reset/' -H 'Cookie: sessionid=abc' -H 'X-CSRFToken: token' -d 'csrfmiddlewaretoken=token&email=controlled@example.com'
```

## Expected Output

Response: "We've emailed you instructions for setting your password."

## Related

- [[Related Procedure: Initiate-Password-Reset-via-Controlled-Email]]
