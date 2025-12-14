---
url: 'https://www.npmjs.com/package/dy-server2'
tags:
  - http-server
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.453Z'
id: 61f9de8a-5747-4f5b-be07-15eb4474f449
validated: true
submitted: true
---
# dy-server2

**Status**: Unverified

## Overview

dy-server2 is a lightweight Node.js HTTP server for file transfer and frontend project previews, vulnerable to stored XSS due to unsanitized file/folder name rendering.

## Description

It provides a simple way to serve static files over HTTP, commonly used in development. In security contexts, its lack of input sanitization allows XSS exploitation via malicious names. Features include port specification and directory serving.

## Features

- Feature 1: Simple static file serving
- Feature 2: Custom port binding
- Feature 3: Directory listing without escaping

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm i -g dy-server2
```

## Basic Usage

```bash
dy-server2 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --port` | Set listening port |
| `-h, --help` | Show help |

## Examples

### Example 1: Basic Usage

```bash
dy-server2 -p 8888
```

### Example 2: Advanced Usage

```bash
dy-server2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for dy-server2.exe or node dy-server2
- Port scans showing HTTP on non-standard ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1|http-server]]

## References

- Official documentation: https://www.npmjs.com/package/dy-server2
