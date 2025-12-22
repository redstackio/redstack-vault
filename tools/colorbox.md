---
id: tool-003
url: 'http://www.jacklmoore.com/colorbox/'
tags:
  - javascript-plugin
  - xss-vector
type: tool
verified: false
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.287Z'
validated: true
submitted: true
---
# colorbox

**Status**: Unverified

## Overview

Colorbox is a jQuery-based lightbox plugin for displaying images, inline HTML, and AJAX content, exploited here as a vector for loading external scripts in XSS attacks.

## Description

It inserts fetched content into the DOM without sanitization, allowing arbitrary JS execution when triggered by user clicks on injected links.

## Features

- Feature 1: AJAX content loading
- Feature 2: Inline HTML insertion
- Feature 3: Cross-browser compatibility

## Installation

### Requirements

- jQuery library

### Install Commands

```bash
# Download from official site or CDN
# Include in HTML: <script src="jquery.colorbox.js"></script>
```

## Basic Usage

```javascript
$("a.colorbox").colorbox({href: "/path"});
```

### Common Options

| Option | Description |
|--------|-------------|
| `href` | URL to load |
| `class` | CSS class for triggering |
| `onComplete` | Callback after load |

## Examples

### Example 1: Basic Usage

```html
<a href="/external" class="colorbox">Click</a>
```

### Example 2: Advanced Usage

```javascript
$(".colorbox").colorbox({iframe: true, width: "80%"});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of colorbox.js in site source
- Outbound AJAX requests from plugin

## Related Procedures

- [[procedures/Craft-Malicious-Search-URL-for-Colorbox-Exploitation]]
- [[procedures/Trigger-XSS-Execution-via-User-Interaction]]

## Related Tools

- [[tools/jquery]]

## References

- Official documentation: http://www.jacklmoore.com/colorbox/
