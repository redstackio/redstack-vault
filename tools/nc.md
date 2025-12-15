---
id: tool-uuid-002
url: 'https://nc110.sourceforge.net/'
tags:
  - listener
  - network
  - tcp
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.393Z'
validated: true
submitted: true
---
# nc

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking utility for reading/writing data across TCP/UDP connections, often used as a listener to capture incoming requests in SSRF testing.

## Description

nc excels at creating simple servers or clients for protocol testing. Here, it's configured to listen on a port to observe SSRF-forwarded HTTP requests from GitLab, confirming internal pivoting.

## Features

- Feature 1: TCP/UDP listening (-l)
- Feature 2: Bind to specific IP/port
- Feature 3: Raw data capture without protocol overhead

## Installation

### Requirements

- Unix-like system (often pre-installed as netcat)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install netcat-openbsd

# On macOS
brew install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Listen mode |
| `-p` | Specify port |
| `-v` | Verbose |

## Examples

### Example 1: Basic Usage

```bash
nc -l 8080
```

### Example 2: Advanced Usage

```bash
nc -l 0.0.0.0 81 -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]
- [[Network Service Scanning]]

### Tactics

- [[Reconnaissance]]
- [[Command and Control]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process listings showing nc -l on non-standard ports
- Inbound connections from app servers to unexpected listeners
- Network flow logs with ephemeral ports

## Related Procedures

- [[procedures/Observe-SSRF-Request-with-Netcat]]

## Related Tools

- [[Related Tool 1|socat]]
- [[Related Tool 2|tcpdump]]

## References

- Official documentation: https://nc110.sourceforge.net/netcat.html
