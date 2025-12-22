---
type: command
executor: bash
data: >-
  curl -X POST http://target.com/graphql -H "Content-Type: application/json" -d
  '{"query": "mutation { signIn(login: \"Admin\", password: \"secretp@ssw0rd\")
  { token } }"}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - graphql
  - authentication
verified: true
validated: true
---

# graphql-admin-signin-mutation

## Command

```bash
curl -X POST $_ENDPOINT \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { signIn(login: \"$_LOGIN\", password: \"$_PASSWORD\") { token } }"}'
```

## Description

Sends a GraphQL signIn mutation to authenticate as an admin user and retrieve a session token. Use this to gain elevated access before performing destructive mutations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ENDPOINT | Target GraphQL endpoint URL (e.g., http://target.com/graphql) | Yes |
| $_LOGIN | Admin login username | Yes |
| $_PASSWORD | Admin password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { signIn(login: \"Admin\", password: \"secretp@ssw0rd\") { token } }"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST http://target.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation { signIn(login: \"Admin\", password: \"secretp@ssw0rd\") { token } }"}'
```

## Expected Output

Successful response includes the token:

```json
{
  "data": {
    "signIn": {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
  }
}
```

Error if credentials invalid:

```json
{
  "errors": [
    {
      "message": "Invalid credentials"
    }
  ]
}
```

## Related

- [[procedures/GraphQL-Injection-via-Mutations-for-Credential-Theft-and-User-Addition]]
