---
url: 'https://nodejs.org'
tags:
  - runtime
  - web
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  JavaScript runtime for building server-side applications, used here to
  demonstrate vulnerabilities in its HTTP parsing.
id: f3bab32a-6f92-4531-a10f-2e0a1ab7dc06
created_at: '2025-12-13T09:01:17.414Z'
updated_at: '2025-12-13T09:01:17.414Z'
verified: false
validated: true
submitted: true
---
# Node.js

**Status**: Unverified

## Overview

Node.js is a JavaScript runtime built on Chrome's V8 engine, commonly used for server-side applications. In security testing, it's used to replicate environments for vulnerabilities like HTTP Request Smuggling in its http module.

## Description

Node.js includes the http module with llhttp parser, which can be vulnerable to issues like improper header folding. It's used to set up test servers for exploit demonstrations.

## Features

- Asynchronous event-driven architecture
- Built-in HTTP server capabilities
- Extensive module ecosystem

## Installation

### Requirements

- Compatible OS
- Internet access for download

### Install Commands

```bash
# Install via package manager or download from official site
```

## Basic Usage

```bash
node --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Show version |

## Examples

### Example 1: Basic Usage

```bash
node server.js
```

### Example 2: Advanced Usage

```bash
node --inspect server.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for Node.js processes handling HTTP traffic
- Check logs for parsing errors or unusual headers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/printf]]
- [[tools/nc]]

## References

- https://nodejs.org/en/docs/
- HackerOne report: https://hackerone.com/reports/1501679
