---
id: tool-got
url: 'https://www.npmjs.com/package/got'
tags:
  - http-client
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.471Z'
validated: true
submitted: true
---
# got

**Status**: Unverified

## Overview

Got is a lightweight HTTP request client for Node.js, used to fetch HTML pages for scraping in vulnerable applications like those exploiting metascraper XSS.

## Description

It provides a simple, promise-based API for GET/POST requests, faster than alternatives like request. In attacks, it retrieves malicious pages for extraction.

## Features

- Feature 1: Streaming support
- Feature 2: Retry logic
- Feature 3: JSON parsing

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install got
```

## Basic Usage

```bash
got('http://example.com').then(response => console.log(response.body));
```

### Common Options

| Option | Description |
|--------|-------------|
| timeout | Request timeout |
| json | Parse as JSON |
| headers | Custom headers |

## Examples

### Example 1: Basic Usage

```bash
# In script
const { body } = await got('http://127.0.0.1:8080/article.html');
```

### Example 2: Advanced Usage

```bash
got('url', { timeout: 5000 }).json();
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Protocols]] Web Protocols

### Tactics

- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- got module imports
- Outbound HTTP requests
- Error logs from fetches

## Related Procedures


## Related Tools

- [[tools/metascraper]]

## References

- https://github.com/sindresorhus/got
