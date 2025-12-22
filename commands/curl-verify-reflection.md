---
data: >-
  curl -X GET
  "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=test_reflection"
  -H "Authorization: Bearer YOUR_API_TOKEN"
tags:
  - api
  - reflection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.098Z'
id: 26a0243f-5f27-4e84-823a-8b1a5a710565
verified: false
validated: true
submitted: true
---
# curl-verify-reflection

## Command

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=test_reflection" -H "Authorization: Bearer YOUR_API_TOKEN"
```

## Description

Tests reflection by injecting a test string in the 'url' parameter and checking the error response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=test_reflection` | Test string for mirroring | Yes |
| `-H "Authorization: ..."` | Auth header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/123/siteaudit/page/list?url=echo_me" -H "Authorization: Bearer token"
```

## Expected Output

Error message containing "test_reflection" directly.

## Related

- [[Related Procedure: Verify-URL-Parameter-Reflection]]
