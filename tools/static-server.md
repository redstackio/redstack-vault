---
id: tool-static-server
url: null
tags:
  - http-server
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.461Z'
configuration: Runs on port 8080
validated: true
submitted: true
---
# static-server

**Status**: Unverified

## Overview

A simple static file server (e.g., Python http.server or npm http-server) to host HTML and JS files locally for PoC, simulating an attacker site in XSS exploits.

## Description

Serves files over HTTP without processing, ideal for hosting malicious OG HTML. Configured on port 8080 for this attack.

## Features

- Feature 1: Serve directories
- Feature 2: Custom port binding
- Feature 3: Basic logging

## Installation

### Requirements

- Python or Node.js

### Install Commands

```bash
# Python built-in
# Or npm install -g http-server
```

## Basic Usage

```bash
http-server -p 8080
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Port number |
| -a | Address to bind |
| --cors | Enable CORS |

## Examples

### Example 1: Basic Usage

```bash
python -m http.server 8080
```

### Example 2: Advanced Usage

```bash
http-server ./ -p 8080 --cors
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Protocols]] Web Protocols

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Port 8080 listening
- Directory listings
- Simple HTTP responses

## Related Procedures


## Related Tools

- [[tools/node]]

## References

- Python: https://docs.python.org/3/library/http.server.html
