---
url: 'https://emitrani.myshopify.com/admin/apps/shopify-graphiql-app'
tags:
  - graphql
  - api-testing
type: tool
verified: false
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.270Z'
id: d321a4ea-1f0f-4234-b726-73c5129db130
validated: true
submitted: true
---
# Shopify-GraphiQL-App

**Status**: Unverified

## Overview

The Shopify GraphiQL App is a web-based interface for developers to test and execute GraphQL queries against the Shopify Admin API, ideal for exploring endpoints, parameters, and rate limiting behaviors in security testing.

## Description

This official Shopify app provides an interactive GraphQL playground within the admin dashboard, allowing real-time query execution, schema introspection, and response inspection including cost and throttle details. It's commonly used for API development but enables vulnerability testing like parameter fuzzing for business logic flaws.

## Features

- Feature 1: Interactive query editor with auto-completion
- Feature 2: Real-time execution against live Admin API
- Feature 3: Response extensions showing query costs and bucket status

## Installation

### Requirements

- Shopify partner or store admin account
- Installed via Shopify App Store

### Install Commands

No CLI install; access via admin dashboard after adding the app.

```bash
# No command needed; browse to admin/apps and search GraphiQL
```

## Basic Usage

```bash
# Open in browser: https://yourstore.myshopify.com/admin/apps/shopify-graphiql-app
# Paste query and click Execute
```

### Common Options

| Option | Description |
|--------|-------------|
| Query Editor | Input GraphQL queries |
| Schema Tab | Explore available fields |

## Examples

### Example 1: Basic Usage

Open app, run simple query like { shop { name } } to test connection.

### Example 2: Advanced Usage

Fuzz parameters: Change 'first: 10' to 'first: -100' and execute to test costs.

```graphql
# In editor: { appInstallations(first: -100) { ... } }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- API logs showing GraphiQL user-agent
- High volume of exploratory queries from admin IP
- Parameter anomalies in GraphQL requests

## Related Procedures


## Related Tools

- [[GraphQL Voyager]] for schema visualization
- [[Postman]] for API testing

## References

- Official: https://apps.shopify.com/graphiql-app
- Documentation: https://shopify.dev/docs/api/usage/graphql
