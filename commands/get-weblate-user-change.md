---
data: >-
  curl -X GET "https://weblate-target.com/admin/weblate_auth/user/5/change/" -H
  "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/"
tags:
  - csrf
  - http
type: command
output: HTML response containing 'csrfmiddlewaretoken' form field
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.238Z'
id: 3340ab83-970a-47b9-90f7-dac2898c16cb
verified: false
validated: true
submitted: true
---
# get-weblate-user-change

## Command

```bash
curl -X GET "https://weblate-target.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/"
```

## Description

Accesses the change form for a specific Weblate user to obtain the CSRF token from the HTML form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| URL with <ID> | User change endpoint, e.g., /user/5/change/ | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |
| `-H "Referer: ..."` | Anti-CSRF header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://weblate.example.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=abc123" -H "Referer: https://weblate.example.com/"
```

### Advanced Usage

```bash
curl -X GET "https://weblate.example.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=abc123" | grep -o "csrfmiddlewaretoken' value='[^']*"
```

## Expected Output

Form HTML including `<input name='csrfmiddlewaretoken' value='token_value'>`.

## Related

- [[Related Procedure]]
