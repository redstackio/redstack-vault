---
data: >-
  curl -X DELETE 'https://veris.example.com/api/groups/{group-id}' -H
  'Authorization: Bearer {token}' -H 'Content-Type: application/json' -v
tags:
  - web
  - api
  - delete
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 65f15b11-482f-4aaf-8542-ced82454e73f
created_at: '2025-12-14T17:25:23.181Z'
updated_at: '2025-12-14T17:25:23.181Z'
verified: false
validated: true
submitted: true
---
# curl-capture-group-delete

## Command

```bash
curl -X DELETE 'https://veris.example.com/api/groups/{group-id}' -H 'Authorization: Bearer {token}' -H 'Content-Type: application/json' -v
```

## Description

This command captures or simulates a group deletion request in the Veris API, useful for intercepting and analyzing the structure during IDOR testing. The -v flag provides verbose output for debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP DELETE method | Yes |
| `https://veris.example.com/api/groups/{group-id}` | Target endpoint with group ID | Yes |
| `-H 'Authorization: Bearer {token}'` | Authentication header | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-v` | Verbose mode for request/response details | No |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://veris.example.com/api/groups/123' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' -v
```

### Advanced Usage

```bash
curl -X DELETE 'https://veris.example.com/api/groups/123' -H 'Authorization: Bearer {token}' -H 'Content-Type: application/json' -d '{}' -v
```

## Expected Output

Verbose details of the request sent and response received, such as 200 OK for success or 403 for authorization failure, including headers and body.

## Related

- [[Related Procedure: Access-Veris-Group-Deletion-Functionality]]
- [[commands/curl-modify-group-id]]
