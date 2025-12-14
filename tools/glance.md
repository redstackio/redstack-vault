---
id: tool-uuid-2
url: 'https://www.npmjs.com/package/glance'
tags:
  - http-server
  - static-files
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.945Z'
validated: true
submitted: true
---
# glance

**Status**: Unverified

## Overview

Glance is a lightweight Node.js HTTP server for serving static files, vulnerable to Stored XSS due to unsanitized file names in directory listings.

## Description

It generates simple HTML listings but fails to escape file names, allowing JavaScript injection. Used in testing for demonstrating web vulnerabilities in Node.js apps.

## Features

- Feature 1: Disposable static file serving
- Feature 2: Directory listing generation
- Feature 3: Verbose logging support

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install glance
```

## Basic Usage

```bash
glance --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--dir` | Root directory |
| `--verbose` | Detailed logs |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/glance/bin/glance.js --dir ./
```

### Example 2: Advanced Usage

```bash
./node_modules/glance/bin/glance.js --verbose --dir ./
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port 3000 listening with Node.js process
- Logs showing Glance startup

## Related Procedures

- [[procedures/Run-Glance-Server]]

## Related Tools

- [[tools/npm]]

## References

- npm page: https://www.npmjs.com/package/glance
