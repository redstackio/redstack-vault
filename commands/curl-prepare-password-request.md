---
data: 'curl -X GET https://example.mil/Login.aspx -c cookies.txt'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.210Z'
id: aa7ad063-6ea7-49b1-992d-75df03737540
verified: false
validated: true
submitted: true
---
# curl-prepare-password-request

## Command

```bash
curl -X GET https://example.mil/Login.aspx -c cookies.txt
```

## Description

Fetches the ASP.NET login page to inspect form structure and save session cookies, preparing for request templating in password reset attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://example.mil/Login.aspx` | Target login endpoint | Yes |
| `-c cookies.txt` | Saves cookies to file for session persistence | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://example.mil/Login.aspx -c cookies.txt
```

### Advanced Usage

```bash
curl -X GET https://example.mil/Login.aspx -c cookies.txt -o login.html --verbose
```

## Expected Output

HTML response of the login page, including form fields like __VIEWSTATE. Cookies saved to cookies.txt for reuse.

## Related

- [[Related Procedure]]
