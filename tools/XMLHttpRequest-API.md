---
id: tool-uuid-1
name: XMLHttpRequest-API
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.172Z'
platforms:
  - Web
tags:
  - browser
  - api
  - http
url: 'https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest'
validated: true
submitted: true
---

# XMLHttpRequest-API

**Status**: Unverified

## Overview

XMLHttpRequest is a built-in browser API for making asynchronous HTTP requests, commonly used in web applications and security testing to simulate cross-origin fetches, especially in exploits like CORS misconfigurations.

## Description

This API allows JavaScript to send HTTP requests to servers, including cross-origin ones if permitted by CORS. In offensive security, it's used to test and exploit web vulnerabilities by including credentials (withCredentials=true) to steal data from authenticated sessions.

## Features

- Feature 1: Asynchronous request handling with onload/onerror events
- Feature 2: Support for credentials in cross-origin requests
- Feature 3: Method flexibility (GET, POST, etc.) with custom headers

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, etc.)
- No installation needed; native JavaScript API

### Install Commands

```bash
# No installation; use in browser console or HTML script
console.log(new XMLHttpRequest());
```

## Basic Usage

```javascript
new XMLHttpRequest(); // Instantiate
```

### Common Options

| Option | Description |
|--------|-------------|
| open(method, url, async) | Initialize request with method, URL, and async flag |
| setRequestHeader(name, value) | Set custom headers like Origin |
| withCredentials | Boolean to include cookies in CORS requests |
| send(body) | Send the request (body optional for GET) |

## Examples

### Example 1: Basic Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://example.com/api', true);
xhr.send();
```

### Example 2: Advanced Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://target.com/api', true);
xhr.withCredentials = true;
xhr.onload = function() { console.log(this.responseText); };
xhr.send();
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Browser network logs showing unexpected cross-origin requests with credentials
- Detection method 2: Server logs for requests from untrusted Origins

## Related Procedures

- [[procedures/Exploit-CORS-via-JavaScript-to-Steal-User-Data]]

## Related Tools

- [[Fetch-API]]
- [[cURL]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
- Related resources: OWASP CORS Cheat Sheet
