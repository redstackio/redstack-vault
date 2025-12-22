---
data: >-
  curl -X DELETE 'https://api.linkedin.com/learning/comments/{target_urn}' -H
  'Authorization: Bearer {access_token}' -H 'Content-Type: application/json'
tags:
  - api
  - deletion
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.096Z'
id: 89477809-4863-43b5-a96a-4cc466e7a3f6
verified: false
validated: true
submitted: true
---
# curl-delete-comment

## Command

```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/{target_urn}' -H 'Authorization: Bearer {access_token}' -H 'Content-Type: application/json'
```

## Description

Executes a comment deletion via the LinkedIn Learning API, used to test unauthorized access by targeting modified URNs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies deletion method | Yes |
| `{target_urn}` | URN of the comment to delete | Yes |
| `-H 'Authorization: Bearer {access_token}'` | Auth header | Yes |
| `-H 'Content-Type: application/json'` | Request content type | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/urn:li:comment:123' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/urn:li:comment:123' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' --data '{}'
```

## Expected Output

Success: `{"message": "Comment deleted"}` or 204 status; failure: 403 or 404 error.

## Related

- [[Related Procedure]]
