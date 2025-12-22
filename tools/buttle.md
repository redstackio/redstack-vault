---
url: 'https://www.npmjs.com/package/buttle'
tags:
  - server
  - static-file
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.821Z'
id: c0fc4ffe-2c7e-4997-aeff-0d7263b17cca
validated: true
submitted: true
---
# buttle

**Status**: Unverified

## Overview

Buttle is a lightweight Node.js static file and markdown server, vulnerable to stored XSS in version 0.2.0 due to unsanitized directory listings. Used in testing to demonstrate HTML injection via filenames.

## Description

Built on the connect framework, buttle serves files and generates HTML indexes. The vulnerability allows arbitrary JS execution when viewing listings, useful for client-side attack simulations.

## Features

- Feature 1: Static file serving
- Feature 2: Markdown rendering
- Feature 3: Directory indexing (vulnerable)

## Installation

### Requirements

- Node.js
- npm

### Install Commands

```bash
npm i buttle
```

## Basic Usage

```bash
./node_modules/buttle/bin/buttle --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p` | Port to bind |
| `-h, --help` | Show help |

## Examples

### Example 1: Basic Usage

```bash
./node_modules/buttle/bin/buttle -p 8080
```

### Example 2: Advanced Usage

```bash
./node_modules/buttle/bin/buttle -p 3000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port listening on non-standard ports
- Process named buttle
- Directory listing access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[connect]]

## References

- https://www.npmjs.com/package/buttle
