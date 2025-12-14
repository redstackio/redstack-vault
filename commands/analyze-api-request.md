---
id: cmd-3371448-analyze-request
data: >-
  echo 'POST
  https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable
  Headers: Authorization: Bearer <ADMIN_JWT>, Content-Type: application/json
  Body: {"approval_preference":"disable"}'
tags:
  - api-analysis
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.412Z'
verified: false
validated: true
submitted: true
---
# analyze-api-request

## Command

```bash
echo 'POST https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable' \
  'Headers: Authorization: Bearer <ADMIN_JWT>, Content-Type: application/json' \
  'Body: {"approval_preference":"disable"}'
```

## Description

Simple echo command to format and review captured API request details for analysis before modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<WORKSPACE_ID>` | Workspace ID from capture | Yes |
| `<ADMIN_JWT>` | Token from intercepted request | Yes |

## Examples

### Basic Usage

```bash
echo 'POST https://lovable-api.com/workspaces/123/tool-preferences/ai_gateway/enable Headers: Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```

### Advanced Usage

Pipe to file for further editing:

```bash
echo '...' > request.txt
```

## Expected Output

Printed request structure for manual review.

## Related

- [[commands/modify-jwt-request]]
- [[procedures/Capture-and-Replay-API-Request]]
