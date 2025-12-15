---
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API'
tags:
  - http-client
  - javascript
type: tool
platforms:
  - Web
description: >-
  Native JavaScript API for making HTTP requests in browsers, used for
  cross-origin testing and vulnerability exploitation.
id: 14545159-9537-4b66-8b69-d3c4f76e1242
created_at: '2025-12-14T17:32:48.567Z'
updated_at: '2025-12-14T17:32:48.567Z'
verified: false
validated: true
submitted: true
---
# Fetch-API

**Status**: Unverified

## Overview

The Fetch API is a modern JavaScript interface for fetching resources across the network, replacing XMLHttpRequest. It's ideal for security testing of web APIs, enabling cross-origin requests to probe CORS policies, headers, and caching behaviors without server-side code.

## Description

Built into browsers, Fetch supports promises for async requests and allows inspection of response headers like ACAO. In offensive security, it's used to send custom Origin headers (browser-enforced) to endpoints like WP-JSON, triggering echoes and cache poisoning for DoS attacks.

## Features

- Feature 1: Promise-based async HTTP requests
- Feature 2: Access to full response objects, including headers
- Feature 3: CORS mode control (e.g., 'cors' for cross-origin)

## Installation

### Requirements

- Browser supporting ES6+ (all modern browsers)

### Install Commands

No installation; native.

## Basic Usage

```javascript
fetch('https://example.com').then(r => r.text()).then(t => console.log(t));
```

### Common Options

| Option | Description |
|--------|-------------|
| mode: 'cors' | Enforce CORS checks |
| credentials: 'include' | Send cookies if needed |
| headers | Custom request headers |

## Examples

### Example 1: Basic Usage

```javascript
fetch('https://api.example.com/data');
```

### Example 2: Advanced Usage

```javascript
fetch('https://target.com/wp-json/?test', {method: 'GET'}).then(r => {
  console.log(r.headers.get('Access-Control-Allow-Origin'));
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser network logs showing Fetch-initiated requests
- CORS preflight OPTIONS requests

## Related Procedures

- [[procedures/Verify-DoS-via-Poisoned-CORS-Response]]

## Related Tools

- [[tools/Browser-JavaScript-Console]]

## References

- MDN: Fetch API Documentation
