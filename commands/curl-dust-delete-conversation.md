---
id: cmd-curl-dust-delete-001
data: >-
  curl -X DELETE
  "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H
  "Authorization: Bearer YOUR_SESSION_TOKEN"
tags:
  - api
  - delete
  - dust-tt
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.878Z'
verified: false
validated: true
submitted: true
---
# curl-dust-delete-conversation

## Command

```bash
curl -X DELETE "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer YOUR_SESSION_TOKEN"
```

## Description

Deletes a conversation via the Dust.tt API without ownership checks, leading to permanent data loss.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | HTTP method for deletion | Yes |
| `URL` | Endpoint with IDs | Yes |
| `-H "Authorization: Bearer TOKEN"` | Auth header | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer TOKEN"
```

### Advanced Usage

With silent output:

```bash
curl -s -X DELETE "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer TOKEN"
```

## Expected Output

Empty response body with HTTP 200 or 204 status indicating success.

## Related

- [[commands/curl-dust-read-conversation]]
- [[procedures/Delete-Unauthorized-Conversation]]
