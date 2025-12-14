---
url: 'https://github.com/summernote/summernote'
tags:
  - wysiwyg
  - javascript
  - vulnerable
type: tool
platforms:
  - Web
description: >-
  A JavaScript WYSIWYG editor library with a known vulnerability allowing stored
  XSS via unsafe link insertion.
id: 9af0427d-9815-4d44-abc5-914f6ff7df74
created_at: '2025-12-13T23:55:20.619Z'
updated_at: '2025-12-13T23:55:20.619Z'
verified: false
validated: true
submitted: true
---
# Summernote-JS

**Status**: Unverified

## Overview

Summernote JS is a simple WYSIWYG editor for web applications, often used in content management systems like email template editors. In this context, it's the vulnerable component in Judge.me that enables stored XSS by failing to sanitize javascript: URIs in links.

## Description

Summernote provides a Bootstrap-compatible editor with features like formatting, media insertion, and link creation. The bug (pre-patch versions) allows arbitrary JavaScript execution when links with javascript: protocols are inserted and saved, persisting in HTTP responses without escaping. It's commonly integrated into apps like Shopify plugins for user-generated content.

## Features

- Feature 1: Rich text editing with toolbar for bold, italic, links
- Feature 2: Media embed and code view for HTML manipulation
- Feature 3: Plugin support, but vulnerable to unsafe data handling in core link insertion

## Installation

### Requirements

- Node.js and npm for development integration
- Compatible with Bootstrap 3/4

### Install Commands

```bash
# Via npm
npm install summernote

# Or CDN for quick integration
# <link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.css" rel="stylesheet">
# <script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.js"></script>
```

## Basic Usage

```bash
tool-name --help
```

No CLI; it's a client-side JS library. Initialize in HTML:

```javascript
$('#editor').summernote();
```

### Common Options

| Option | Description |
|--------|-------------|
| `height` | Set editor height (e.g., 300px) |
| `callbacks.onChange` | Hook for content changes |
| `toolbar` | Customize buttons, e.g., include/disable link tool |

## Examples

### Example 1: Basic Usage

Embed in a form:

```html
<div id="summernote"></div>
<script>
  $('#summernote').summernote({ height: 200 });
</script>
```

### Example 2: Advanced Usage

With link callback to attempt sanitization:

```javascript
$('#summernote').summernote({
  callbacks: {
    onCreateLink: function(link) {
      if (link.indexOf('javascript:') === 0) {
        alert('Unsafe link blocked');
        return false;
      }
    }
  }
});
```

## Expected Output

Editor renders with toolbar; content saved as HTML. Vulnerable versions output unsanitized <a href="javascript:alert(1)">link</a>.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Scan web app source for summernote.min.js includes
- Monitor for javascript: links in stored content
- Use vulnerability scanners like OWASP ZAP to test link insertion

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[CKEditor]]
- [[TinyMCE]]

## References

- Official documentation: https://summernote.org/
- Vulnerability details: https://hackerone.com/reports/1376672
