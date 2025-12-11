---
id: f2e180aa-e34d-4f2b-87be-b3b06c491312
name: XMLHttpRequest
type: tool
verified: false
created_at: '2025-12-11T06:10:15.554Z'
updated_at: '2025-12-11T06:10:15.554Z'
platforms:
  - Web
tags:
  - javascript
  - http
url: 'https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest'
description: JavaScript API for making HTTP requests.
validated: true
submitted: true
---

# XMLHttpRequest

**Status**: Unverified

## Overview

XMLHttpRequest is a built-in browser API for making asynchronous HTTP requests, used in attacks for fetching and exfiltrating data.

## Description

In this context, it's used synchronously with custom headers to query metadata endpoints during DNS rebinding.

## Features

- Feature 1: Synchronous and asynchronous requests
- Feature 2: Custom headers support
- Feature 3: GET/POST methods

## Installation

### Requirements

- Web browser or JS environment

### Install Commands

```bash
# Built-in, no install needed
```

## Basic Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', url, false);
xhr.send();
```

### Common Options

| Option | Description |
|--------|-------------|
| `open(method, url, async)` | Initialize request |
| `setRequestHeader` | Set headers |

## Examples

### Example 1: Basic Usage

```javascript
xhr.open('GET', '/log?msg=data', false);
xhr.send();
```

### Example 2: Advanced Usage

```javascript
xhr.setRequestHeader('X-Google-Metadata-Request', 'True');
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unusual XHR requests in browser logs
- Detect metadata endpoint access

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Flask]]
- [[tools/flask_cors]]

## References

- https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
- MDN Web Docs
