---
id: tool-graphiql-001
url: 'https://electronjs.org/apps/graphiql'
tags:
  - graphql
  - api-testing
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.075Z'
validated: true
submitted: true
---
# GraphiQL

**Status**: Unverified

## Overview

GraphiQL is an in-browser IDE for exploring and executing GraphQL queries against endpoints, ideal for security testing of API schemas, filter bypasses, and information disclosure vulnerabilities.

## Description

GraphiQL provides syntax highlighting, auto-completion, and real-time query execution, making it suitable for crafting complex 'where' filters and observing responses in offensive security operations like schema bypass exploits.

## Features

- Feature 1: Interactive schema introspection for field discovery
- Feature 2: Query execution with variable support and response visualization
- Feature 3: History and documentation pane for iterative testing

## Installation

### Requirements

- Node.js (for custom setups) or use pre-built Electron app
- Web browser for online versions

### Install Commands

```bash
# Download from https://electronjs.org/apps/graphiql or use npm for integration
npm install -g graphiql-cli
```

## Basic Usage

```bash
graphiql --endpoint https://api.target.com/graphql
```

### Common Options

| Option | Description |
|--------|-------------|
| -e, --endpoint | Specify GraphQL endpoint URL |
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Launch and connect to endpoint:

```bash
graphiql -e https://api.hackerone.com/graphql
```

### Example 2: Advanced Usage

Execute a query file:

```bash
graphiql -e https://api.target.com/graphql -q exploit-query.gql
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to GraphQL endpoints with high query volume
- User-agent strings indicating GraphiQL/Electron app
- Anomalous introspection queries in API logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Postman]]
- [[Insomnia]]

## References

- Official documentation: https://github.com/graphql/graphiql
- Related resources: GraphQL security testing guides
