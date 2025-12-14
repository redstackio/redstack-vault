---
url: 'https://www.npmjs.com/package/mcstatic'
tags:
  - http-server
  - node-js
  - vulnerable
type: tool
platforms:
  - Node.js
  - Web
description: >-
  Vulnerable static HTTP server module for Node.js, exploitable via path
  traversal.
id: a87fb3c5-d635-4d75-9c43-dc23ecf01eb8
created_at: '2025-12-14T17:26:16.755Z'
updated_at: '2025-12-14T17:26:16.755Z'
verified: false
validated: true
submitted: true
---
# mcstatic

**Status**: Unverified

## Overview

mcstatic is a lightweight Node.js module for serving static files over HTTP, vulnerable to server directory traversal in version 0.0.20 due to unsanitized paths.

## Description

Designed for simple static hosting, mcstatic lacks proper input validation, allowing attackers to read arbitrary files by crafting requests with '../' sequences. Used in security testing to demonstrate web server vulnerabilities.

## Features

- Feature 1: Basic HTTP serving on custom ports
- Feature 2: Directory listing support
- Feature 3: Minimal configuration for quick setup

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm i mcstatic
```

## Basic Usage

```bash
./node_modules/mcstatic/bin/mcstatic --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--port` | Set listening port |
| `--dir` | Serve from specific directory |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/mcstatic/bin/mcstatic --port 6060
```

### Example 2: Advanced Usage

```bash
./node_modules/mcstatic/bin/mcstatic --port 8080 --dir ./static
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Tactics

- [[Initial Access]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for mcstatic binary
- HTTP logs showing traversal attempts

## Related Procedures

- [[procedures/Start-mcstatic-Server]]

## Related Tools

- [[http-server]]
- [[express]]

## References

- HackerOne Report: https://hackerone.com/reports/330285
