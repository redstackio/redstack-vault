---
url: 'https://jquery.com/'
tags:
  - javascript
  - dom-manipulation
type: tool
platforms:
  - Web
description: >-
  Fast, small JavaScript library for HTML traversal and manipulation, used in
  GitLab for injecting loaded content.
id: 2696f62d-e126-455e-bc4a-b757ad244938
created_at: '2025-12-14T00:11:16.613Z'
updated_at: '2025-12-14T00:11:16.613Z'
verified: false
validated: true
submitted: true
---
# jQuery

**Status**: Unverified

## Overview

jQuery simplifies HTML document traversal, event handling, and Ajax interactions.

## Description

In GitLab, it's used to parse and inject HTML from loaded JSON, facilitating CSP bypass by executing injected scripts.

## Features

- DOM manipulation
- Event handling
- Ajax requests

## Installation

### Requirements

- Browser environment

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
| `$.get` | Ajax GET |

## Examples

### Example 1: Basic Usage

```javascript
$('body').append('<div>');
```

### Example 2: Advanced Usage

```javascript
$.parseHTML(json.html).appendTo('#element');
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for jQuery-based injections in console
- Detect unexpected HTML appends

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
- [[tools/Axios]]

## References

- https://api.jquery.com/
