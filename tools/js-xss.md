---
url: 'https://github.com/leizongmin/js-xss'
tags:
  - sanitization
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.117Z'
id: 72f63281-a4fb-47af-8496-78e503e39683
validated: true
submitted: true
---
# js-xss

**Status**: Unverified

## Overview

js-xss is a JavaScript HTML sanitization library designed to prevent XSS by stripping dangerous tags and attributes.

## Description

Used by Judge.me for email template sanitization, but a custom onIgnoreTag for IE comments allows bypass via parsing differences, enabling payload injection.

## Features

- Feature 1: Configurable tag/attr whitelisting
- Feature 2: Custom callbacks like onIgnoreTag
- Feature 3: XSS filtering for user input

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install xss
```

## Basic Usage

```javascript
const xss = require('xss');
const clean = xss('<script>alert(1)</script>');
```

### Common Options

| Option | Description |
|--------|-------------|
| onIgnoreTag | Custom handler for ignored tags |
| whiteList | Allowed tags/attrs |

## Examples

### Example 1: Basic Usage

```javascript
const options = { onIgnoreTag: customFunc };
const filter = new xss.FilterXSS(options);
```

### Example 2: Advanced Usage

Configure for comments: return t for specific e/t without filtering.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Collection]]

## Detection

- Review app code for custom sanitization configs
- Test inputs for bypasses

## Related Procedures

- [[procedures/Inject-XSS-Payload-into-Email-Template]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- GitHub repo: https://github.com/leizongmin/js-xss
