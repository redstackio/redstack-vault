---
id: tool-notevil
url: 'https://www.npmjs.com/package/notevil'
tags:
  - sandbox
  - javascript
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.418Z'
configuration: Version 1.3.2
validated: true
submitted: true
---
# notevil

**Status**: Unverified

## Overview

notevil is a Node.js module providing a safe alternative to eval() by parsing JavaScript with esprima and restricting dangerous AST nodes, vulnerable in v1.3.2 to sandbox escape.

## Description

It evaluates code in a sandboxed context, but flaws allow prototype manipulation for arbitrary execution. Used in apps like react-schema-form for form condition evaluation.

## Features

- Feature 1: AST-based safe evaluation
- Feature 2: Blacklist of dangerous globals
- Feature 3: Browser and Node.js support

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install notevil@1.3.2
```

## Basic Usage

```javascript
require('notevil');
```

### Common Options

| Option | Description |
|--------|-------------|
| safeEval(code) | Evaluate sandboxed code |

## Examples

### Example 1: Basic Usage

```javascript
var result = safeEval('1+1');
```

### Example 2: Advanced Usage

Pass malicious payload for escape.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Dependency scans showing v1.3.2
- Logs of safeEval calls

## Related Procedures


## Related Tools

- [[tools/esprima]]

## References

- npm: https://www.npmjs.com/package/notevil
