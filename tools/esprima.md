---
id: tool-esprima
url: null
tags:
  - parser
  - javascript
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.415Z'
validated: true
submitted: true
---
# esprima

**Status**: Unverified

## Overview

Esprima is a JavaScript parser that generates ASTs, used internally by notevil for safe code evaluation.

## Description

It parses JS source into an abstract syntax tree, enabling notevil to inspect and restrict nodes. Vulnerabilities arise when the sandbox fails to block reconstructed constructors.

## Features

- Feature 1: High-performance parsing
- Feature 2: AST generation
- Feature 3: ECMAScript compliance

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install esprima
```

## Basic Usage

```javascript
require('esprima');
```

### Common Options

| Option | Description |
|--------|-------------|
| parse(code) | Parse to AST |

## Examples

### Example 1: Basic Usage

```javascript
var ast = esprima.parseScript('var x = 1;');
```

### Example 2: Advanced Usage

Integrate with sandbox tools.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- AST parsing in eval contexts

## Related Procedures


## Related Tools

- [[tools/notevil]]

## References

- esprima.org
