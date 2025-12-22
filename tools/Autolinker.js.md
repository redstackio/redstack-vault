---
id: tool-autolinker-001
url: 'https://github.com/gregjacobs/Autolinker.js'
tags:
  - javascript
  - linking
  - xss
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.606Z'
validated: true
submitted: true
---
# Autolinker.js

**Status**: Unverified

## Overview

A JavaScript library for automatically parsing text input and converting URLs, emails, etc., into clickable HTML anchors; underlying dependency for react-autolinker-wrapper, contributing to XSS when used without sanitization.

## Description

Autolinker.js scans text and wraps matches in <a> tags. When output is set via innerHTML without escaping, it allows script injection. Used in web apps for dynamic linking; fixed in later versions with sanitizeHtml option.

## Features

- Feature 1: Links URLs, emails, mentions, and phones
- Feature 2: Customizable matchers and HTML attributes
- Feature 3: Replace mode for text substitution

## Installation

### Requirements

- JavaScript environment (browser or Node)

### Install Commands

```bash
npm install autolinker
```

## Basic Usage

```javascript
const linked = Autolinker.link("Visit https://example.com");
```

### Common Options

| Option | Description |
|--------|-------------|
| newTab | Open links in new tab |
| sanitizeHtml | Enable sanitization (post-vuln fix) |

## Examples

### Example 1: Basic Usage

```javascript
Autolinker.link("https://example.com");
// Output: <a href="https://example.com">https://example.com</a>
```

### Example 2: Advanced Usage

```javascript
Autolinker.link("Email: test@example.com", {email: true});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Autolinker.link calls in source code
- Unsanitized innerHTML with linked text
- Dependency in package-lock.json

## Related Procedures

- [[procedures/Trigger-XSS-with-Malicious-Input]]

## Related Tools

- [[tools/react-autolinker-wrapper]]

## References

- GitHub: https://github.com/gregjacobs/Autolinker.js
