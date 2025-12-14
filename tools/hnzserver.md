---
id: 123e4567-e89b-12d3-a456-426614174008
name: hnzserver
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.439Z'
platforms:
  - Linux
  - Node.js
tags:
  - static-server
  - vulnerable
url: 'https://www.npmjs.com/package/hnzserver'
validated: true
submitted: true
---

# hnzserver

**Status**: Unverified

## Overview

hnzserver is a simple Node.js-based static file server that serves files from the current directory on port 8888. Version 2.0.6 is vulnerable to path traversal, allowing arbitrary file reads outside the root.

## Description

This tool is designed for quick local file serving but lacks security features like path sanitization, making it suitable for vulnerability demos in security research. It uses Node.js HTTP module internally.

## Features

- Feature 1: Automatic serving from current directory
- Feature 2: Default port 8888 binding
- Feature 3: Basic MIME type handling for files

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g hnzserver
```

## Basic Usage

```bash
hnzserver --help
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | Start server on port 8888 |

## Examples

### Example 1: Basic Usage

```bash
hnzserver
```

### Example 2: Advanced Usage

```bash
cd /path/to/dir && hnzserver
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'hnzserver' or Node.js on port 8888
- Network logs showing HTTP traffic to localhost:8888
- File system scans for unsanitized server outputs

## Related Procedures

- [[procedures/Start-hnzserver-Static-Server]]

## Related Tools

- [[tools/http-server]]
- [[tools/python-http-server]]

## References

- Official documentation: https://www.npmjs.com/package/hnzserver
- Related resources: HackerOne report #579517
