---
data: >-
  {appInstallations(first:100) {edges{node{id,publication{name}, launchUrl,
  app{apiKey, features, pricingDetails, published, feedback{messages{message}}
  }}}}}
tags:
  - graphql
  - app-installations
  - pricing
  - disclosure
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.054Z'
id: 12a43e8e-58a0-4ba8-81f9-2b2a9df86805
verified: false
validated: true
submitted: true
---
# graphql-query-app-installations-detailed

## Command

```graphql
{appInstallations(first:100) {edges{node{id,publication{name}, launchUrl, app{apiKey, features, pricingDetails, published, feedback{messages{message}} }}}}} 
```

## Description

Detailed GraphQL query for app installations, including publication names, API keys, features, pricing, status, and feedback messages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first:100 | Limits to first 100 | Yes |
| edges{node{...}} | Includes publication.name, launchUrl, app.apiKey, features, pricingDetails, published, feedback.messages.message | Yes |

## Examples

### Basic Usage

```graphql
{appInstallations(first:100) {edges{node{id,publication{name}, launchUrl, app{apiKey, features, pricingDetails, published, feedback{messages{message}} }}}}} 
```

### Advanced Usage

Filter by status:

```graphql
{appInstallations(first:100, query:"published:true") {edges{node{...}}}}
```

## Expected Output

JSON with expanded node data, including publication.name (string), pricingDetails (object), published (boolean), and feedback messages (array of strings); some fields may be null but core data like apiKey exposed.

## Related

- [[commands/graphql-query-app-installations-basic]]
- [[procedures/Query-App-Installations-for-Sensitive-App-Details]]
