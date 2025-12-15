---
data: >-
  query{publications(first: 100){edges{node{name, id, supportsFuturePublishing,
  app{apiKey}}}}}}
tags:
  - graphql
  - api-keys
  - disclosure
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.061Z'
id: 9f645ad4-6614-41c1-92f0-21b540e6f296
verified: false
validated: true
submitted: true
---
# graphql-query-publications-api-keys

## Command

```graphql
query{publications(first: 100){edges{node{name, id, supportsFuturePublishing, app{apiKey}}}}}}
```

## Description

This GraphQL query retrieves the first 100 publications, including names, IDs, future publishing support, and associated app API keys, bypassing permission checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first: 100 | Limits results to the first 100 edges | Yes |
| edges{node{...}} | Accesses node fields: name, id, supportsFuturePublishing, and nested app.apiKey | Yes |

## Examples

### Basic Usage

```graphql
query{publications(first: 100){edges{node{name, id, supportsFuturePublishing, app{apiKey}}}}}}
```

### Advanced Usage

Include more app details:

```graphql
query{publications(first: 100){edges{node{name, id, supportsFuturePublishing, app{apiKey, title}}}}}}
```

## Expected Output

JSON with data.publications containing edges, each node showing name (string), id (global ID), supportsFuturePublishing (boolean), and app.apiKey (string), confirming key exposure.

## Related

- [[commands/graphql-query-marketing-activities]]
- [[procedures/Query-Publications-to-Retrieve-API-Keys]]
