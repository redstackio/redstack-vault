---
url: 'https://nodejs.org/'
tags:
  - runtime
  - javascript
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.907Z'
id: c2f4d526-3092-41ad-8dc5-a6617f5f24e0
validated: true
submitted: true
---
# node

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime built on Chrome's V8 engine, used to execute server-side scripts like the webpack-bundle-analyzer binary in this local XSS attack.

## Description

Node enables running JS outside browsers, ideal for build tools and analyzers. In security testing, it's used to launch vulnerable applications for exploitation demonstration.

## Features

- Feature 1: Asynchronous I/O for efficient execution
- Feature 2: Module system for package integration
- Feature 3: REPL for interactive debugging

## Installation

### Requirements

- Supported OS (Linux, macOS, Windows)

### Install Commands

```bash
# Download from nodejs.org or use package manager
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --version` | Print Node.js version |
| `-e` | Evaluate script |

## Examples

### Example 1: Basic Usage

```bash
node script.js
```

### Example 2: Advanced Usage

```bash
node ./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js poc.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- node process in ps aux
- Port listening on 8888

## Related Procedures

- [[procedures/Run-Analyzer-on-Malicious-JSON]]

## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://nodejs.org/en/docs/
