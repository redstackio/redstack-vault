---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
name: Browser-Network-Inspector
type: tool
verified: false
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.525Z'
platforms:
  - Web
tags:
  - inspection
  - browser
url: 'https://developer.chrome.com/docs/devtools/network/'
validated: true
submitted: true
---

# Browser-Network-Inspector

**Status**: Unverified

## Overview

Built-in developer tool in modern web browsers (e.g., Chrome DevTools, Firefox Developer Tools) for inspecting network requests and responses during web page loading.

## Description

This tool captures HTTP/HTTPS traffic, allowing users to filter by resource type (e.g., JS files), view headers, and download contents. Commonly used in offensive security for identifying exposed resources on web applications.

## Features

- Feature 1: Real-time network request logging
- Feature 2: Filtering by type (XHR, JS, CSS)
- Feature 3: Response body preview and download

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, Edge)

### Install Commands

No installation needed; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# No CLI; browser-based
```

### Common Options

| Option | Description |
|--------|-------------|
| Network Tab | View requests |
| Filter: JS | Show JavaScript files only |

## Examples

### Example 1: Basic Usage

Load a page and open Network tab to see all requests.

### Example 2: Advanced Usage

Filter for JS, select file, and preview response.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser developer tools are client-side and hard to detect
- Monitor for unusual resource access from known IPs

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/network/
- Related resources: Browser dev tools guides
