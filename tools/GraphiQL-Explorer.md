---
id: uuid-graphiql
url: 'https://gitlab.com/gitlab-org/gitlab/-/issues/related_to_graphiql'
tags:
  - graphql
  - explorer
type: tool
verified: false
platforms:
  - Web
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.114Z'
validated: true
submitted: true
---
# GraphiQL-Explorer

**Status**: Unverified

## Overview

GraphiQL Explorer is GitLab's built-in interactive GraphQL IDE for exploring schemas, writing queries, and executing mutations like destroySnippet during security testing.

## Description

Accessible at /-/graphiql-explorer in a GitLab project, it allows authenticated users to test GraphQL endpoints. In offensive ops, it's used to run exploit mutations with custom IDs, validating responses without external tools. Supports schema introspection and error handling.

## Features

- Feature 1: Interactive query builder with autocomplete
- Feature 2: Real-time execution and response viewing
- Feature 3: Schema documentation explorer

## Installation

### Requirements

- GitLab instance with GraphQL enabled (default)
- Maintainer or higher access

### Install Commands

No installation; built-in to GitLab.

## Basic Usage

Navigate to project > Explore > GraphiQL.

### Common Options

| Option | Description |
|--------|-------------|
| Docs sidebar | View schema |
| Execute button | Run query/mutation |

## Examples

### Example 1: Basic Usage

Enter mutation in editor, click Execute to test destroySnippet.

### Example 2: Advanced Usage

Use variables for parameterized inputs.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Access logs to /graphiql-explorer
- Unusual mutation executions in GraphQL logs

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: GitLab GraphQL docs
- Related resources: GraphQL.org tutorials
