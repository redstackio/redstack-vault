---
id: c2e3f4g5-h6i7-8902-efgh-567890123456
data: >-
  curl -c cookies.txt -d 'log=attacker&pwd=weakpass123'
  https://target.com/wp-login.php
tags:
  - wordpress
  - authentication
type: command
output: |-
  HTTP/1.1 302 Found
  Location: https://target.com/wp-admin/
  Set-Cookie: wordpress_logged_in_...=...;
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.292Z'
verified: false
validated: true
submitted: true
---
# wp-login-user

## Command

```bash
curl -c cookies.txt -d 'log=attacker&pwd=weakpass123' https://target.com/wp-login.php
```

## Description

Authenticates a WordPress user and saves session cookies for subsequent API requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Save cookies to file | Yes |
| `-d` | Form data with log (username) and pwd (password) | Yes |
| `https://target.com/wp-login.php` | Login endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -d 'log=user&pwd=pass' https://example.com/wp-login.php
```

### Advanced Usage

```bash
curl -c cookies.txt -d 'log=user&pwd=pass&redirect_to=/wp-admin/' https://example.com/wp-login.php --verbose
```

## Expected Output

302 redirect to dashboard with session cookies set.

## Related

- [[commands/wp-register-user]]
- [[procedures/Exploit-BuddyPress-REST-API-for-Privilege-Escalation]]
