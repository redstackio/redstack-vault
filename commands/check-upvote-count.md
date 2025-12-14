---
data: >-
  curl -X GET -H "Cookie: session=abc123" https://target.com/reviews/comment/123
  | grep -o '"upvotes":[0-9]*'
tags:
  - http
  - verification
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T17:24:22.833Z'
id: e3496df5-1a76-4e5b-b43b-56d4ae9c2f25
verified: false
validated: true
submitted: true
---
# check-upvote-count

## Command

```bash
curl -X GET -H "Cookie: session=abc123" https://target.com/reviews/comment/123 | grep -o '"upvotes":[0-9]*'
```

## Description

This command retrieves the comment details via GET request and extracts the upvote count to verify if inflation occurred after exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `-H "Cookie: session=abc123"` | Authentication header | Yes |
| `https://target.com/reviews/comment/123` | Target comment URL | Yes |
| `| grep -o '"upvotes":[0-9]*'` | Extract upvote field from response | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://example.com/comment/123 | grep upvotes
```

### Advanced Usage

```bash
curl -s -X GET -H "Cookie: session=abc123" -H "Accept: application/json" https://target.com/reviews/comment/123 | jq '.upvotes'
```

## Expected Output

Extracted string like "upvotes":15, indicating the current count.

## Related

- [[commands/concurrent-like-requests]]
- [[procedures/Exploit-Race-Condition-in-Comments-Likes]]
