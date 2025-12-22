---
data: >-
  curl -X GET
  "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=invalid_input"
  -H "Authorization: Bearer YOUR_API_TOKEN"
tags:
  - api
  - error-trigger
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.104Z'
id: 609788e9-5adc-4d5b-896e-358c3906bbff
verified: false
validated: true
submitted: true
---
# curl-trigger-mongodb-error

## Command

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=invalid_input" -H "Authorization: Bearer YOUR_API_TOKEN"
```

## Description

Sends a GET request to the Semrush API with an invalid 'url' parameter to trigger a MongoDB error response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `url=invalid_input` | Malformed URL to provoke error | Yes |
| `-H "Authorization: Bearer YOUR_API_TOKEN"` | API authentication header | Yes if auth required |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/123/siteaudit/page/list?url=invalid" -H "Authorization: Bearer token123"
```

### Advanced Usage

Add verbose output:

```bash
curl -v -X GET "https://api.semrush.com/reports/v1/projects/123/siteaudit/page/list?url=invalid" -H "Authorization: Bearer token123"
```

## Expected Output

JSON response with MongoDB error, e.g., {"error": "MongoError: ..."}

## Related

- [[Related Procedure: Trigger-MongoDB-Error-in-Semrush-API]]
