---
id: 612828b7-9d17-4422-a3e4-a799338c4d83
name: curl-perform-login
type: command
executor: bash
data: >-
  curl -c cookies.txt -d "username=$_USERNAME&password=$_PASSWORD" -X POST
  https://$_TARGET_URL/login
output: null
created_at: '2023-04-06T03:55:53.954047+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web
  - authentication
verified: true
validated: true
---

# curl-perform-login

## Command

```bash
curl -c cookies.txt -d "username=$_USERNAME&password=$_PASSWORD" -X POST https://$_TARGET_URL/login
```

## Description

This command performs a login request to a web application's authentication endpoint using curl, capturing the resulting session cookie in a file. It is used to establish an authenticated session prior to attempting 2FA bypass techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username for login | Yes |
| $_PASSWORD | Target password for login | Yes |
| $_TARGET_URL | Base URL of the application (e.g., target.com) | Yes |
| -c cookies.txt | Save cookies to file | Yes |
| -d | POST data payload | Yes |
| -X POST | Specify POST method | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -d "username=admin&password=secret" -X POST https://example.com/login
```

### Advanced Usage

```bash
curl -c cookies.txt -d "username=admin&password=secret&csrf_token=$_CSRF" -X POST -H "Content-Type: application/x-www-form-urlencoded" https://example.com/login
```

## Expected Output

A HTTP response indicating successful login, such as:

```
< HTTP/1.1 302 Found
< Location: https://example.com/2fa/verify
< Set-Cookie: sessionid=abc123; Path=/
```

The cookies.txt file will contain the session cookie for subsequent requests.

## Related

- [[procedures/Bypass-2FA-via-Force-Browsing]]
