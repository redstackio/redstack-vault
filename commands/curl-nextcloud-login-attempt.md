---
data: >-
  curl -X POST 'https://nextcloud.example.com/login.php' -d 'user=username' -d
  'password=knownpassword' -c cookies.txt
tags:
  - brute-force
  - web
  - authentication
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:47.810Z'
id: 55ec5666-30bc-45f9-8cca-f939c8ad564d
verified: false
validated: true
submitted: true
---
# curl-nextcloud-login-attempt

## Command

```bash
curl -X POST 'https://nextcloud.example.com/login.php' -d 'user=username' -d 'password=knownpassword' -c cookies.txt
```

## Description

This command sends a POST request to Nextcloud's login endpoint to authenticate with username and password, storing session cookies for subsequent TOTP attempts. It is used in brute force scenarios to initiate the 2FA challenge.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://nextcloud.example.com/login.php'` | Target login URL | Yes |
| `-d 'user=username'` | Username form field | Yes |
| `-d 'password=knownpassword'` | Password form field | Yes |
| `-c cookies.txt` | Save cookies to file for session persistence | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://nextcloud.example.com/login.php' -d 'user=admin' -d 'password=pass123' -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST 'https://nextcloud.example.com/login.php' -d 'user=admin' -d 'password=pass123' -c cookies.txt -H 'User-Agent: Mozilla/5.0' --max-time 10
```

## Expected Output

HTTP 200 response with HTML containing the TOTP challenge form, or a redirect header. Cookies file populated with session data. No errors if credentials are valid.

## Related

- [[procedures/Brute-Force-Nextcloud-TOTP-2FA]]
