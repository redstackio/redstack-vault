---
id: tool-uuid-3
url: 'https://www.npmjs.com/package/public'
tags:
  - static-server
  - vulnerable
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.771Z'
configuration: 'Version 0.1.2, run via bin/public with base dir and port'
validated: true
submitted: true
---
# public-module

**Status**: Unverified

## Overview

The 'public' Node.js module is a lightweight static file hosting server with directory index support, vulnerable to path traversal in version 0.1.2.

## Description

It serves files via HTTP without sanitizing paths, allowing '../' traversal to read arbitrary files. Used in testing to demonstrate supply chain vulnerabilities in npm packages.

## Features

- Feature 1: Simple static file serving
- Feature 2: Directory indexing
- Feature 3: Command-line binary for easy startup

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install public
```

## Basic Usage

```bash
./node_modules/public/bin/public ./ 8080
```

### Common Options

| Option | Description |
|--------|-------------|
| Base dir | Directory to serve | Required |
| Port | Listening port | Required |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/public/bin/public ./ 8080
```

### Example 2: Advanced Usage

```bash
./node_modules/public/bin/public /var/www 3000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'public' binary
- Port scans for unexpected HTTP servers

## Related Procedures

- [[procedures/Run-Vulnerable-Public-Server]]

## Related Tools

- [[tools/express]]

## References

- npm page: https://www.npmjs.com/package/public
- HackerOne report: https://hackerone.com/reports/312918
