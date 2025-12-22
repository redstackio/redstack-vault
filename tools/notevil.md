---
id: k1l2m3n4-o5p6-7890-klmn-123456789012
name: notevil
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.314Z'
platforms:
  - Node.js
tags:
  - sandbox
  - javascript
url: 'https://www.npmjs.com/package/notevil'
validated: true
submitted: true
---

# notevil

**Status**: Unverified

## Overview

notevil is a Node.js module for safe JavaScript evaluation, using esprima to parse code into an AST and restrict access to dangerous globals, commonly used in scenarios requiring user input execution like form validation.

## Description

It wraps the evaluation context to block access to constructors like Function or process, but version 1.3.2 is vulnerable to sandbox escape via prototype descriptor manipulation. In offensive security, it's exploited for RCE in Node.js apps or XSS in browser deps. Features include AST walking to rename/omit globals.

## Features

- Feature 1: esprima-based AST parsing for safe code analysis
- Feature 2: Global object wrapping to prevent escapes
- Feature 3: Support for limited expressions in safe contexts

## Installation

### Requirements

- Node.js v10+
- npm

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
| -h, --help | Show usage (if CLI wrapper used) |
| -v, --version | Display version |

## Examples

### Example 1: Basic Usage

```javascript
var safeEval = require('notevil'); safeEval('1+1');
```

### Example 2: Advanced Usage

```javascript
safeEval('malicious code'); // Exploitable in v1.3.2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor npm installs for notevil@1.3.2
- Scan for safeEval calls in source code
- Detect anomalous util.log in safe contexts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/esprima]]

## References

- https://www.npmjs.com/package/notevil
- HackerOne Report #809012
