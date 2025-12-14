---
url: 'http://gitlab.example.vm/-/graphql-explorer'
tags:
  - graphql
  - testing
type: tool
verified: false
platforms:
  - Web
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.401Z'
id: 077bb235-201a-4f2f-846e-ec189fad35fd
validated: true
submitted: true
---
# GraphQL-Explorer

**Status**: Unverified

## Overview

GitLab's built-in web interface for exploring, testing, and executing GraphQL queries and mutations, ideal for vulnerability assessment in API endpoints.

## Description

The GraphQL Explorer provides an interactive playground for GitLab's GraphQL API, allowing authenticated users to craft and send requests. In offensive security, it's used to test mutations like deleteAnnotation for exploits such as type confusion. Supports introspection and real-time execution.

## Features

- Feature 1: Interactive query builder with schema introspection
- Feature 2: Authentication integration for role-based testing
- Feature 3: Response formatting and error handling

## Installation

### Requirements

- GitLab instance access
- Authenticated browser session

### Install Commands

No installation needed; access via browser at /-/graphql-explorer.

## Basic Usage

```bash
# Open in browser
open http://gitlab.example.vm/-/graphql-explorer
```

### Common Options

| Option | Description |
|--------|-------------|
| Query Editor | Input GraphQL syntax |
| Execute Button | Run the query/mutation |

## Examples

### Example 1: Basic Usage

Enter a simple query and execute to fetch projects.

### Example 2: Advanced Usage

Craft mutation for exploitation:

```graphql
mutation { deleteAnnotation(input: {id: "gid://GitLab/Project/123"}) { clientMutationId } }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser access logs to /graphql-explorer
- Anomalous GraphQL mutation volumes

## Related Procedures


## Related Tools

- [[tools/IRB]]

## References

- GitLab GraphQL Documentation
