---
data: >-
  curl -X PATCH https://www.every.org/api/me -H "X-CSRF-Token: <captured_token>"
  -H "Cookie: session=<session_cookie>" -H "Content-Type: application/json" -d
  '{"some_field": "updated_value"}'
tags:
  - api
  - patch
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:02.044Z'
id: 98a2bc85-b557-48a5-b724-b4e25e393a7c
verified: false
validated: true
submitted: true
---
# curl-capture-profile-patch

## Command

```bash
curl -X PATCH https://www.every.org/api/me \
  -H "X-CSRF-Token: <captured_token>" \
  -H "Cookie: session=<session_cookie>" \
  -H "Content-Type: application/json" \
  -d '{"some_field": "updated_value"}'
```

## Description

Simulates a profile update PATCH request to capture auth details; primarily used with proxies for interception in web API testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | HTTP method for update | Yes |
| `-H "X-CSRF-Token: <token>"` | CSRF protection header | Yes |
| `-H "Cookie: session=<cookie>"` | Session authentication | Yes |
| `-d '{...}'` | JSON payload for update | Yes |

## Examples

### Basic Usage

```bash
curl -X PATCH https://www.every.org/api/me -H "X-CSRF-Token: abc123" -H "Cookie: session=def456" -H "Content-Type: application/json" -d '{"name": "Test"}'
```

### Advanced Usage

Add verbose output: ```bash
curl -v -X PATCH ... ```

## Expected Output

HTTP 200 with JSON confirmation: {"success": true, "data": {...}}

## Related

- [[Related Procedure]]
