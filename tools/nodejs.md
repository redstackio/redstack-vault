---
url: 'https://nodejs.org/'
tags:
  - runtime
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.637Z'
id: 3100b7e9-e812-46e3-ae04-7a32912a4b41
validated: true
submitted: true
---
# nodejs

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime for server-side execution, used to run the Glance module and host the vulnerable server.

## Description

Node.js enables non-blocking I/O for scalable applications, including HTTP servers like Glance. In security contexts, it's used to deploy and test vulnerable Node modules.

## Features

- Feature 1: Event-driven architecture
- Feature 2: Module support via npm
- Feature 3: Built-in HTTP server

## Installation

### Requirements

- Compatible OS

### Install Commands

```bash
# Download from nodejs.org or use package manager
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
| `-v` | Version |
| `--version` | Node version |

## Examples

### Example 1: Basic Usage

```bash
node script.js
```

### Example 2: Advanced Usage

```bash
node --version
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process named 'node' running
- Port bindings on non-standard ports

## Related Procedures

- [[procedures/Start-Glance-Static-File-Server]]

## Related Tools

- [[tools/npm]]

## References

- Official site: https://nodejs.org/
