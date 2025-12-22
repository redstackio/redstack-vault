---
url: 'https://swagger.io/tools/swagger-ui/'
tags:
  - rendering
  - openapi
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.692Z'
id: 1012e5d7-d336-4b54-852f-192448cd9e1b
validated: true
submitted: true
---
# SwaggerUIBundle

**Status**: Unverified

## Overview

SwaggerUIBundle is a JavaScript library for rendering interactive documentation of OpenAPI specifications, commonly used in web applications like GitLab's blob viewer for visualizing API docs.

## Description

In security contexts, it can be exploited if it renders user-controlled content without proper sanitization, allowing HTML attributes in fields like descriptions to persist and enable XSS when combined with other libraries like jQuery.

## Features

- Feature 1: Parses and displays OpenAPI/Swagger JSON/YAML
- Feature 2: Generates interactive API explorers
- Feature 3: Supports HTML rendering in descriptions, vulnerable to attribute injection

## Installation

### Requirements

- Node.js environment
- npm or yarn

### Install Commands

```bash
npm install swagger-ui-dist
```

## Basic Usage

```bash
# Typically bundled in web apps, not direct CLI
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Library imported via script tag or bundle |

## Examples

### Example 1: Basic Usage

In HTML/JS:

```javascript
const ui = SwaggerUIBundle({
  spec: openapiSpec,
  dom_id: '#swagger-ui'
});
```

### Example 2: Advanced Usage

Custom plugins for rendering, but defaults allow unsafe HTML.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for SwaggerUI script loads in web apps
- Scan for unsanitized OpenAPI renders

## Related Procedures


## Related Tools

- [[tools/jQuery-ujs]]

## References

- Official documentation: https://swagger.io/docs/
- Related resources: GitLab vulnerability reports
