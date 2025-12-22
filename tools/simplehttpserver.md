---
id: tool-simplehttpserver
url: 'https://www.npmjs.com/package/simplehttpserver'
tags:
  - http-server
  - vulnerable
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.603Z'
validated: true
submitted: true
---
# simplehttpserver

**Status**: Unverified

## Overview

A simple Node.js HTTP server module imitating Python's SimpleHTTPServer, used for testing but vulnerable to path traversal via symlinks in v0.2.1.

## Description

This tool serves directories over HTTP without path validation, appending URLs directly to the root and following symlinks, enabling attacks to access outside directories. Common in dev/testing; avoid in production due to flaws.

## Features

- Feature 1: Directory listing on GET requests
- Feature 2: Serves static files
- Feature 3: Port 8000 default

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install simplehttpserver -g
```

## Basic Usage

```bash
simplehttpserver --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `<dir>` | Web root directory |
| `-p` | Custom port |

## Examples

### Example 1: Basic Usage

```bash
simplehttpserver ./
```

### Example 2: Advanced Usage

```bash
simplehttpserver /var/www -p 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'node simplehttpserver.js'
- Port scans for 8000 with directory listings

## Related Procedures

- [[procedures/Start-simplehttpserver-with-Current-Directory]]

## Related Tools

- [[Python's SimpleHTTPServer]]

## References

- npm page: https://www.npmjs.com/package/simplehttpserver
