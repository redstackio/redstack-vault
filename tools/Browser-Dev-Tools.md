---
url: ''
tags:
  - debugging
  - inspection
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.323Z'
id: 5403a6fa-9ffa-4976-a436-31243b6b0ead
validated: true
submitted: true
---
# Browser Dev Tools

**Status**: Unverified

## Overview

Built-in browser developer tools (e.g., Chrome DevTools) for inspecting elements, console logging, and setting cookies, used to discover XSS by observing unescaped 'guvo' reflections in window objects.

## Description

Tools include Console for JS execution, Application tab for cookie management, and Network for request inspection. Here, used to set test cookies and verify injection into window.ySitRepParams/window.yelp.guv.

## Features

- Feature 1: Console for running JS and logging
- Feature 2: Storage inspector for cookies/localStorage
- Feature 3: Elements panel for DOM inspection

## Installation

### Requirements

- Modern browser (Chrome, Firefox)

### Install Commands

```bash
# Built-in; press F12 or Ctrl+Shift+I
```

## Basic Usage

```javascript
# In console: document.cookie = 'guvo=test'; console.log(window.yelp.guv);
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open dev tools |
| Console | JS REPL |

## Examples

### Example 1: Basic Usage

Set cookie: document.cookie = 'guvo=<script>alert(1)</script>'; reload page.

### Example 2: Advanced Usage

Inspect Network for Set-Cookie headers after canary URL.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Client-side; detect via anomalous JS in console

## Related Procedures

- [[procedures/Discover-Reflected-XSS-in-Cookie-Reflection]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: MDN Web Docs
