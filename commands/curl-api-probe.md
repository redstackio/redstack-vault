---
id: cmd-uuid-1
data: >-
  curl -X GET "https://api.line.me/v2/timeline/hidden_friends" -H "Accept:
  application/json" -v
tags:
  - api-probe
  - recon
type: command
output: null
executor: bash
platforms:
  - Web
  - Mobile API
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.932Z'
verified: false
validated: true
submitted: true
---
# curl-api-probe

## Command

```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends" -H "Accept: application/json" -v
```

## Description

This command probes the LINE Timeline API endpoint to check for access control issues, using verbose mode to inspect headers and responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `"https://api.line.me/v2/timeline/hidden_friends"` | Target endpoint URL | Yes |
| `-H "Accept: application/json"` | Requests JSON response | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=TEST_ID" -H "Accept: application/json" -v
```

## Expected Output

HTTP/1.1 200 OK followed by JSON body like {"status": "ok"}, indicating successful unauthenticated access.

## Related

- [[Related Procedure]]
