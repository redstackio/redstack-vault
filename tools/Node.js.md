---
url: 'https://nodejs.org'
tags:
  - runtime
  - javascript
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.384Z'
id: 2363d9f5-a9e2-4bde-9e27-0f960ec3c795
validated: true
submitted: true
---
# Node.js

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime environment built on Chrome's V8 engine, used for server-side scripting and vulnerable to the experimental permission model path traversal issue in version 20.x.

## Description

Node.js enables execution of JavaScript outside browsers, including file system access via the 'fs' module. In this context, it's exploited to demonstrate bypassing the experimental permission model by overwriting path.resolve, allowing unauthorized file reads in restricted environments.

## Features

- Feature 1: Asynchronous I/O for file operations
- Feature 2: Built-in modules like 'path' and 'fs' for system interactions
- Feature 3: Experimental permission model for sandboxing (vulnerable in 20.x)

## Installation

### Requirements

- Linux OS
- Build tools (gcc, make)

### Install Commands

```bash
# Download and install latest (use 20.x for vuln demo)
curl -fsSL https://nodejs.org/dist/v20.0.0/node-v20.0.0-linux-x64.tar.xz | tar -xJ
sudo mv node-v20.0.0-linux-x64 /opt/nodejs
sudo ln -s /opt/nodejs/bin/node /usr/local/bin/node
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Evaluate string as code |
| `--experimental-permission` | Enable permission model |
| `--allow-fs-read` | Allow FS reads in specified paths |

## Examples

### Example 1: Basic Usage

```bash
node -p "console.log('Hello Node')
```

### Example 2: Advanced Usage

```bash
node --experimental-permission --allow-fs-read=/tmp/ -p "fs.readFileSync('/tmp/file.txt')"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[File and Directory Discovery]]

### Tactics

- [[Execution]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'node' with --experimental-permission flags
- File access logs showing unexpected reads (e.g., /etc/passwd)
- Code analysis for path.resolve overwrites

## Related Procedures

- [[procedures/Enable-Node.js-Experimental-Permission-Model]]
- [[procedures/Overwrite-path.resolve-Function]]

## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://nodejs.org/en/docs
- Vulnerability report: https://hackerone.com/reports/2225660
