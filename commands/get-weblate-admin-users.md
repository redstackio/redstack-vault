---
data: >-
  curl -X GET "https://weblate-target.com/admin/weblate_auth/user/" -H "Cookie:
  sessionid=your_session" -H "Referer: https://weblate-target.com/"
tags:
  - discovery
  - http
type: command
output: HTML response containing user list with IDs
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.241Z'
id: 3ca3aff0-18b0-420c-bd0a-7c7f26de34c8
verified: false
validated: true
submitted: true
---
# get-weblate-admin-users

## Command

```bash
curl -X GET "https://weblate-target.com/admin/weblate_auth/user/" -H "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/"
```

## Description

Retrieves the list of user records from Weblate's admin interface to identify user IDs, typically used in JavaScript payloads for enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| URL | Target admin endpoint | Yes |
| `-H "Cookie: sessionid=..."` | Authenticated session cookie | Yes |
| `-H "Referer: ..."` | Referer header for CSRF | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://weblate.example.com/admin/weblate_auth/user/" -H "Cookie: sessionid=abc123" -H "Referer: https://weblate.example.com/"
```

### Advanced Usage

```bash
curl -X GET "https://weblate.example.com/admin/weblate_auth/user/?q=username" -H "Cookie: sessionid=abc123" -H "Referer: https://weblate.example.com/" | grep -o 'id="[^"]*"'
```

## Expected Output

HTML table with user entries, e.g., `<td>5</td><td>attacker</td>`, parse for IDs.

## Related

- [[Related Procedure]]
