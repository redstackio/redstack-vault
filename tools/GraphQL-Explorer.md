---
url: 'https://localhost/-/graphql-explorer'
tags:
  - graphql
  - api
  - testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.627Z'
id: ae9a1abf-f598-492e-80a6-780a5d22bfe6
validated: true
submitted: true
---
# GraphQL Explorer

**Status**: Unverified

## Overview

GraphQL Explorer is GitLab's built-in web interface for testing and executing GraphQL queries and mutations, ideal for API-based attacks like injecting payloads into custom resources.

## Description

It allows authenticated users to explore schemas, write queries, and send mutations interactively. In security contexts, it's used to test API vulnerabilities, such as unvalidated inputs in custom emoji creation, without needing external tools.

## Features

- Feature 1: Schema introspection and documentation
- Feature 2: Real-time query execution with authentication
- Feature 3: Response formatting and error handling

## Installation

### Requirements

- GitLab instance with GraphQL API enabled
- Browser access

### Install Commands

```bash
# Built-in; access via browser at /-/graphql-explorer
```

## Basic Usage

```bash
# No CLI; open in browser
```

### Common Options

| Option | Description |
|--------|-------------|
| Headers | Add auth tokens manually |

## Examples

### Example 1: Basic Usage

Paste mutation and click 'Run query'.

### Example 2: Advanced Usage

Include variables for dynamic payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- API logs showing explorer access
- High volume of mutation requests

## Related Procedures

- [[procedures/Create-Malicious-Custom-Emoji-via-GraphQL]]

## Related Tools

- [[tools/Web-Browser]]

## References

- GitLab GraphQL API docs
