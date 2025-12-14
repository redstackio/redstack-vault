---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X GET 'https://lark.example.com/api/v1/autoreply/config' -H
  'Authorization: Bearer YOUR_TOKEN'
tags:
  - api
  - recon
  - config
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:28.496Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-config

## Command

```bash
curl -X GET 'https://lark.example.com/api/v1/autoreply/config' -H 'Authorization: Bearer YOUR_TOKEN'
```

## Description

This curl command retrieves the AutoReply configuration from Lark's API, useful for reconnaissance to inspect file ID structures and endpoint behaviors during IDOR vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method for fetching config | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authenticates the request with a session token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://lark.example.com/api/v1/autoreply/config' -H 'Authorization: Bearer abc123'
```

### Advanced Usage

```bash
curl -X GET 'https://lark.example.com/api/v1/autoreply/config' -H 'Authorization: Bearer abc123' -o config.json
```

## Expected Output

JSON response with AutoReply settings, e.g., {"config": {"file_id": "abc123"}}, revealing direct references for exploitation.

## Related

- [[Related Procedure: Explore-Lark-AutoReply-Feature]]
