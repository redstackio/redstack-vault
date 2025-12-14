---
id: tool-uuid-2
url: 'https://www.npmjs.com/package/html-pages'
tags:
  - http-server
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.781Z'
validated: true
submitted: true
---
# html-pages

**Status**: Unverified

## Overview

html-pages is a lightweight Node.js HTTP server for development, serving static files and directory listings; vulnerable to stored XSS in v2.1.1 due to unsanitized directory names.

## Description

It generates HTML for directories without escaping, allowing XSS payloads in names to execute on access. Used in testing for client-side attacks like session hijacking.

## Features

- Feature 1: Automatic directory indexing
- Feature 2: Port configuration via -p flag
- Feature 3: Simple file serving

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install html-pages
```

## Basic Usage

```bash
./node_modules/html-pages/bin/index.js --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Set port (default 3000) |
| `--root` | Set root directory |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/html-pages/bin/index.js -p 6060
```

### Example 2: Advanced Usage

```bash
./node_modules/html-pages/bin/index.js -p 8080 --root ./public
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process listening on non-standard ports like 6060
- Directory listings with unsanitized content

## Related Procedures

- [[procedures/Start-html-pages-Server]]

## Related Tools

- [[tools/npm]]

## References

- Package page: https://www.npmjs.com/package/html-pages
