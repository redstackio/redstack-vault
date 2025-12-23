---
id: tool-runkit
url: 'http://runkit.com/phra/notevil---sandbox-escape'
tags:
  - nodejs
  - online-ide
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.422Z'
validated: true
submitted: true
---
# RunKit

**Status**: Unverified

## Overview

RunKit is an online Node.js environment for executing and sharing JavaScript code snippets, ideal for testing POCs like the notevil sandbox escape.

## Description

It provides a REPL-like interface in the browser, supporting npm requires and console output, used here to demonstrate RCE without local setup.

## Features

- Feature 1: Instant Node.js execution
- Feature 2: npm package integration
- Feature 3: Shareable notebooks

## Installation

### Requirements

- Web browser

### Install Commands

No installation; access via URL.

## Basic Usage

```bash
# Visit and paste code
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Browser-based |

## Examples

### Example 1: Basic Usage

Visit http://runkit.com and run require('notevil').

### Example 2: Advanced Usage

Paste full POC for sandbox escape.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to runkit.com
- Embedded Node.js execution logs

## Related Procedures


## Related Tools

- [[tools/notevil]]

## References

- Official site: runkit.com
