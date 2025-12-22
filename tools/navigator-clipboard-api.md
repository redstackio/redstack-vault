---
id: tool-clipboard-api
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API'
tags:
  - api
  - clipboard
  - javascript
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.004Z'
validated: true
submitted: true
---
# Navigator Clipboard API

**Status**: Unverified

## Overview

The Clipboard API allows JavaScript to write text to the system clipboard, used here to deliver the self-XSS payload covertly by tricking the user into granting permission.

## Description

In secure contexts (HTTPS), writeText() copies strings. Requires user gesture/permission in browsers like Firefox. Enables payload placement without direct input.

## Features

- Feature 1: writeText() for string copy
- Feature 2: Permission prompt for security
- Feature 3: Promise-based for async handling

## Installation

### Requirements

- Modern browser (Firefox 63+)
- HTTPS page

### Install Commands

```bash
# No install; native JS API
```

## Basic Usage

```javascript
navigator.clipboard.writeText('payload');
```

### Common Options

| Option | Description |
|--------|-------------|
| writeText | Write string | N/A |

## Examples

### Example 1: Basic Usage

```javascript
navigator.clipboard.writeText('test');
```

### Example 2: Advanced Usage

```javascript
navigator.clipboard.writeText(payload).then(() => console.log('Copied'));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Console logs of write attempts
- User permission prompts
- Clipboard content inspection

## Related Procedures

- [[procedures/copy-malicious-payload-to-clipboard]]

## Related Tools

- [[tools/firefox-browser]]

## References

- MDN Web Docs: Clipboard API
- WHATWG Clipboard API Spec
