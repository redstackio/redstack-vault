---
url: 'https://nodejs.org/'
tags:
  - runtime
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:18.996Z'
id: 4d9fd84d-044f-4e09-aaaf-6b51e9455848
validated: true
submitted: true
---
# node

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime environment used to execute server-side scripts, such as running Express apps in vulnerability PoCs.

## Description

Node enables asynchronous I/O for web servers and integrates with npm for package management, crucial for testing Node.js module flaws like improper auth.

## Features

- Feature 1: Event-driven non-blocking I/O
- Feature 2: JavaScript execution
- Feature 3: Module integration

## Installation

### Requirements

- OS support (Linux, Windows, macOS)

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
| -v | Version |
| --inspect | Debug mode |

## Examples

### Example 1: Basic Usage

```bash
node index.js
```

### Example 2: Advanced Usage

```bash
node --inspect index.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- node executable running
- Process listening on ports like 3000

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
