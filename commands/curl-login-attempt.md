---
id: cmd-uuid-002
data: >-
  curl -X POST http://target.com/admin/login -d "username=admin&password=admin"
  -c cookies.txt -v
tags:
  - auth
  - http-post
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.398Z'
verified: false
validated: true
submitted: true
---
# curl-login-attempt

## Command

```bash
curl -X POST http://target.com/admin/login -d "username=admin&password=admin" -c cookies.txt -v
```

## Description

Attempts login to a web form using POST data with default credentials, saving session cookies for further use in authenticated requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Use POST method | Yes |
| `-d` | Form data (username/password) | Yes |
| `-c cookies.txt` | Save cookies to file | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/login -d "user=admin&pass=admin" -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST -d "username=admin&password=admin" --data-urlencode http://target.com/admin/login -c cookies.txt -v
```

## Expected Output

Verbose logs showing request/response, including 302 redirect and Set-Cookie headers if successful.

## Related

- [[Related Procedure: Attempt-Login-with-Default-Credentials]]
