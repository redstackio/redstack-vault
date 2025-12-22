---
url: 'https://github.com/basecamp/trix'
tags:
  - editor
  - xss
type: tool
verified: false
platforms:
  - Web
  - Electron
id: 476ed8bb-8ccd-47b6-9f86-bea01129423f
created_at: '2025-12-13T23:55:06.737Z'
updated_at: '2025-12-13T23:55:06.737Z'
validated: true
submitted: true
---
# Trix-Editor

**Status**: Unverified

## Overview

Trix is a rich text editor used in Basecamp, vulnerable to mutation-based XSS in v2.1.8.

## Description

Open-source editor for HTML5 content, integrates with Electron apps like Basecamp Desktop. Vulnerable to copy-paste bypasses via MathML mutations.

## Features

- Feature 1: WYSIWYG editing
- Feature 2: Attachment handling (data-trix-attachment)
- Feature 3: Sanitization via DOMPurify

## Installation

### Requirements

- Node.js

### Install Commands

```bash
git clone https://github.com/basecamp/trix
cd trix
npm install
```

## Basic Usage

```bash
trix --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |

## Examples

### Example 1: Basic Usage

Embed in HTML: <trix-editor></trix-editor>

### Example 2: Advanced Usage

Configure sanitizer: trix.config.sanitizer = DOMPurify.sanitize

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

- Monitor for unsanitized MathML in editor content
- Patch to latest version

## Related Procedures

- [[procedures/Craft-XSS-Payload-HTML-for-Trix-Editor]]

## Related Tools

- [[tools/DOMPurify]]

## References

- https://github.com/basecamp/trix
