---
id: tool-nodejs
url: 'https://nodejs.org/'
tags:
  - runtime
  - javascript
  - filesystem
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.627Z'
validated: true
submitted: true
---
# Node-js

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime built on Chrome's V8 engine, used for server-side scripting and vulnerable to path traversal in its fs module when handling Uint8Array paths in version 20.

## Description

Node.js enables execution of JavaScript outside browsers, including filesystem operations via the node:fs module. In vulnerable versions, fs functions like readFileSync fail to normalize Uint8Array paths, allowing traversal attacks to bypass permissions and access arbitrary files.

## Features

- Feature 1: Asynchronous I/O for non-blocking operations
- Feature 2: Built-in fs module for file system interactions
- Feature 3: Experimental permission system for sandboxing

## Installation

### Requirements

- Supported OS (Linux, Windows, macOS)
- Internet access for download

### Install Commands

```bash
# Using package manager (Ubuntu/Debian)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Or download from official site
wget https://nodejs.org/dist/v20.0.0/node-v20.0.0-linux-x64.tar.xz
tar -xJf node-v20.0.0-linux-x64.tar.xz
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --print` | Evaluate and print expression |
| `--experimental-permission` | Enable permission system |
| `--allow-fs-read` | Specify allowed read directories |

## Examples

### Example 1: Basic Usage

```bash
node -p 'console.log("Hello Node")'
```

### Example 2: Advanced Usage

```bash
node --experimental-permission --allow-fs-read=/tmp/ -p 'fs.readFileSync("/tmp/test.txt")'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'node' executable with experimental flags
- Audit logs showing fs access outside permitted paths
- Network traces if combined with remote exploitation

## Related Procedures

- [[procedures/Exploit-Node-js-fs-Path-Traversal-via-Uint8Array]]

## Related Tools

- [[tools/TextEncoder]] (built-in API)

## References

- Official documentation: https://nodejs.org/en/docs/
- Vulnerability report: https://hackerone.com/reports/2256167
