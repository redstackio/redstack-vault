---
id: tool-398285-serve
url: 'https://www.npmjs.com/package/serve'
tags:
  - web-server
  - xss-vulnerable
type: tool
verified: false
platforms:
  - Web
  - Node.js
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.880Z'
validated: true
submitted: true
---
# serve

**Status**: Unverified

## Overview

Serve is a lightweight Node.js static file server with a CLI, vulnerable to stored XSS in v9.6.0 due to unsanitized directory listings, used here to host malicious filenames for payload execution.

## Description

Serve provides simple HTTP serving for development, but its directory handler inserts filenames into HTML without escaping, enabling XSS. Common in local testing; impact includes JS execution for any viewer.

## Features

- Feature 1: Automatic directory listing
- Feature 2: Port and listen options
- Feature 3: Static asset compression

## Installation

### Requirements

- Node.js v10+
- yarn or npm

### Install Commands

```bash
yarn global add serve
```

## Basic Usage

```bash
serve --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Set port (default 5000) |
| -s | Single page app mode |

## Examples

### Example 1: Basic Usage

```bash
serve
```

### Example 2: Advanced Usage

```bash
serve -p 3000 .
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port 5000 listening processes
- serve binary in global PATH
- Logs showing directory access

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools


## References

- Official documentation: https://www.npmjs.com/package/serve
- Related resources: HackerOne report #398285
