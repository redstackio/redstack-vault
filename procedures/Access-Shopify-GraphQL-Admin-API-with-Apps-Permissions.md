---
tags:
  - graphql
  - access-control
  - shopify
type: procedure
tools:
  - '[[tools/GraphiQL]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:25:53.076Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b8bc4558-670e-405a-8f93-c788c1a21517
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Access-Shopify-GraphQL-Admin-API-with-Apps-Permissions

## Summary

This procedure establishes access to Shopify's GraphQL Admin API using only 'Apps' read permissions, setting the stage for testing over-privileged queries that bypass documented scope requirements.

## Description

In Shopify's ecosystem, the GraphQL Admin API is intended to enforce strict permission scopes, but misconfigurations allow 'Apps' permission holders to query sensitive endpoints. This procedure involves installing the GraphiQL app on a target store and authenticating with minimal privileges to explore the QueryRoot schema. The target environment is a Shopify store admin panel, and success reveals the API's lack of enforcement, enabling further information disclosure. Prerequisites include a valid Shopify account with 'Apps' access and installation rights for apps.

## Requirements

1. Shopify collaborator or staff account with 'Apps' read permissions only
2. Access to the target store's admin panel for app installation
3. Network connectivity to Shopify's API endpoints

## Defense

Defensive measures and detection strategies:

- Enforce strict GraphQL schema permissions and validate scopes at runtime
- Monitor API queries for anomalous access patterns from low-privilege accounts
- Use API gateways with rate limiting and audit logging for GraphQL endpoints

## Objectives

1. Establish authenticated access to GraphQL Admin API
2. Verify minimal permissions allow schema exploration
3. Identify over-privileged queries without additional scopes

## Instructions

### Step 1: Install GraphiQL App

**Context**: The GraphiQL app provides an interactive interface for testing GraphQL queries directly within the Shopify admin.

**Instructions**: Navigate to the Shopify App Store, search for GraphiQL, and install it on the target store. Authenticate using the low-privilege account.

**Expected Output**: GraphiQL interface accessible in the store admin, connected to the GraphQL Admin API endpoint.

### Step 2: Explore QueryRoot Schema

**Context**: Reference official documentation to understand expected permissions for queries.

**Instructions**: In GraphiQL, load the introspection query or browse the schema docs. Test a basic query like { shop { name } } to confirm access.

```graphql
query {
  shop {
    name
    myshopifyDomain
  }
}
```

> This basic query should succeed, indicating API access is granted. Expected output includes store name and domain without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/GraphiQL]]

## Tags

- [[graphql]]
- [[shopify]]
- [[api-access]]
