---
id: cmd-uuid-1
name: curl-inspect-token
type: command
executor: bash
data: >-
  curl -X POST https://liberapay.com/login -d "username=user&password=pass" -c
  cookies.txt -D headers.txt -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.827Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web-testing
  - csrf
verified: false
validated: true
submitted: true
---

# curl-inspect-token

## Command

```bash
curl -X POST https://liberapay.com/login -d "username=user&password=pass" -c cookies.txt -D headers.txt -v
```

## Description

This command performs a login request to a web application, saves session cookies, dumps response headers to a file, and enables verbose output to inspect CSRF tokens in transit. Use it during authentication testing to capture token values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data payload for login form | Yes |
| `-c cookies.txt` | Save cookies to file | Yes |
| `-D headers.txt` | Dump headers to file | Yes |
| `-v` | Verbose mode for detailed output | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/login -d "username=user&password=pass" -c cookies.txt -D headers.txt -v
```

### Advanced Usage

```bash
curl -X POST https://liberapay.com/login -d "username=user&password=pass&csrf_token=abc123" -b cookies.txt -c cookies.txt -D headers.txt -v
```

## Expected Output

Verbose logs showing request/response details, including headers with potential CSRF tokens (e.g., X-CSRF-Token: somevalue). Cookies saved in cookies.txt, headers in headers.txt. Successful login returns HTTP 200 or 302 redirect.

## Related

- [[Related Procedure: Test-Login-Logout-Cycles]]
