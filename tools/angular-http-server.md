---
id: tool-uuid-002
url: 'https://www.npmjs.com/package/angular-http-server'
tags:
  - http-server
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.698Z'
validated: true
submitted: true
---
# angular-http-server

**Status**: Unverified

## Overview

angular-http-server is a simple Node.js HTTP server for serving single-page applications (SPAs), vulnerable to path traversal allowing arbitrary file reads.

## Description

Designed for development, it serves static files but lacks path validation, making it exploitable via '../' in requests. Used in testing to demonstrate file disclosure attacks.

## Features

- Feature 1: Serves SPAs with index.html fallback
- Feature 2: Configurable port and path
- Feature 3: Basic MIME type handling

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install angular-http-server
```

## Basic Usage

```bash
angular-http-server --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--path` | Root directory to serve |
| `-p` | Port number |

## Examples

### Example 1: Basic Usage

```bash
angular-http-server --path ./
```

### Example 2: Advanced Usage

```bash
angular-http-server --path ./ -p 3000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process name angular-http-server
- Listening on non-standard ports like 8080
- Log entries for file sends outside root

## Related Procedures

- [[procedures/Setup-and-Run-angular-http-server]]

## Related Tools

- [[http-server]]

## References

- Package page: https://www.npmjs.com/package/angular-http-server
- Vulnerability report: https://hackerone.com/reports/309120
