---
url: ''
tags:
  - javascript
  - dom
type: tool
platforms:
  - Web
description: >-
  JavaScript library for HTML traversal and manipulation, used in GitLab for
  injecting HTML from JSON
id: dce55d55-d802-439a-8d50-a4d493ba1ef3
created_at: '2025-12-11T03:47:56.417Z'
updated_at: '2025-12-11T03:47:56.417Z'
verified: false
validated: true
submitted: true
---
# jQuery

**Status**: Unverified

## Overview

jQuery is a fast, small JavaScript library for simplifying HTML document traversal, event handling, and animation.

## Description

In GitLab, jQuery parses and injects HTML from loaded JSON, enabling CSP bypass by allowing script injection without violating policy.

## Features

- DOM manipulation: Easy element selection and modification
- Event handling: Bind events to elements
- AJAX support: Asynchronous requests

## Installation

### Requirements

- Web browser or Node.js

### Install Commands

```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

## Basic Usage

```javascript
$(document).ready(function() {});
```

### Common Options

| Option | Description |
|--------|-------------|
| `selector` | CSS selector |

## Examples

### Example 1: Basic Usage

```javascript
$('body').html('<p>Hello</p>');
```

### Example 2: Advanced Usage

```javascript
$.getJSON('/url', function(data) { $('body').append(data.html); });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Inspect DOM for dynamic injections
- Monitor for jQuery-related CSP violations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nokogiri]]
- #axios

## References

- Official jQuery documentation: https://jquery.com/
