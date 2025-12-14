---
url: 'https://nodejs.org/'
tags:
  - runtime
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.232Z'
id: 6349050e-3459-4744-8314-5f2c0d1c6177
validated: true
submitted: true
---
# nodejs

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime built on Chrome's V8 engine, used to execute server-side scripts like http-file-server for demonstrating web vulnerabilities such as stored XSS.

## Description

Node.js enables non-blocking I/O for scalable network applications. In security contexts, it's used to run vulnerable modules or custom exploits targeting web apps.

## Features

- Feature 1: Event-driven architecture
- Feature 2: npm integration
- Feature 3: Module system for packages

## Installation

### Requirements

- Linux distribution with package manager

### Install Commands

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --version` | Show version |
| `-e` | Execute string |

## Examples

### Example 1: Basic Usage

```bash
node script.js
```

### Example 2: Advanced Usage

```bash
node /path/to/http-file-server.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- node process listening on ports
- JavaScript file executions
- High CPU from V8

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://nodejs.org/en/docs/
