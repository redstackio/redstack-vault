---
data: >-
  curl -x 127.0.0.1:8080 -X POST https://example.mil/Login.aspx -d
  "txtUserName=victim@example.com&txtPassword=random123&btnLogin=Login" -v -c
  cookies.txt
tags:
  - web
  - intercept
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.206Z'
id: 79a8f1bf-2775-4d65-a92b-f5e58e8f64d3
verified: false
validated: true
submitted: true
---
# curl-simulate-login

## Command

```bash
curl -x 127.0.0.1:8080 -X POST https://example.mil/Login.aspx -d "txtUserName=victim@example.com&txtPassword=random123&btnLogin=Login" -v -c cookies.txt
```

## Description

Simulates a login attempt through a proxy (e.g., Burp) to intercept and extract ASP.NET state tokens from the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-x 127.0.0.1:8080` | Proxy for interception | Yes |
| `-d "..."` | Form data with credentials | Yes |
| `-v` | Verbose output for debugging | Yes |

## Examples

### Basic Usage

```bash
curl -x 127.0.0.1:8080 -X POST https://example.mil/Login.aspx -d "txtUserName=victim@example.com&txtPassword=random123&btnLogin=Login" -v
```

### Advanced Usage

```bash
curl -x 127.0.0.1:8080 -X POST https://example.mil/Login.aspx -d "..." -v -o response.html
```

## Expected Output

Failed login response (302 or 200) with HTML containing __VIEWSTATE in the body.

## Related

- [[Related Procedure]]
