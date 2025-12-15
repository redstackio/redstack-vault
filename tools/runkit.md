---
id: m3n4o5p6-q7r8-9012-mnop-345678901234
name: runkit
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.299Z'
platforms:
  - Web
  - Node.js
tags:
  - playground
  - testing
url: 'http://runkit.com/phra/notevil---sandbox-escape'
validated: true
submitted: true
---

# runkit

**Status**: Unverified

## Overview

Runkit is an online Node.js playground for executing and sharing code snippets, useful for quickly testing vulnerabilities like the notevil sandbox escape without local setup.

## Description

It provides a REPL-like interface with npm integration, ideal for PoC development in offensive security. The specific example at the URL demonstrates the notevil exploit.

## Features

- Feature 1: Instant Node.js execution in browser
- Feature 2: npm package require support
- Feature 3: Shareable notebooks for PoCs

## Installation

### Requirements

- Web browser

### Install Commands

No installation; access via web.

## Basic Usage

```bash
# Visit https://runkit.com and paste code
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based, no CLI |

## Examples

### Example 1: Basic Usage

Paste require('notevil') and safeEval code into a new notebook.

### Example 2: Advanced Usage

Use for multi-step exploits with console.log outputs.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to runkit.com domains
- Embedded runkit iframes in testing docs

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

- http://runkit.com/phra/notevil---sandbox-escape
