---
url: 'https://swagger.io/'
tags:
  - api-doc
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.583Z'
id: 92e2c1a0-c701-4d6a-b5e6-22391a5242a7
validated: true
submitted: true
---
# Swagger

**Status**: Unverified

## Overview

Swagger is an open-source tool for designing documenting and consuming RESTful APIs commonly used to generate interactive UI for endpoint exploration in security testing.

## Description

Swagger (now OpenAPI) allows automatic generation of API documentation from code annotations providing details on endpoints methods and parameters. In offensive security it's leveraged to discover unprotected routes in web APIs like those in proposal systems enabling reconnaissance without source access.

## Features

- Feature 1: Interactive UI for testing API calls
- Feature 2: Schema validation for requests/responses
- Feature 3: Export to various formats (JSON YAML)

## Installation

### Requirements

- Node.js for some implementations
- Typically server-side generated no client install needed

### Install Commands

```bash
# For Swagger Editor
npm install -g swagger-editor-dist
```

## Basic Usage

```bash
# Access via browser if exposed
open https://target/swagger
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Browser-based interaction |
| `--validate` | Validate API specs |

## Examples

### Example 1: Basic Usage

Navigate to exposed Swagger UI to browse endpoints.

### Example 2: Advanced Usage

Use Swagger Codegen to generate client:
```bash
swagger-codegen generate -i swagger.json -l javascript -o ./client
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Requests to /swagger or /api-docs
- User-agent strings indicating Swagger clients

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]
- [[Postman]]

## References

- Official documentation: https://swagger.io/docs/
- Related resources: OpenAPI Specification
