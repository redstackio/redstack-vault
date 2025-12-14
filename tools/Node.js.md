---
url: 'https://nodejs.org'
tags:
  - runtime
  - javascript
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.113Z'
id: 2b70ce48-c9e9-43b6-ac99-c235a3332890
validated: true
submitted: true
---
# Node.js

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime for server-side execution, used to run TypeORM scripts and reproduce the SQL injection in a local environment.

## Description

It enables asynchronous I/O for database operations. In security testing, it's the execution environment for vulnerable code, version v8.12.0 used here.

## Features

- Feature 1: Event-driven architecture
- Feature 2: NPM integration
- Feature 3: Module system

## Installation

### Requirements

- Compatible OS (Linux, Windows, macOS)

### Install Commands

```bash
# Download from nodejs.org or use package manager
curl -fsSL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v` | Version info |
| `--trace-warnings` | Enable warnings |

## Examples

### Example 1: Basic Usage

```bash
node index.ts
```

### Example 2: Advanced Usage

```bash
node --inspect index.ts
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'node' binaries
- Port scans for default Node apps

## Related Procedures

- [[procedures/Execute-Injected-Query]]

## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://nodejs.org/en/docs
