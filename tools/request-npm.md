---
url: 'https://www.npmjs.com/package/request'
tags:
  - http-client
  - npm
type: tool
platforms:
  - Node.js
description: >-
  HTTP client library for Node.js used in portScanner.js to send POST requests
  to jsreport API.
id: 3bcf2f29-9602-4283-8104-a852b16bf1a7
created_at: '2025-12-14T17:23:24.903Z'
updated_at: '2025-12-14T17:23:24.903Z'
verified: false
validated: true
submitted: true
---
# request

**Status**: Unverified

## Overview

The 'request' module facilitates sending form data POSTs for SSRF template rendering in the scanning script.

## Description

Simplified HTTP request library for Node.js, wrapped in Promises for async port scanning operations.

## Features

- Feature 1: Form data encoding
- Feature 2: JSON handling
- Feature 3: Error response parsing

## Installation

### Requirements

- Node.js installed

### Install Commands

```bash
npm install request
```

## Basic Usage

```bash
node -e "require('request').post('url', {form: {key: 'value'}}, cb);"
```

### Common Options

| Option | Description |
|--------|-------------|
| `form` | Data for POST |
| `url` | Target endpoint |

## Examples

### Example 1: Basic Usage

```javascript
const request = require('request');
request.post('http://localhost/api/report', {form: {template: html}}, (err, res) => {});
```

### Example 2: Advanced Usage

```javascript
request.post({url: '/api', formData: {content: '<img src=...>'}}, cb);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Tactics

- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- NPM logs for installation
- HTTP traffic patterns from Node.js

## Related Procedures

- [[procedures/discover-script-manager-port-via-ssrf]]

## Related Tools

- [[tools/axios]]
- [[tools/node-fetch]]

## References

- NPM page: https://www.npmjs.com/package/request
