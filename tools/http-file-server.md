---
id: tool-http-file-server
url: 'https://www.npmjs.com/package/http-file-server'
tags:
  - file-server
  - vulnerable
  - http
type: tool
verified: false
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.563Z'
validated: true
submitted: true
---
# http-file-server

**Status**: Unverified

## Overview

http-file-server is a lightweight Node.js module for serving files over HTTP, vulnerable to path traversal in version 0.2.6, used in testing to demonstrate directory access flaws.

## Description

It appends URL paths directly to a root directory without validation, allowing traversal attacks. Primarily for development/testing, but highlights insecure file serving practices.

## Features

- Feature 1: Simple HTTP file serving from a specified path
- Feature 2: Configurable host and port binding
- Feature 3: Directory listing support

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g http-file-server@0.2.6
```

## Basic Usage

```bash
http-file-server --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--path` | Set root directory |
| `--host` | Bind to host (e.g., *) |
| `--port` | Listening port |

## Examples

### Example 1: Basic Usage

```bash
./http-file-server.js --path=/tmp/ --port=1234
```

### Example 2: Advanced Usage

```bash
./http-file-server.js --path=/tmp/ --host=* --port=1234
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process running http-file-server.js
- HTTP traffic on non-standard ports like 1234
- Log entries for file access outside root

## Related Procedures

- [[procedures/Start-http-file-server-with-Tmp-Root]]

## Related Tools

- [[tools/python-http-server]]
- [[tools/nginx]]

## References

- Official documentation: npm package page
- Related resources: HackerOne report #570133
