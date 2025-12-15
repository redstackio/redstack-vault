---
url: 'https://www.npmjs.com/package/glance'
tags:
  - http-server
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.648Z'
id: b40eb669-7f08-49ef-ac5f-4ea07928b2da
validated: true
submitted: true
---
# glance

**Status**: Unverified

## Overview

Glance is a Node.js module for serving static files over HTTP, vulnerable to path traversal due to missing sanitization.

## Description

Glance starts a simple HTTP server on port 8080, serving directories without path validation, allowing arbitrary file reads in security testing.

## Features

- Feature 1: Static file serving
- Feature 2: Verbose logging
- Feature 3: Directory specification

## Installation

### Requirements

- Node.js
- npm

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
| `--dir` | Serve directory |
| `--verbose` | Detailed logs |

## Examples

### Example 1: Basic Usage

```bash
./bin/glance.js --dir ./public
```

### Example 2: Advanced Usage

```bash
./bin/glance.js --verbose --dir ./node_modules/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port 8080 listening with Node.js process
- Logs showing traversal attempts

## Related Procedures

- [[procedures/Start-Glance-Static-File-Server]]

## Related Tools

- [[tools/nodejs]]

## References

- npm page: https://www.npmjs.com/package/glance
