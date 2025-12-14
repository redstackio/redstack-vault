---
id: tool-uuid-4
url: 'https://www.npmjs.com/package/flsaba'
tags:
  - http-server
  - vulnerable
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.318Z'
validated: true
submitted: true
---
---

# flsaba

**Status**: Unverified

## Overview

Fl saba is a simple Node.js HTTP server module with directory listing, vulnerable to stored XSS in version 1.1.0 due to unsanitized name insertion in HTML.

## Description

Designed for quick file serving, it lacks input validation, making it ideal for demonstrating web vulns in local testing scenarios.

## Features

- Feature 1: Automatic directory listing
- Feature 2: Serves static files
- Feature 3: Default port 3000

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g flsaba
```

## Basic Usage

```bash
flsaba --help
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Defaults to current dir, port 3000 |

## Examples

### Example 1: Basic Usage

```bash
flsaba
```

### Example 2: Advanced Usage

```bash
PORT=8080 flsaba
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process named flsaba listening on 3000
- HTTP traffic to localhost:3000
- Package logs in npm history

## Related Procedures


## Related Tools

- [[tools/npm]]

## References

- Official documentation: https://www.npmjs.com/package/flsaba
- HackerOne report: https://hackerone.com/reports/856588

