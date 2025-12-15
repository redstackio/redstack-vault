---
id: tool-graphql-client
url: 'https://www.graphql.org/'
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
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.552Z'
validated: true
submitted: true
---
# GraphQL Client

**Status**: Unverified

## Overview

GraphQL clients like Insomnia, Postman, or Altair are used to construct, send, and debug GraphQL queries against APIs, ideal for testing vulnerabilities in endpoints like HackerOne's search features.

## Description

These tools provide a GUI or CLI for interacting with GraphQL servers, supporting query building, variable passing, authentication, and response introspection. In offensive security, they enable crafting complex queries like aggregations to probe for info disclosure flaws without writing custom scripts.

## Features

- Feature 1: Visual query editor with schema introspection.
- Feature 2: Support for authentication (Bearer tokens, cookies).
- Feature 3: Response formatting (JSON pretty-print, error highlighting).

## Installation

### Requirements

- Node.js (for some clients like Altair).
- Basic HTTP client capabilities.

### Install Commands

```bash
# For Insomnia (via binary download)
# Download from https://insomnia.rest/

# For curl (built-in on most systems)
# No install needed

# For Altair (Chrome extension or app)
npm install -g @altair-graphql/desktop-app
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
curl -X POST https://api.example.com/graphql -d '{"query": "{ hello }"}'
```

### Example 2: Advanced Usage

In Insomnia: Create new request, set URL to endpoint, paste query in body as JSON.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing GraphQL POST requests with aggregation queries.
- User-agent strings from client tools in API access logs.

## Related Procedures

- [[Prepare GraphQL Client for HackerOne API]]
- [[Execute Terms Aggregation Query on Handle Field]]

## Related Tools

- [[Postman]]
- [[Burp Suite]]

## References

- Official GraphQL docs: https://graphql.org/
- Insomnia: https://insomnia.rest/
