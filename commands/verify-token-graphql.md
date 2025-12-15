---
id: cmd-uuid-2
data: >-
  curl -X POST https://arrive-server.shopifycloud.com/graphql -H "Content-Type:
  application/json" -H "Accept-Encoding: gzip, deflate" -H "Cookie:
  _arrive-server_session=2a969ef15e1cc286ca6c5a88433d7173" -H "User-Agent:
  Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)" -H
  "Host: arrive-server.shopifycloud.com" -H "Connection: close" --data-raw
  '{"operationName":"VerifyToken","variables":{"token":"TOKENHERE"},"query":"mutation
  VerifyToken($token: String!) { verifyToken(token: $token) { user { id
  __typename } userErrors { field message __typename } __typename } }"}'
tags:
  - graphql
  - token-verify
type: command
output: >-
  {"data":{"verifyToken":{"user":{"id":"123","__typename":"User"},"userErrors":[]}}},
  Set-Cookie: _arrive-server_session=new_session
executor: curl
platforms:
  - Linux
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.305Z'
verified: false
validated: true
submitted: true
---
# verify-token-graphql

## Command

```bash
curl -X POST https://arrive-server.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Cookie: _arrive-server_session=2a969ef15e1cc286ca6c5a88433d7173" \
  -H "User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)" \
  -H "Host: arrive-server.shopifycloud.com" \
  -H "Connection: close" \
  --data-raw '{"operationName":"VerifyToken","variables":{"token":"TOKENHERE"},"query":"mutation VerifyToken($token: String!) { verifyToken(token: $token) { user { id __typename } userErrors { field message __typename } __typename } }"}'
```

## Description

Verifies a magic link token via GraphQL to obtain a session cookie for account access in the Arrive app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| token | Extracted token from deeplink | Yes |
| Cookie | Existing session if any | No |

## Examples

### Basic Usage

```bash
curl ... --data-raw '{"variables":{"token":"actual_token"}, ...}'
```

### Advanced Usage

Include verbose output with -v for headers.

## Expected Output

JSON with user ID and Set-Cookie header for session.

## Related

- [[commands/send-verification-email-graphql]]
