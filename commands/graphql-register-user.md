---
data: >-
  curl -X POST $ENDPOINT -H "Content-Type: application/json" -d '{"query":
  "mutation { register(input: {email: \"$EMAIL\", password: \"$PASSWORD\"}) {
  user { id email } token } }"}'
tags:
  - graphql
  - auth
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.671Z'
id: 143a69c4-0d9c-4abd-9f2e-17e3bc5691fe
verified: false
validated: true
submitted: true
---
# graphql-register-user

## Command

```bash
curl -X POST $ENDPOINT -H "Content-Type: application/json" -d '{"query": "mutation { register(input: {email: \"$EMAIL\", password: \"$PASSWORD\"}) { user { id email } token } }"}'
```

## Description

Executes the GraphQL Register mutation to create a user account and retrieve an auth token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $ENDPOINT | GraphQL API URL | Yes |
| $EMAIL | User email | Yes |
| $PASSWORD | User password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -d '{"query": "mutation { register(input: {email: \"test@example.com\", password: \"pass123\"}) { token } }"}'
```

### Advanced Usage

Add more fields if schema supports, e.g., name.

## Expected Output

{"data":{"register":{"user":{"id":"123","email":"test@example.com"},"token":"eyJ..."}}}

## Related

- [[Related Procedure: Register-Regular-User-Account]]
