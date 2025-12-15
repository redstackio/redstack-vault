---
id: l2m3n4o5-p6q7-8901-lmno-234567890123
name: esprima
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.304Z'
platforms:
  - Node.js
tags:
  - parser
  - ast
url: ''
validated: true
submitted: true
---

# esprima

**Status**: Unverified

## Overview

esprima is a JavaScript parser library that generates Abstract Syntax Trees (AST) from code, used internally by tools like notevil for safe evaluation and vulnerability analysis.

## Description

In security testing, esprima helps identify exploitable patterns in JS code, such as those enabling sandbox escapes. It's lightweight and supports ECMAScript standards, making it ideal for static analysis in offensive ops.

## Features

- Feature 1: High-performance AST generation
- Feature 2: Error-tolerant parsing
- Feature 3: Integration with walkers for code transformation

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install esprima
```

## Basic Usage

```bash
node -e "console.log(require('esprima').parseScript('code'))"
```

### Common Options

| Option | Description |
|--------|-------------|
| --loc | Include line/column info in AST |
| --range | Add character ranges |

## Examples

### Example 1: Basic Usage

```javascript
var ast = require('esprima').parseScript('var x = 1;');
```

### Example 2: Advanced Usage

Parse with options: esprima.parseScript(code, {loc: true})

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence in node_modules/esprima
- AST parsing logs in app output

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/notevil]]

## References

- Official esprima documentation
