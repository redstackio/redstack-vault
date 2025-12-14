---
url: 'https://github.com/rails/jquery-ujs'
tags:
  - javascript
  - ajax
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.689Z'
id: 97908f57-e587-40fc-8e43-a9e3d3db3b9f
validated: true
submitted: true
---
# jQuery-ujs

**Status**: Unverified

## Overview

jQuery-ujs is a JavaScript library that provides unobtrusive AJAX support for Rails applications, handling data-* attributes to enable remote requests on events like clicks.

## Description

In offensive security, it can be leveraged in XSS payloads where injected attributes (e.g., data-remote=true) trigger AJAX calls or eval scripts, bypassing restrictions when combined with unsanitized rendering.

## Features

- Feature 1: Binds events to data attributes for AJAX
- Feature 2: Supports globalEval for dynamic script execution
- Feature 3: Integrates with jQuery for client-side interactions

## Installation

### Requirements

- jQuery library

### Install Commands

```bash
# Via CDN or npm
npm install jquery-ujs
```

## Basic Usage

```javascript
// Included via script tag
$("a[data-remote]").on("click", function() { /* AJAX */ });
```

### Common Options

| Option | Description |
|--------|-------------|
| data-remote | Enables AJAX on link clicks |
| data-type | Specifies response type, e.g., script |

## Examples

### Example 1: Basic Usage

HTML with attributes:

```html
<a href="/action" data-remote="true" data-type="script">Click</a>
```

### Example 2: Advanced Usage

Triggers eval on script responses.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Look for data-* attributes in rendered HTML
- Monitor for unexpected AJAX requests from UI elements

## Related Procedures


## Related Tools

- [[tools/SwaggerUIBundle]]

## References

- Official documentation: https://github.com/rails/jquery-ujs
- Related resources: XSS exploitation guides
