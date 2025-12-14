---
id: tool-uuid-2
url: 'https://developer.apple.com/documentation/webkit'
tags:
  - devtools
  - javascript
type: tool
verified: false
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.641Z'
validated: true
submitted: true
---
# Safari-JavaScript-Console

**Status**: Unverified

## Overview

The JavaScript Console in Safari's Web Inspector is a built-in REPL for executing JS on loaded pages, crucial for injecting payloads like CSRF forms during web exploitation.

## Description

Part of Safari DevTools, it allows real-time code execution, DOM manipulation, and network monitoring, ideal for testing browser-specific vulnerabilities like the CSRF bypass here.

## Features

- Feature 1: Live JS evaluation on current page
- Feature 2: Error debugging and logging
- Feature 3: Integration with Elements and Network panels

## Installation

### Requirements

- Safari with Develop menu enabled

### Install Commands

No separate install; enable via UI.

```bash
# Enable: Safari Preferences > Advanced > Show Develop menu
```

## Basic Usage

Open via Develop > Show Web Inspector > Console tab.

### Common Options

| Option | Description |
|--------|-------------|
| Clear | Clear console output |
| Preserve Log | Keep logs across navigations |

## Examples

### Example 1: Basic Usage

Execute simple JS: `console.log('Test');`

### Example 2: Advanced Usage

Inject form: Paste multi-line JS for DOM append.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Console API calls in client logs
- Unusual JS execution patterns

## Related Procedures


## Related Tools

- [[Chrome DevTools]]

## References

- Official documentation: https://developer.apple.com/documentation/webkit/wkwebinspector
- Related resources: https://stackoverflow.com/questions/40234993/how-to-inspect-element-using-safari-browser
