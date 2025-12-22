---
url: 'https://gitlab.com/-/graphql-explorer'
tags:
  - graphql
  - api-testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.254Z'
id: dd8fbfd9-58a8-4a3f-8cea-59636fd7d19d
validated: true
submitted: true
---
# GitLab-GraphQL-Explorer

**Status**: Unverified

## Overview

The GitLab GraphQL Explorer is an interactive web-based tool for testing and executing GraphQL queries against GitLab's API, allowing users to explore schema, build queries, and view responses in real-time. It's commonly used in security testing to identify authorization flaws and information disclosures in API endpoints.

## Description

This browser-based interface provides autocomplete for GraphQL schema, query validation, and execution without needing API tokens for public access. In offensive security, it's leveraged to probe for over-privileged endpoints, such as fetching restricted data like private notes. No installation required; it's hosted on GitLab instances. Key capabilities include schema introspection, variable support, and response formatting (JSON).

## Features

- Feature 1: Interactive schema explorer with field suggestions and documentation
- Feature 2: Query execution in unauthenticated or authenticated sessions
- Feature 3: Response highlighting and error details for debugging API issues

## Installation

### Requirements

- Web browser (e.g., Chrome, Firefox)
- Access to a GitLab instance

### Install Commands

No installation needed; access via URL.

## Basic Usage

```bash
# Simply navigate in browser
# No CLI; web-only
```

### Common Options

| Option | Description |
|--------|-------------|
| Query Editor | Paste or write GraphQL queries |
| Variables | JSON input for query parameters |
| Headers | Add auth tokens if needed (unauthenticated by default) |

## Examples

### Example 1: Basic Usage

Navigate to https://gitlab.com/-/graphql-explorer, paste a simple query like `query { currentUser { name } }`, and execute to test access.

### Example 2: Advanced Usage

In the explorer, enter a complex query targeting issues and notes, set no headers for unauthenticated mode, and execute to fetch private data.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[T1213.003]] Code Repositories

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Web logs showing accesses to /-/graphql-explorer from unauthenticated IPs
- High volume of GraphQL queries on sensitive fields like notes.system
- Anomalous response sizes indicating data exfiltration

## Related Procedures

- [[procedures/Exploit-GitLab-GraphQL-for-Private-Note-Disclosure]]

## Related Tools

- [[GraphQL Playground]]
- [[Postman]]

## References

- Official GitLab GraphQL Docs: https://docs.gitlab.com/ee/api/graphql/
- HackerOne Report: https://hackerone.com/reports/633001
