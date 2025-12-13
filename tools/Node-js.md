---
url: null
tags:
  - runtime
type: tool
platforms:
  - Linux
  - Web
description: >-
  JavaScript runtime for building servers and scripts, vulnerable to HTTP
  smuggling in certain versions.
id: abba356d-6def-4dd5-9029-9c2e4eb02e62
created_at: '2025-12-13T09:01:22.059Z'
updated_at: '2025-12-13T09:01:22.059Z'
verified: false
validated: true
submitted: true
---
# Node.js

**Status**: Unverified

## Overview

Node.js is an open-source, cross-platform JavaScript runtime environment that executes JavaScript code outside a web browser, used for backend servers and exploitation scripts.

## Description

Versions 14.13.1 or 12.19.0 use http and net modules for servers and clients, with a bug in handling duplicate headers.

## Features

- Asynchronous I/O: Non-blocking operations
- Modules: Built-in http, net
- npm integration: Package management

## Installation

### Requirements

- OS-specific installer

### Install Commands

```bash
# Use package manager or official installer
```

## Basic Usage

```bash
node script.js
```

### Common Options

| Option | Description |
|--------|-------------|
| `DEBUG=*` | Enable debug |

## Examples

### Example 1: Basic Usage

```bash
node app.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Node.js processes
- Check for vulnerable versions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Express]]

## References

- Node.js official documentation
