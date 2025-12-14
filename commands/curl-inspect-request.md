---
id: cmd-curl-inspect-request
data: >-
  curl -X GET 'https://monitor.mozilla.org/api/emails' -H 'Authorization: Bearer
  YOUR_TOKEN'
tags:
  - web
  - api
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.429Z'
verified: false
validated: true
submitted: true
---
# curl-inspect-request

## Command

```bash
curl -X GET 'https://monitor.mozilla.org/api/emails' -H 'Authorization: Bearer YOUR_TOKEN'
```

## Description

This command retrieves the list of secondary emails for the authenticated user in Mozilla Monitor, allowing inspection of email IDs and request structure to identify IDOR opportunities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://monitor.mozilla.org/api/emails` | Endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://monitor.mozilla.org/api/emails' -H 'Authorization: Bearer YOUR_TOKEN'
```

### Advanced Usage

```bash
curl -X GET 'https://monitor.mozilla.org/api/emails' -H 'Authorization: Bearer YOUR_TOKEN' -v
```

## Expected Output

JSON array of emails with IDs, e.g., `[{ "id": 12345, "email": "test@example.com" }]`. Use this to note ID formats.

## Related

- [[Related Procedure]]
