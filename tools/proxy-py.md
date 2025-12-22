---
id: tool-uuid-001
url: null
tags:
  - proxy
  - ssrf
  - http-server
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.512Z'
validated: true
submitted: true
---
# proxy-py

**Status**: Unverified

## Overview

Simple Python HTTP server/proxy for simulating internal services in SSRF attacks, returning 200 OK and logging requests on a specified port.

## Description

Custom script to listen on ports like 8500, capture incoming SSRF traffic from git clones, and respond to confirm hits. Useful for GitLab exploitation to observe leaked internal data.

## Features

- Feature 1: Listens on specified port (e.g., 8500)
- Feature 2: Logs request method, path, headers
- Feature 3: Returns static 200 OK response

## Installation

### Requirements

- Python 3

### Install Commands

```bash
# Assume script is provided; save as proxy.py
```

## Basic Usage

```bash
python3 proxy.py 8500
```

### Common Options

| Option | Description |
|--------|-------------|
| Port arg | Port to listen on |

## Examples

### Example 1: Basic Usage

```bash
python3 proxy.py 8500
```

### Example 2: Advanced Usage

No advanced options; basic listener.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: python3 proxy.py
- Port binding: netstat -lpn | grep 8500
- Logs: Unusual HTTP traffic on internal ports

## Related Procedures

- [[procedures/Start-Local-Proxy-Server-for-SSRF-Simulation]]

## Related Tools

- [[netcat]]

## References

- Custom script for SSRF testing
