---
id: cmd-3371448-admin-toggle
data: >-
  curl -X POST
  https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable
  -H "Authorization: Bearer <ADMIN_JWT>" -H "Content-Type: application/json" -d
  '{"approval_preference":"disable"}'
tags:
  - api-test
  - authorization
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
updated_at: '2025-12-14T17:30:07.416Z'
verified: false
validated: true
submitted: true
---
# admin-toggle-ai-capture

## Command

```bash
curl -X POST https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Description

This command sends a POST request to the Lovable AI API to disable the AI gateway feature using an admin JWT token, simulating the UI toggle action for capture and analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<WORKSPACE_ID>` | The ID of the target workspace | Yes |
| `<ADMIN_JWT>` | Valid admin JWT token | Yes |
| `--data` or `-d` | JSON payload for preference update | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://lovable-api.com/workspaces/123/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://lovable-api.com/workspaces/123/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

## Expected Output

HTTP 200 OK with JSON response like {"success": true, "preferences": {"ai_gateway": "disabled"}}, indicating the feature is toggled off.

## Related

- [[commands/replay-editor-toggle]]
- [[procedures/Access-Admin-Endpoint-as-Editor]]
