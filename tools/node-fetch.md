---
url: 'https://www.npmjs.com/package/node-fetch'
tags:
  - http-client
  - api-testing
type: tool
platforms:
  - Web
  - Node.js
description: Lightweight HTTP client for Node.js to make requests like POST to APIs.
id: f86a5f48-5f22-44ba-9131-dd00cda6678e
created_at: '2025-12-14T17:28:36.431Z'
updated_at: '2025-12-14T17:28:36.431Z'
verified: false
validated: true
submitted: true
---
# node-fetch

**Status**: Unverified

## Overview

node-fetch is a Node.js library that brings the Fetch API to server-side environments, ideal for simulating API requests in security testing, such as exploiting vulnerabilities in web APIs like TikTok's.

## Description

It allows sending HTTP requests with custom headers, methods, and JSON bodies, mimicking browser behavior. Commonly used in offensive security for API abuse, parameter testing, and data exfiltration without a full browser.

## Features

- Feature 1: Supports all HTTP methods (GET, POST, etc.)
- Feature 2: Handles JSON serialization/deserialization
- Feature 3: Promise-based for async operations

## Installation

### Requirements

- Node.js >= 10

### Install Commands

```bash
npm install node-fetch
```

## Basic Usage

```javascript
const fetch = require('node-fetch');
fetch('https://example.com').then(res => res.text()).then(body => console.log(body));
```

### Common Options

| Option | Description |
|--------|-------------|
| method | HTTP method (e.g., 'POST') |
| headers | Request headers object |
| body | Request body (string/Buffer) |

## Examples

### Example 1: Basic Usage

```javascript
fetch('https://api.example.com', {method: 'GET'}).then(res => res.json()).then(data => console.log(data));
```

### Example 2: Advanced Usage

```javascript
fetch(url, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(postData)}).then(...);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Node.js User-Agent or fetch patterns
- API access from non-browser clients

## Related Procedures


## Related Tools

- [[axios]]
- [[curl]]

## References

- Official documentation: https://www.npmjs.com/package/node-fetch
