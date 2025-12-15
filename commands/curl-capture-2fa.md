---
data: >-
  curl -X POST https://target.com/login/confirm -H "Cookie:
  steamid=your_steamid" -d '{"token":"session_token","code":"123456"}'
tags:
  - http
  - post
  - 2fa
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.340Z'
id: d59497ec-eb22-4b78-8435-cc32fe7878ac
verified: false
validated: true
submitted: true
---
# curl-capture-2fa

## Command

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=your_steamid" -d '{"token":"session_token","code":"123456"}'
```

## Description

Sends a sample POST request to the 2FA confirmation endpoint to capture or simulate the structure, including steamid cookie, for interception and analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H "Cookie: steamid=..."` | Sets the steamid cookie | Yes |
| `-d '{...}'` | JSON body with token and code | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://csmoney.com/login/confirm -H "Cookie: steamid=123456789" -d '{"token":"abc123","code":"654321"}'
```

### Advanced Usage

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=your_id; session=xyz" -H "Content-Type: application/json" -d '{"token":"session_token","code":"invalid"}'
```

## Expected Output

HTTP response with JSON error or success; e.g., {"error":"Invalid code"} for capture validation.

## Related

- [[Related Procedure]]
