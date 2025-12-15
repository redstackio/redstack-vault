---
url: 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'
tags:
  - javascript-library
  - ajax
type: tool
verified: false
platforms:
  - Web
id: 0eeadca0-dbe1-4167-809a-cb930cde2034
created_at: '2025-12-14T17:33:34.367Z'
updated_at: '2025-12-14T17:33:34.367Z'
validated: true
submitted: true
---
# jQuery-for-Cross-Domain-AJAX

**Status**: Unverified

## Overview

jQuery is a fast, small JavaScript library that simplifies HTML document traversal, event handling, and AJAX interactions, commonly used in web attacks for cross-domain requests with credentials.

## Description

In offensive security, jQuery enables easy POST requests to set cookies across domains by configuring xhrFields for credentials and crossDomain flags, bypassing some browser restrictions in legacy contexts.

## Features

- Feature 1: Simplified AJAX with $.ajax() for credentialed cross-origin requests
- Feature 2: Chainable methods for quick payload delivery
- Feature 3: Compatible with older browsers for broad attack surface

## Installation

### Requirements

- HTML page to embed the script tag

### Install Commands

No installation; load via CDN:
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
```

## Basic Usage

```javascript
$.ajax({ url: 'target', type: 'POST', data: {key: 'value'} });
```

### Common Options

| Option | Description |
|--------|-------------|
| `xhrFields: {withCredentials: true}` | Include cookies in cross-domain requests |
| `crossDomain: true` | Enable CORS handling |
| `async: false` | Synchronous execution for sequencing |

## Examples

### Example 1: Basic Usage

```javascript
$.post('https://target.com/endpoint', {name: 'value'});
```

### Example 2: Advanced Usage

```javascript
$.ajax({
  url: 'https://gnar.grammarly.com/cookies',
  type: 'POST',
  data: {name: 'gnar_containerId', value: 'payload'},
  xhrFields: {withCredentials: true},
  crossDomain: true,
  async: false
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing AJAX POSTs from third-party domains
- Browser console errors for cross-domain credential attempts

## Related Procedures

- [[procedures/Set-Malicious-gnar_containerId-Cookie-via-POST-Endpoint]]

## Related Tools

- [[tools/XMLHttpRequest-for-Credentialed-Requests]]

## References

- Official documentation: https://jquery.com/
