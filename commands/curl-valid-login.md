---
id: cmd-uuid-002
data: >-
  curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json"
  -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input:
  $input) { ... on LogInUserSuccess { token } }
  }","variables":{"input":{"email":"validuser@gmail.com","password":"validpass","client_id":"client_id","client_secret":"client_secret"}}}'
  -c cookies.txt -v
tags:
  - graphql
  - login
type: command
output: HTTP/1.1 200 OK with JSON containing access token.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.267Z'
verified: false
validated: true
submitted: true
---
# curl-valid-login

## Command

```bash
curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"validuser@gmail.com","password":"validpass","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -v
```

## Description

Submits valid credentials to GraphQL login for access token, useful for bypass testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d '...'` | Payload with valid creds | Yes |
| `-c cookies.txt` | Cookie jar | No |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"validuser@gmail.com","password":"validpass","client_id":"client_id","client_secret":"client_secret"}}}' -v
```

### Advanced Usage

Add silent mode and parse:

```bash
curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"validuser@gmail.com","password":"validpass","client_id":"client_id","client_secret":"client_secret"}}}' -s | jq '.data.logInUser.token'
```

## Expected Output

JSON response with successful login and token field populated.

## Related

- [[commands/curl-invalid-login]]
- [[procedures/Bypass-Throttle-with-Valid-Credentials]]
