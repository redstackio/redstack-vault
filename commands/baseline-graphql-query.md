---
data: >-
  curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121
  Safari/537.36' -H 'content-type: application/json' -H 'accept: */*'
  --data-binary '{"query":"query { search(q: \"AAA\", lang: \"en\") { _id
  weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
tags:
  - graphql
  - baseline
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.211Z'
id: d24dd3ef-4580-455d-93a1-8b69366bb812
verified: false
validated: true
submitted: true
---
# baseline-graphql-query

## Command

```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"AAA\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

## Description

Sends a benign GraphQL search query to establish baseline response time for the wiki.cs.money endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'user-agent: ...'` | Mimics browser headers | Yes |
| `-H 'content-type: application/json'` | Sets JSON payload type | Yes |
| `-H 'accept: */*'` | Accepts any response | Yes |
| `--data-binary` | Raw JSON GraphQL query | Yes |
| `--compressed` | Enables gzip | No |

## Examples

### Basic Usage

```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"AAA\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

### Advanced Usage

Add `-v` for verbose output to see timings.

```bash
curl -v 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"AAA\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

## Expected Output

JSON response with search results, e.g., {"data":{"search":[{"_id":"...","weapon_id":"..."}]}}, latency <1s.

## Related

- [[commands/probe-null-byte]]
- [[procedures/Baseline-GraphQL-Search-Query]]
