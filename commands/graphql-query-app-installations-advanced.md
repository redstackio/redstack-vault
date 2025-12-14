---
data: >-
  {appInstallations(first:100) {edges{node{id, launchUrl,
  app{pricingDetailsSummary, apiKey, features, pricingDetails,
  failedRequirements{action{url, title}}, published, feedback{messages{message},
  link{url}} }}}}}
tags:
  - graphql
  - app-installations
  - feedback
  - disclosure
type: command
output: null
executor: graphql
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.044Z'
id: 04bef3fb-8036-45f8-8fcc-0bb86f5feb7e
verified: false
validated: true
submitted: true
---
# graphql-query-app-installations-advanced

## Command

```graphql
{appInstallations(first:100) {edges{node{id, launchUrl, app{pricingDetailsSummary, apiKey, features, pricingDetails, failedRequirements{action{url, title}}, published, feedback{messages{message}, link{url}} }}}}} 
```

## Description

Advanced GraphQL query for app installations, capturing pricing summaries, API keys, failed requirements, publication status, feedback messages, and links.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| first:100 | Limits to first 100 | Yes |
| edges{node{...}} | Retrieves id, launchUrl, app.pricingDetailsSummary, apiKey, features, pricingDetails, failedRequirements.action{url,title}, published, feedback{messages.message, link.url} | Yes |

## Examples

### Basic Usage

```graphql
{appInstallations(first:100) {edges{node{id, launchUrl, app{pricingDetailsSummary, apiKey, features, pricingDetails, failedRequirements{action{url, title}}, published, feedback{messages{message}, link{url}} }}}}} 
```

### Advanced Usage

Include more nesting:

```graphql
{appInstallations(first:100) {edges{node{app{... , developer{name}}}}}}
```

## Expected Output

Comprehensive JSON response with app.pricingDetailsSummary (string), failedRequirements (array with action.url and title), feedback.link.url (string), and persistent apiKey exposure.

## Related

- [[commands/graphql-query-app-installations-detailed]]
- [[procedures/Query-App-Installations-for-Sensitive-App-Details]]
