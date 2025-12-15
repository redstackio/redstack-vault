---
data: >-
  curl -X GET 'https://api.linkedin.com/learning/comments?thread_id={thread_id}'
  -H 'Authorization: Bearer {token}'
tags:
  - api
  - recon
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.101Z'
id: b92839b4-b1fd-4ec8-ba17-1dd126361c8f
verified: false
validated: true
submitted: true
---
# curl-inspect-api

## Command

```bash
curl -X GET 'https://api.linkedin.com/learning/comments?thread_id={thread_id}' -H 'Authorization: Bearer {token}'
```

## Description

This command fetches comments from a LinkedIn Learning Q&A thread to inspect URNs and API structure, useful for reconnaissance in access control testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `thread_id` | ID of the Q&A thread | Yes |
| `-H 'Authorization: Bearer {token}'` | Authenticates the request | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://api.linkedin.com/learning/comments?thread_id=12345' -H 'Authorization: Bearer abc123'
```

### Advanced Usage

```bash
curl -X GET 'https://api.linkedin.com/learning/comments?thread_id=12345&limit=50' -H 'Authorization: Bearer abc123' -o comments.json
```

## Expected Output

JSON array of comments with URNs, e.g., `{"comments": [{"urn": "urn:li:comment:67890", "owner": "user_id"}]}`.

## Related

- [[Related Procedure]]
