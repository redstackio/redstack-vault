---
data: >-
  curl -X POST $ENDPOINT -H "Content-Type: application/json" -H "Authorization:
  Bearer $TOKEN" -d '{"query": "mutation { updateBanner(input: {id: \"$ID\",
  content: \"$CONTENT\"}) { banner { id content } } }"}'
tags:
  - graphql
  - modification
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.658Z'
id: 5d4317f0-6834-471b-9319-ae6f8f3ec31d
verified: false
validated: true
submitted: true
---
# graphql-modify-banner

## Command

```bash
curl -X POST $ENDPOINT -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query": "mutation { updateBanner(input: {id: \"$ID\", content: \"$CONTENT\"}) { banner { id content } } }"}'
```

## Description

Modifies a banner via GraphQL mutation using admin privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ENDPOINT | GraphQL URL | Yes |
| $TOKEN | Admin token | Yes |
| $ID | Banner ID | Yes |
| $CONTENT | New content | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Authorization: Bearer admin_token" -d '{"query": "mutation { updateBanner(input: {id: \"1\", content: \"New Banner\"}) { banner { id } } }"}'
```

## Expected Output

{"data":{"updateBanner":{"banner":{"id":"1","content":"New Banner"}}}}

## Related

- [[Related Procedure: Access-and-Modify-Privileged-Features]]
