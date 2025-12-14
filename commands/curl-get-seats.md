---
data: 'curl -X GET https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN"'
tags:
  - api
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7ca57e06-2445-4d8f-9f47-c7716f7fdcf2
created_at: '2025-12-14T17:24:22.260Z'
updated_at: '2025-12-14T17:24:22.260Z'
verified: false
validated: true
submitted: true
---
# curl-get-seats

## Command

```bash
curl -X GET https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN"
```

## Description

This command retrieves the current seat configuration from the Krisp API /v2/seats endpoint, useful for baseline assessment before exploiting race conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Provides the API authentication token | Yes |

## Examples

### Basic Usage

```bash
TOKEN="your_token"
curl -X GET https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN"
```

### Advanced Usage

```bash
# Pipe to jq for parsing
curl -X GET https://api.krisp.ai/v2/seats -H "Authorization: Bearer $TOKEN" | jq '.max_seats'
```

## Expected Output

HTTP 200 OK response with JSON, e.g., {"max_seats": 5, "assigned": 3, "available": 2}.

## Related

- [[Related Procedure: Exploit TOCTOU Race Condition on Krisp Seats Endpoint]]
