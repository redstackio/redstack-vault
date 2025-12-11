---
url: ''
tags:
  - browser
  - javascript
  - devtools
type: tool
platforms:
  - Web
description: >-
  Built-in developer tool in web browsers for executing JavaScript and
  inspecting network activity.
id: 6ec311d9-0d8d-44b7-9167-d76981eb882e
created_at: '2025-12-11T03:47:59.472Z'
updated_at: '2025-12-11T03:47:59.472Z'
verified: false
validated: true
submitted: true
---
# Browser Console

**Status**: Unverified

## Overview

The browser console allows execution of JavaScript code in the context of a web page, used in web exploits for API calls and manipulation.

## Description

Part of developer tools in browsers like Chrome or Firefox, enabling fetch requests, DOM manipulation, and debugging for client-side attacks.

## Features

- JavaScript execution
- Network inspection
- Console logging

## Installation

### Requirements

- Modern web browser

### Install Commands

Built-in, no installation needed.

## Basic Usage

Press F12 or Ctrl+Shift+J to open.

### Common Options

N/A (UI-based).

## Examples

### Example 1: Basic Usage

Execute fetch() in console.

### Example 2: Advanced Usage

Craft and send POST requests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Information Repositories]]
- [[JavaScript]]

### Tactics

- [[Persistence]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Client-side script execution logs (if monitored)
- Anomalous API requests

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Flask]]
- #ngrok

## References

- Browser documentation (e.g., Chrome DevTools)
