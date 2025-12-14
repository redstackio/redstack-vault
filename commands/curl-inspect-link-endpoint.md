---
data: >-
  curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer
  YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id":
  "YOUR_LINK_ID", "user_id": "YOUR_USER_ID"}'
tags:
  - web
  - api
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 337cb891-b51c-47f1-848d-63ef3f5d942d
created_at: '2025-12-14T17:30:07.424Z'
updated_at: '2025-12-14T17:30:07.424Z'
verified: false
validated: true
submitted: true
---
# curl-inspect-link-endpoint

## Command

```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id": "YOUR_LINK_ID", "user_id": "YOUR_USER_ID"}'
```

## Description

This command sends a POST request to the okl.lt hide-link endpoint to inspect the API behavior for legitimate requests, helping identify parameters vulnerable to IDOR manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://okl.lt/api/hide-link'` | Target endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header with session token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-d '{"link_id": "YOUR_LINK_ID", "user_id": "YOUR_USER_ID"}'` | JSON data with link and user IDs | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"link_id": "link456", "user_id": "user789"}'
```

### Advanced Usage

Add `-v` for verbose output to see full request/response:

```bash
curl -v -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"link_id": "link456", "user_id": "user789"}'
```

## Expected Output

A JSON response like {"status": "success", "message": "Link hidden"} if successful, or error details for failures.

## Related

- [[Related Procedure]]
