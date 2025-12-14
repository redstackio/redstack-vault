---
id: tool-uuid-5
url: 'https://marked.js.org/'
tags:
  - markdown-parser
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.798Z'
validated: true
submitted: true
---
---

# marked

**Status**: Unverified

## Overview

Marked is a Markdown parser library underlying react-marked-markdown, whose link renderer is insecurely overridden, leading to the XSS vulnerability.

## Description

Parses Markdown to HTML; in this case, the sanitize option is ignored for hrefs, allowing javascript: injections.

## Features

- Feature 1: Fast Markdown-to-HTML conversion
- Feature 2: Custom renderer overrides
- Feature 3: Sanitization options (flawed in wrapper)

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install marked
```

## Basic Usage

```javascript
import { marked } from 'marked';
```

### Common Options

| Option | Description |
|--------|-------------|
| `sanitize: true` | Attempt HTML sanitization |

## Examples

### Example 1: Basic Usage

```javascript
marked('[link](url)');
```

### Example 2: Advanced Usage

```javascript
marked.parse(md, { sanitize: true });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Check for marked imports in code
- Scan for custom renderer overrides

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[react-marked-markdown]]

## References

- Official documentation: https://marked.js.org/using_marked

