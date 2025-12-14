---
url: 'https://axios-http.com/'
tags:
  - http-client
  - javascript
type: tool
platforms:
  - Web
description: >-
  Promise-based HTTP client for the browser and Node.js, used in GitLab for
  loading diff content.
id: 18beebec-9472-433f-8e7d-3a04d8d7da0a
created_at: '2025-12-14T00:11:16.617Z'
updated_at: '2025-12-14T00:11:16.617Z'
verified: false
validated: true
submitted: true
---
# Axios

**Status**: Unverified

## Overview

Axios is a JavaScript library for making HTTP requests, supporting promises and interceptors.

## Description

In GitLab, it's used in single_file_diff.js to fetch JSON via GET, enabling CSP bypass when loading malicious content.

## Features

- Promise-based requests
- Automatic transforms for JSON data
- Client-side XSRF protection

## Installation

### Requirements

- Node.js or browser environment

### Install Commands

```bash
npm install axios
```

## Basic Usage

```javascript
axios.get('/url')
```

### Common Options

| Option | Description |
|--------|-------------|
| `method` | HTTP method |

## Examples

### Example 1: Basic Usage

```javascript
axios.get('https://example.com')
```

### Example 2: Advanced Usage

```javascript
axios.get('/diff', { params: { path: 'malicious.json' } })
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor network requests for unexpected GETs to JSON paths
- Inspect JavaScript for axios imports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nokogiri]]
- [[tools/jQuery]]

## References

- https://axios-http.com/docs/intro
