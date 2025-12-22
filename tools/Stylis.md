---
url: null
tags:
  - css
  - preprocessor
type: tool
platforms:
  - Web
description: >-
  CSS preprocessor used by Mermaid to generate and insert style rules from
  configurations.
id: e7f63bcc-d384-46cb-bcda-e5d87c306f72
created_at: '2025-12-13T23:52:24.539Z'
updated_at: '2025-12-13T23:52:24.539Z'
verified: false
validated: true
submitted: true
---
# Stylis

**Status**: Unverified

## Overview

Stylis is a lightweight CSS parser and minifier, employed in Mermaid for compiling theme variables into style tags, vulnerable when user input is unsanitized.

## Description

It processes config objects to create CSS rules (e.g., `#id { font-family: user-input }`), inserting via innerHTML, allowing breakout injections in vulnerable setups.

## Features

- Feature 1: CSS rule generation from JS objects
- Feature 2: Minification and scoping
- Feature 3: innerHTML output

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install stylis
```

## Basic Usage

```bash
stylis --help
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | API-based |

## Examples

### Example 1: Basic Usage

```javascript
const stylis = new Stylis();
stylis('#id', 'color: red');
```

### Example 2: Advanced Usage

```javascript
stylis.process('#graph', userStyles, themeVariables);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Inspect generated style tags for anomalies
- Log CSS insertion events

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mermaid]]

## References

- Related resources
