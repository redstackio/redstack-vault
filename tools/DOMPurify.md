---
id: tool-uuid-001
name: DOMPurify
type: tool
verified: false
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.352Z'
platforms:
  - Web
tags:
  - sanitizer
  - xss-prevention
url: 'https://cure53.de/purify'
validated: true
submitted: true
---

# DOMPurify

**Status**: Unverified

## Overview

DOMPurify is a fast and secure DOM-only XSS sanitizer for HTML, MathML, and SVG, commonly used in web applications to prevent cross-site scripting by stripping malicious code while preserving safe content. In security testing, it's referenced for understanding and bypassing sanitization weaknesses, such as in SVG animate attributes.

## Description

DOMPurify parses and cleans HTML/SVG inputs using a whitelist approach, configurable via hooks and options. In offensive security, testers use it to simulate defenses and craft bypass payloads, like those exploiting xlink:href animations in SVGs. It's JavaScript-based, integrates easily into browsers or Node.js, and is maintained by Cure53.

## Features

- Feature 1: DOM-based sanitization without string manipulation
- Feature 2: Support for SVG and MathML with customizable allowlists
- Feature 3: Hooks for pre- and post-sanitization modifications

## Installation

### Requirements

- JavaScript environment (browser or Node.js)

### Install Commands

```bash
# Via npm for Node.js
npm install dompurify

# Or include via CDN in HTML
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.6/dist/purify.min.js"></script>
```

## Basic Usage

```javascript
dompurify.sanitize('<svg><script>alert(1)</script></svg>');
```

### Common Options

| Option | Description |
|--------|-------------|
| `ALLOW_DATA_ATTR` | Allow data attributes (default: false) |
| `FORBID_TAGS` | Explicitly forbid certain tags like 'svg' |

## Examples

### Example 1: Basic Usage

```javascript
var clean = DOMPurify.sanitize(dirtyHTML);
console.log(clean); // Malicious code removed
```

### Example 2: Advanced Usage

```javascript
DOMPurify.addHook('uponSanitizeElement', function(node, data) {
  if (node.tagName === 'A') {
    // Custom hook for xlink:href
    data.forceRemove.push('xlink:href');
  }
});
var cleanSVG = DOMPurify.sanitize(svgPayload, { ADD_TAGS: ['animate'] });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of DOMPurify script in page source
- Logs showing sanitization hooks or whitelist checks

## Related Procedures


## Related Tools

- [[tools/Sanitizer-Test-Frameworks]]

## References

- Official documentation: https://github.com/cure53/DOMPurify
- Related resources: Cure53 research on SVG bypasses
