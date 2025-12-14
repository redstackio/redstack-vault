---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -H "Authorization: Bearer EXPOSED_API_KEY"
  https://api.adobe.com/v1/test-endpoint
tags:
  - api-testing
  - credential-check
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.323Z'
verified: false
validated: true
submitted: true
---
# curl-test-api-key

## Command

```bash
curl -H "Authorization: Bearer EXPOSED_API_KEY" https://api.adobe.com/v1/test-endpoint
```

## Description

This command tests the validity of an exposed API key by sending an HTTP request to an Adobe API endpoint using Bearer token authentication. It is used to verify if the key remains active post-exposure, enabling detection of rotation failures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds a custom header (Authorization: Bearer <key>) | Yes |
| `EXPOSED_API_KEY` | The API key to test | Yes |
| URL | Target API endpoint (e.g., https://api.adobe.com/v1/test-endpoint) | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer abc123def456" https://api.adobe.com/v1/status
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer abc123def456" -X POST https://api.adobe.com/v1/data -d '{"test":"data"}'
```

## Expected Output

Successful execution returns HTTP 200 with JSON data like {"status":"ok", "data":[...]}, indicating valid key. Failure shows 401 Unauthorized.

## Related

- [[Related Procedure: Check-Exposed-API-Key-Validity]]
