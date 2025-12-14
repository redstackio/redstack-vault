---
id: cmd-uuid-001
data: >-
  curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json"
  -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input:
  $input) { ... on LogInUserSuccess { token } }
  }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}'
  -c cookies.txt -v
tags:
  - graphql
  - login
type: command
output: HTTP/1.1 200 OK or 429 with throttle message; JSON body with auth error.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.269Z'
verified: false
validated: true
submitted: true
---
# curl-invalid-login

## Command

```bash
curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -v
```

## Description

Sends an invalid login attempt to a GraphQL endpoint to trigger rate limiting or auth failure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '...'` | GraphQL mutation payload with invalid creds | Yes |
| `-c cookies.txt` | Saves cookies to file | No |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}' -v
```

### Advanced Usage

```bash
curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -s | jq .
```

## Expected Output

HTTP response with 200 and JSON error (e.g., invalid credentials) or 429 throttle after repeats.

## Related

- [[commands/curl-valid-login]]
- [[procedures/Trigger-Rate-Limiting-on-GraphQL-Login]]
