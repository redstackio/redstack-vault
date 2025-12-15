---
data: >-
  curl -X GET https://www.every.org/api/users/bug.hunter3 -H "X-CSRF-Token:
  <captured_token>" -H "Cookie: session=<session_cookie>" -H "User-Agent:
  Mozilla/5.0..."
tags:
  - api
  - get
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:02.039Z'
id: 06944d4c-cf29-4d50-98cc-fad3172b0f1a
verified: false
validated: true
submitted: true
---
# curl-query-private-profile

## Command

```bash
curl -X GET https://www.every.org/api/users/bug.hunter3 \
  -H "X-CSRF-Token: <captured_token>" \
  -H "Cookie: session=<session_cookie>" \
  -H "User-Agent: Mozilla/5.0..."
```

## Description

Queries a user profile API endpoint with preserved auth to access private data; used for information disclosure testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method for retrieval | Yes |
| `https://.../users/<username>` | Target private user path | Yes |
| `-H "X-CSRF-Token: <token>"` | CSRF header | Yes |
| `-H "Cookie: ..."` | Auth cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://www.every.org/api/users/privateuser -H "X-CSRF-Token: abc123" -H "Cookie: session=def456"
```

### Advanced Usage

With output to file: ```bash
curl ... > response.json
```

## Expected Output

JSON: {"data": {"user": {"causes": [...]}}}

## Related

- [[Related Procedure]]
