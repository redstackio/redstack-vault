---
data: >-
  {appInstallations(first:100)   {edges{node{id, launchUrl, app{apiKey,
  features}}}}}
tags:
  - graphql
  - app-installations
  - disclosure
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.058Z'
id: bfb8da9b-805b-42c4-92dc-4ae4970c8810
verified: false
validated: true
submitted: true
---
# graphql-query-app-installations-basic

## Command

```graphql
{appInstallations(first:100)   {edges{node{id, launchUrl, app{apiKey, features}}}}}
```

## Description

Basic GraphQL query for the first 100 app installations, retrieving IDs, launch URLs, API keys, and features to test permission bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first:100 | Limits to first 100 installations | Yes |
| edges{node{...}} | Retrieves node details: id, launchUrl, app.apiKey, app.features | Yes |

## Examples

### Basic Usage

```graphql
{appInstallations(first:100)   {edges{node{id, launchUrl, app{apiKey, features}}}}}
```

### Advanced Usage

Add more fields:

```graphql
{appInstallations(first:100) {edges{node{id, launchUrl, app{apiKey, features, title}}}}}
```

## Expected Output

JSON data.appInstallations with edges containing node.id (global ID), launchUrl (string), app.apiKey (string), and app.features (array), without errors.

## Related

- [[commands/graphql-query-app-installations-detailed]]
- [[procedures/Query-App-Installations-for-Sensitive-App-Details]]
