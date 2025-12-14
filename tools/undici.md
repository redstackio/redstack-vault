---
id: tool-uuid-1
url: 'https://github.com/nodejs/undici'
tags:
  - http-client
  - node-js
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.598Z'
validated: true
submitted: true
---
# undici

**Status**: Unverified

## Overview

Undici is a fast and lightweight HTTP/1.1 client library for Node.js, designed as an alternative to the built-in http/https modules, with support for modern features like async/await and connection pooling. Commonly used in security testing to demonstrate client-side vulnerabilities such as header handling flaws during redirects.

## Description

Undici provides a standards-compliant HTTP client with features like automatic redirects (configurable via maxRedirections), origin enforcement, and custom headers. In offensive security, it's used to replicate real-world client behaviors in PoCs for issues like the Proxy-Authorization header leakage on cross-origin redirects (vulnerable up to v6.7.0). Alternatives include the native fetch() API or got library.

## Features

- Feature 1: Async request handling with Promise-based API
- Feature 2: Configurable redirect following and header management
- Feature 3: Connection pooling for efficient multiple requests

## Installation

### Requirements

- Node.js 14+
- npm or yarn

### Install Commands

```bash
npm install undici
```

## Basic Usage

```bash
node -e "const {request} = require('undici'); request('http://example.com').then(console.log);"
```

### Common Options

| Option | Description |
|--------|-------------|
| `maxRedirections` | Number of redirects to follow (default: 0) |
| `headers` | Object of request headers |
| `origin` | Enforce request origin for security

## Examples

### Example 1: Basic Usage

```javascript
const { request } = require('undici');
request('http://example.com');
```

### Example 2: Advanced Usage

```javascript
request({
  origin: 'http://localhost/',
  pathname: '/',
  method: 'GET',
  headers: { 'Proxy-Authorization': 'secret' },
  maxRedirections: 1
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of undici in package.json or node_modules
- Network logs showing HTTP requests from Node.js with undici User-Agent
- Anomalous header patterns in proxy logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[fetch API]]
- [[axios]]

## References

- Official documentation: https://undici.nodejs.org/
- Vulnerability report: https://hackerone.com/reports/2451113
