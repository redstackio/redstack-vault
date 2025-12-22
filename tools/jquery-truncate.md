---
id: tool-jquery-truncate
url: 'https://github.com/Hacker0x01/truncate/blob/master/jquery.truncate.js'
tags:
  - javascript
  - library
  - vulnerable
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:04.010Z'
validated: true
submitted: true
---
# jquery-truncate

**Status**: Unverified

## Overview

jQuery.truncate is a JavaScript plugin for truncating text in HTML elements, but it can be misused when applied to unsanitized user input, leading to HTML parsing and potential XSS vulnerabilities.

## Description

This library appends ellipsis to overflowing text but uses DOM manipulation that interprets HTML, allowing injected tags and scripts to execute if input isn't escaped. In the HackerOne case, it was applied to asset identifiers, enabling stored XSS. Commonly used in web apps for UI text limiting, but requires careful input handling in security contexts.

## Features

- Feature 1: Automatic text truncation with ellipsis in specified containers
- Feature 2: Configurable max length and padding
- Feature 3: Handles HTML elements but parses content dangerously

## Installation

### Requirements

- jQuery library (v1.0+)
- Web environment with script inclusion

### Install Commands

```bash
# Download from GitHub or include via CDN
# No npm; manual script tag: <script src="path/to/jquery.truncate.js"></script>
```

## Basic Usage

```bash
tool-name --help
```

In JavaScript:

```javascript
$("#element").truncate({width: 200});
```

### Common Options

| Option | Description |
|--------|-------------|
| `width` | Max width before truncation |
| `token` | Ellipsis token (default: '&hellip;') |
| `center` | Center truncation mode |

## Examples

### Example 1: Basic Usage

```javascript
$("#asset-id").truncate();
```

### Example 2: Advanced Usage

```javascript
$("#asset-id").truncate({width: 100, token: '...'});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Scan JS bundles for 'truncate' plugin imports
- Detection method 2: Monitor for XSS alerts in logs tied to truncation renders

## Related Procedures


## Related Tools

- [[jQuery]]

## References

- Official GitHub repo
- HackerOne report #449351
