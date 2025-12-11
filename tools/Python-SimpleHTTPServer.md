---
url: null
tags:
  - hosting
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Simple HTTP server module in Python.
id: a9ff2a4e-6fbb-4021-9d6b-781a5d48251e
created_at: '2025-12-11T03:47:47.758Z'
updated_at: '2025-12-11T03:47:47.758Z'
verified: false
validated: true
submitted: true
---
# Python SimpleHTTPServer

**Status**: Unverified

## Overview

Python's SimpleHTTPServer module is used to host malicious HTML files on a local server for exploits like the Kibana RCE.

## Description

It serves files from the current directory over HTTP, making payloads accessible to remote targets.

## Features

- Quick setup: Single command to start server
- Port configuration: Specify listening port
- Basic serving: No authentication needed

## Installation

### Requirements

- Python 2.x (note: deprecated; use http.server in Python 3)

### Install Commands

Python built-in module, no install needed.

## Basic Usage

```bash
python -m SimpleHTTPServer --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `port` | Listening port |

## Examples

### Example 1: Basic Usage

```bash
python -m SimpleHTTPServer 8000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Python processes listening on ports
- Network scans for open HTTP servers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]

## References

- Python documentation
