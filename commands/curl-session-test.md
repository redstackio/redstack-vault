---
id: cmd-curl-session-001
data: >-
  curl -c cookies.txt -d "email=user@example.com&password=pass" -X POST
  https://www.udemy.com/login/
tags:
  - web-testing
  - session-management
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.111Z'
verified: false
validated: true
submitted: true
---
# curl-session-test

## Command

```bash
curl -c cookies.txt -d "email=user@example.com&password=pass" -X POST https://www.udemy.com/login/
```

## Description

This command uses curl to perform an HTTP login request to a web application like Udemy, saving session cookies to a file for later reuse in testing authentication persistence. It is useful for simulating login and capturing auth tokens during vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Save cookies to the specified file | Yes |
| `-d "email=...&password=..."` | POST data for login form | Yes |
| `-X POST` | Specify HTTP method as POST | Yes |
| `https://www.udemy.com/login/` | Target login endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -d "email=user@example.com&password=pass" -X POST https://www.udemy.com/login/
```

### Advanced Usage

```bash
curl -c cookies.txt -d "email=user@example.com&password=pass" -H "User-Agent: Mozilla/5.0" -X POST https://www.udemy.com/login/
```

## Expected Output

HTTP response with status 200 or 302 (redirect on success), and cookies.txt file populated with session tokens like 'access_token' or 'session_id'.

## Related

- [[Related Procedure|procedures/Exploit-Persistent-Authentication-Tokens-After-Logout]]
