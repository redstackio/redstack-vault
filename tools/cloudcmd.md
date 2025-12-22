---
id: tool-uuid-2
url: 'https://www.npmjs.com/package/cloudcmd'
tags:
  - file-manager
  - web
type: tool
verified: false
platforms:
  - Node.js
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.015Z'
validated: true
submitted: true
---
# cloudcmd

**Status**: Unverified

## Overview

CloudCMD is an orthodox web file manager with console and editor for Node.js, vulnerable to stored XSS in version 9.1.5 via unsanitized filenames.

## Description

It provides a web-based interface for file operations, but lacks proper HTML escaping in directory listings, allowing XSS attacks. Used in security testing to demonstrate client-side injection flaws.

## Features

- Feature 1: Web-based file browsing and editing
- Feature 2: Console integration
- Feature 3: Customizable root directory

## Installation

### Requirements

- Node.js
- npm

### Install Commands

```bash
npm i cloudcmd
```

## Basic Usage

```bash
./node_modules/cloudcmd/bin/cloudcmd.js --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --root | Set root directory |
| --port | Set port (default 8080) |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/cloudcmd/bin/cloudcmd.js --root .
```

### Example 2: Advanced Usage

```bash
./node_modules/cloudcmd/bin/cloudcmd.js --root /tmp --port 3000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: cloudcmd.js running on port 8080
- HTTP traffic to localhost:8080
- File system changes in root dir

## Related Procedures

- [[procedures/Launch-CloudCMD-Server]]

## Related Tools

- [[tools/npm]]

## References

- https://github.com/coderaiser/cloudcmd
