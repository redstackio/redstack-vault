---
id: tool-lactate-001
name: lactate
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.967Z'
platforms:
  - Linux
  - Web
tags:
  - web-server
  - static-server
  - vulnerable
url: 'https://www.npmjs.com/package/lactate'
validated: true
submitted: true
---

# lactate

**Status**: Unverified

## Overview

Lactate is a minimal Node.js static file web server; version 0.13.12 is vulnerable to directory traversal, allowing arbitrary file reads via crafted GET paths in security testing.

## Description

It serves files from a directory over HTTP, but lacks path sanitization, making it ideal for demonstrating traversal attacks. Commonly used in pentests to simulate vulnerable endpoints.

## Features

- Feature 1: Simple static file serving
- Feature 2: Port specification via -p
- Feature 3: Directory listing (if enabled)

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g lactate
```

## Basic Usage

```bash
lactate --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --port` | Set listening port |
| `-d, --dir` | Set serving directory |

## Examples

### Example 1: Basic Usage

```bash
lactate -p 8081
```

### Example 2: Advanced Usage

```bash
lactate -p 8081 -d /root
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process named 'lactate' listening on non-standard ports
- HTTP logs showing traversal attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/http-server]]
- [[tools/python-http-server]]

## References

- Official documentation: https://www.npmjs.com/package/lactate
- Related resources: HackerOne report #296645
