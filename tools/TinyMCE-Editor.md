---
id: tool-tinymce-editor
url: 'https://www.tiny.cloud/'
tags:
  - editor
  - xss
  - html
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.573Z'
validated: true
submitted: true
---
# TinyMCE-Editor

**Status**: Unverified

## Overview

TinyMCE is a rich text editor used in Concrete CMS for handling comment input. In Rich Text mode with Source enabled, it allows raw HTML insertion, facilitating Stored XSS by not sanitizing <script> tags.

## Description

TinyMCE provides WYSIWYG editing but exposes a Source view for direct HTML manipulation. In vulnerable configurations like Concrete CMS Conversations, this leads to unsanitized storage. Commonly used in web apps for user-generated content.

## Features

- Feature 1: WYSIWYG visual editing with toolbar
- Feature 2: Source code mode for raw HTML/JS input
- Feature 3: Plugin support for advanced formatting

## Installation

### Requirements

- JavaScript-enabled browser
- Integration into CMS like Concrete

### Install Commands

```bash
# Typically bundled in CMS; for standalone:
npm install tinymce
```

## Basic Usage

```javascript
tinymce.init({
  selector: '#comment',
  plugins: 'code',
  toolbar: 'code'
});
```

### Common Options

| Option | Description |
|--------|-------------|
| plugins: 'code' | Enables Source button |
| toolbar: 'code' | Adds Source to toolbar |
| selector | Targets the input element |

## Examples

### Example 1: Basic Usage

Enable in form:

```javascript
tinymce.init({ selector: 'textarea' });
```

### Example 2: Advanced Usage

With Source mode:

```javascript
tinymce.init({
  selector: '#mytextarea',
  plugins: 'code',
  toolbar: 'code | bold italic'
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for 'Source' button clicks in session logs
- Scan input for raw HTML patterns
- Detect unsanitized script tags in DB

## Related Procedures


## Related Tools

- [[Related Tool: Concrete CMS]]

## References

- Official documentation: https://www.tiny.cloud/docs/
