---
id: cmd-uuid-1
data: >-
  curl -X POST https://arrive-server.shopifycloud.com/graphql -H "Content-Type:
  application/json" -H "Accept-Encoding: gzip, deflate" -H "User-Agent:
  Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)" -H
  "Host: arrive-server.shopifycloud.com" -H "Connection: close" --data-raw
  '{"operationName":"SendVerificationEmail","variables":{"email":"EMAILHERE"},"query":"mutation
  SendVerificationEmail($email: String!) { sendVerificationEmail(email: $email)
  { userErrors { field message __typename } __typename } }"}'
tags:
  - graphql
  - email
type: command
output: >-
  {"data":{"sendVerificationEmail":{"__typename":"SendVerificationEmailPayload","userErrors":[]}}}
executor: curl
platforms:
  - Linux
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.308Z'
verified: false
validated: true
submitted: true
---
# send-verification-email-graphql

## Command

```bash
curl -X POST https://arrive-server.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)" \
  -H "Host: arrive-server.shopifycloud.com" \
  -H "Connection: close" \
  --data-raw '{"operationName":"SendVerificationEmail","variables":{"email":"EMAILHERE"},"query":"mutation SendVerificationEmail($email: String!) { sendVerificationEmail(email: $email) { userErrors { field message __typename } __typename } }"}'
```

## Description

Sends a GraphQL mutation to request a verification email for the Arrive app, triggering a magic link. Use when targeting a known email for login initiation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| email | Target user's email address | Yes |
| User-Agent | Mimics Android client | No |

## Examples

### Basic Usage

```bash
curl ... --data-raw '{"variables":{"email":"target@example.com"}, ...}'
```

### Advanced Usage

Add cookies for session persistence if needed.

## Expected Output

JSON response confirming email sent without errors, e.g., {"data":{"sendVerificationEmail":{"userErrors":[]}}}

## Related

- [[commands/verify-token-graphql]]
