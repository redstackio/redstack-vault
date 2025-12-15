---
id: tool-uuid-002
url: 'https://www.npmjs.com/package/statics-server'
tags:
  - static-server
  - vulnerable
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.359Z'
validated: true
submitted: true
---
# statics-server

**Status**: Unverified

## Overview

A Node.js module for serving static files from a directory; vulnerable version (0.0.9) used to host files and follow symlinks without restrictions.

## Description

Statics-server is a lightweight HTTP server for static content, but its lack of symlink checks in v0.0.9 enables path traversal exploits in offensive security scenarios.

## Features

- Feature 1: Simple directory serving
- Feature 2: Default localhost:8080 binding
- Feature 3: No authentication or validation

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install statics-server -g
```

## Basic Usage

```bash
statics-server --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--port` | Specify port |
| `-h, --help` | Show help |

## Examples

### Example 1: Basic Usage

```bash
statics-server
```

### Example 2: Advanced Usage

```bash
statics-server --port 3000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'statics-server' on port 8080
- Network logs for local HTTP traffic

## Related Procedures

- [[procedures/Run-Statics-Server-in-Directory]]

## Related Tools

- [[tools/nginx]]

## References

- Package page: https://www.npmjs.com/package/statics-server
