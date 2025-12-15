---
data: >-
  query{marketingActivities(first:100){edges{node{id,title, createdAt,
  budget{total{amount}}}}}}
tags:
  - graphql
  - marketing
  - disclosure
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.064Z'
id: d99ec429-8a77-4eb9-a58c-13f5698bcf36
verified: false
validated: true
submitted: true
---
# graphql-query-marketing-activities

## Command

```graphql
query{marketingActivities(first:100){edges{node{id,title, createdAt, budget{total{amount}}}}}}
```

## Description

This GraphQL query fetches the first 100 marketing activities from Shopify's Admin API, retrieving IDs, titles, creation dates, and total budget amounts to demonstrate unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first:100 | Limits the number of returned edges to 100 | Yes |
| edges{node{...}} | Traverses the connection to access specific node fields like id, title, createdAt, and budget.total.amount | Yes |

## Examples

### Basic Usage

```graphql
query{marketingActivities(first:100){edges{node{id,title, createdAt, budget{total{amount}}}}}}
```

### Advanced Usage

Add sorting or filters if supported:

```graphql
query{marketingActivities(first:100, sortKey:CREATED_AT){edges{node{id,title, createdAt, budget{total{amount}}}}}}
```

## Expected Output

A JSON response with a data.marketingActivities object containing an array of edges, each node exposing id (string), title (string), createdAt (datetime), and budget.total.amount (currency value), without access denied errors.

## Related

- [[commands/graphql-query-publications-api-keys]]
- [[procedures/Query-Marketing-Activities-Without-Marketing-Access]]
