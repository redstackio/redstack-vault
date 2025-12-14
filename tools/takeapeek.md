---
url: 'https://www.npmjs.com/package/takeapeek'
tags:
  - web-server
  - vulnerable
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.225Z'
id: 102fcfe9-5080-475e-b31e-567506fd7919
validated: true
submitted: true
---
# takeapeek

**Status**: Unverified

## Overview

takeapeek is a vulnerable Node.js module providing a simple static web server with directory listing, exploited for stored XSS via unsanitized filenames.

## Description

Version 0.2.2 fails to escape filenames in HTML, allowing javascript: injections. Used in testing to simulate misconfigured servers.

## Features

- Feature 1: Static file serving
- Feature 2: Automatic directory indexing
- Feature 3: Localhost binding on port 3141

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g takeapeek
```

## Basic Usage

```bash
takeapeek --help
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Serves current directory |

## Examples

### Example 1: Basic Usage

```bash
takeapeek
```

### Example 2: Advanced Usage

No options; runs on default port.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process listening on port 3141
- Logs showing Node.js child process

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1|http-server]]

## References

- npm page: https://www.npmjs.com/package/takeapeek
