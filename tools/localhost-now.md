---
url: 'https://www.npmjs.com/package/localhost-now'
tags:
  - web-server
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.616Z'
id: 2f221894-27ff-493d-9baa-e27d5f4b5004
validated: true
submitted: true
---
# localhost-now

**Status**: Unverified

## Overview

A Node.js module for starting a simple local web server to test HTML/JS files without full setups like Apache. Version 1.0.2 is vulnerable to path traversal.

## Description

Provides a quick HTTP server for local development. In security testing, it's used to demonstrate path traversal flaws where lib/app.js inadequately sanitizes paths, allowing arbitrary file reads.

## Features

- Feature 1: Simple command-line server startup
- Feature 2: Serves static files from current directory
- Feature 3: Basic HTTP handling (vulnerable in v1.0.2)

## Installation

### Requirements

- Node.js v8.10.0+
- NPM 5.6.0+

### Install Commands

```bash
npm install localhost-now@1.0.2
```

## Basic Usage

```bash
localhost --help
```

### Common Options

| Option | Description |
|--------|-------------|
| Port arg | Specify port, e.g., 5432 |

## Examples

### Example 1: Basic Usage

```bash
localhost 5432
```

### Example 2: Advanced Usage

```bash
localhost 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'localhost' Node.js binary
- Network logs showing binds on non-standard ports like 5432

## Related Procedures

- [[procedures/Start-localhost-now-Server]]

## Related Tools

- [[http-server]]

## References

- https://www.npmjs.com/package/localhost-now
