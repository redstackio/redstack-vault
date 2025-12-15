---
data: >-
  curl -X POST https://gql.reddit.com/ -H "User-Agent: Mozilla/5.0 (X11; Linux
  x86_64; rv:91.0) Gecko/20100101 Firefox/91.0" -H "Accept: */*" -H
  "Content-Type: application/json" -H "Authorization: Bearer your_token" -H
  "Origin: https://www.reddit.com" -H "Referer: https://www.reddit.com/" -d
  '{"id":"6243efcbc61d","variables":{"subredditName":"target-subreddit","after":"endCursorValue"}}'
tags:
  - graphql
  - pagination
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.049Z'
id: 57cc8cf1-f307-4ded-94f6-a41a26348326
verified: false
validated: true
submitted: true
---
# reddit-graphql-modlogs-paginated

## Command

```bash
curl -X POST https://gql.reddit.com/ \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0" \
  -H "Accept: */*" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token" \
  -H "Origin: https://www.reddit.com" \
  -H "Referer: https://www.reddit.com/" \
  -d '{"id":"6243efcbc61d","variables":{"subredditName":"target-subreddit","after":"endCursorValue"}}'
```

## Description

Sends a paginated GraphQL query for subsequent mod logs pages using the after cursor.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Bearer your_token | Reddit token | Yes |
| subredditName | Target subreddit | Yes |
| after | endCursor from prior response | Yes (for pagination) |
| id | Operation ID '6243efcbc61d' | Yes |

## Examples

### Basic Usage

```bash
curl ... -d '{"id":"6243efcbc61d","variables":{"subredditName":"example","after":"cursor123"}}'
```

### Advanced Usage

Integrate in loop for full collection.

## Expected Output

JSON with next batch of modActions, updated pageInfo.

## Related

- [[commands/reddit-graphql-modlogs-initial]]
- [[procedures/Paginate-Through-Moderator-Logs]]
