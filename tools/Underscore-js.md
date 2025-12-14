---
id: tool-underscore-js
url: 'http://underscorejs.org/#template'
tags:
  - javascript
  - template-engine
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.051Z'
validated: true
submitted: true
---
# Underscore-js

**Status**: Unverified

## Overview

Underscore.js is a JavaScript library providing utility functions, including a template engine for dynamic HTML generation, often used in web applications like Mapbox embeds for interpolating data into pages.

## Description

The template function uses syntax like '<%=' for unescaped output and '<%-' for escaped, making it prone to XSS if unescaped interpolation is used on user-controlled inputs like query parameters.

## Features

- Feature 1: Template interpolation with escaping options
- Feature 2: Utility functions for arrays/objects
- Feature 3: Lightweight and modular

## Installation

### Requirements

- Node.js or browser environment

### Install Commands

```bash
# Via npm
npm install underscore

# Via CDN in HTML
<script src="https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.6/underscore-min.js"></script>
```

## Basic Usage

```javascript
_.template("Hello: <%= name %>")({name: "World"});
```

### Common Options

| Option | Description |
|--------|-------------|
| `<%=' | Unescaped interpolation (vulnerable) |
| `<%-' | HTML-escaped interpolation (safe) |

## Examples

### Example 1: Basic Usage

```javascript
var template = _.template("<meta name=\"token\" content=\"<%= token %>\">");
template({token: "test"});
```

### Example 2: Advanced Usage

```javascript
var safeTemplate = _.template("<meta name=\"token\" content=\"<%- token %>\">");
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Script tags loading underscore.js in page source
- Template syntax in JS files

## Related Procedures


## Related Tools

- [[tools/Lodash]]

## References

- Official documentation: http://underscorejs.org/#template
- Related resources: OWASP XSS Prevention Cheat Sheet
