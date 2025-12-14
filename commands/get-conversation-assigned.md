---
data: >-
  GET
  https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid={target-uuid}
tags:
  - discovery
  - api
type: command
output: JSON response with assignment data containing the UUID
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.239Z'
id: 6dd90106-91f3-4cd4-9320-a3f92e1c4541
verified: false
validated: true
submitted: true
---
# get-conversation-assigned

## Command

```bash
# Use curl or browser to trigger/monitor
curl -X GET "https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid={target-uuid}" \
  -H "Cookie: auth={auth-cookie}"
```

## Description

Retrieves conversation assignment data for a specified user UUID, useful for discovering and confirming UUIDs from network traffic during UI interactions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `assignedToUserUuid` | UUID of the target user to query assignments for | Yes |
| `auth-cookie` | Authentication cookie for the requesting user | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid=da4f313f-e21e-4b5f-b2da-42d9864716f6" \
  -H "Cookie: auth=eyJ..."
```

### Advanced Usage

Monitor via proxy for UUID extraction without direct execution.

## Expected Output

JSON array of conversations or empty if none, with the UUID visible in the request URL for copying.

## Related

- [[commands/put-update-preferences]]
- [[procedures/Discover-Target-User-UUID]]
