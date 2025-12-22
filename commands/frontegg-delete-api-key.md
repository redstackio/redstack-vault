---
id: cmd-frontegg-delete-001
data: >-
  DELETE /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID>
  HTTP/1.1

  Host: your-frontegg-instance.com

  Authorization: Bearer <ADMIN_TOKEN>
tags:
  - api-delete
  - frontegg
type: command
output: HTTP 204 No Content or similar success for deletion
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.170Z'
verified: false
validated: true
submitted: true
---
# frontegg-delete-api-key

## Command

```http
DELETE /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID> HTTP/1.1
Host: your-frontegg-instance.com
Authorization: Bearer <ADMIN_TOKEN>
```

## Description

Sends a DELETE request to remove a Frontegg API key, typically triggered from Admin UI but intercepted for modification in exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| API_KEY_ID | Unique identifier of the API key to delete | Yes |
| ADMIN_TOKEN | Bearer token from Admin session | Yes |

## Examples

### Basic Usage

```http
DELETE /frontegg/identity/resources/tenants/api-tokens/v1/abc123 HTTP/1.1
Host: app.frontegg.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Advanced Usage

Include custom headers if needed:

```http
DELETE /frontegg/identity/resources/tenants/api-tokens/v1/abc123 HTTP/1.1
Host: app.frontegg.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
User-Agent: Mozilla/5.0...
```

## Expected Output

HTTP 204 No Content or 200 OK with deletion confirmation; body may be empty.

## Related

- [[commands/frontegg-patch-api-key]]
- [[procedures/Intercept-and-Modify-DELETE-to-PATCH-Request]]
